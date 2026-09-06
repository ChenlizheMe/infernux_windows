"""Packaging tests run without installing Infernux or a platform SDK."""

import json
from pathlib import Path
import tempfile
import unittest
import shutil
from unittest.mock import patch

import release


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name) / "repository"
        source = Path(__file__).resolve().parents[1]
        shutil.copytree(source / "package", self.root / "package", ignore=shutil.ignore_patterns("player"))
        self.payload = self.root / "package/editor/infernux_windows/player"
        self.payload.mkdir()
        (self.payload / "Player.inxmanifest").write_text(json.dumps({
            "engine_version": release.RUNTIME_ENGINE_VERSION, "python_abi": "cp313",
            "platform": "win32", "machine": "x86_64", "distribution": "platform-plugin",
        }), encoding="utf-8")
        for name in ("Runtime.inxrt", "Parallel.inxmod"):
            (self.payload / name).write_bytes(b"INXPKG\0\0fixture")
        (self.payload / "InfernuxPlayerHost.exe").write_bytes(b"MZfixture")
        for module in (release, release.package):
            override = patch.object(module, "__file__", str(self.root / Path(module.__file__).name))
            override.start()
            self.addCleanup(override.stop)

    def test_release_rejects_exporter_only_package(self):
        (self.payload / "Runtime.inxrt").unlink()
        with self.assertRaises(FileNotFoundError):
            release.build_release("v0.2.0")
        self.assertFalse((self.root / "dist").exists())

    def test_release_rejects_wrong_engine_payload(self):
        manifest = self.payload / "Player.inxmanifest"
        document = json.loads(manifest.read_text())
        document["engine_version"] = "0.3.7"
        manifest.write_text(json.dumps(document), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "engine/ABI"):
            release.build_release("v0.2.0")

    def test_cmake_entry_produces_only_the_final_inxpackage_and_manifest(self):
        artifact, manifest = release.build_release()
        self.assertEqual(set((self.root / "dist").iterdir()), {artifact, manifest})
        self.assertEqual(artifact.suffix, ".inxpkg")
        self.assertFalse(list(self.root.rglob("*.zip")))

    def test_package_and_manifest(self):
        root = Path(__file__).resolve().parents[1]
        source = json.loads((root / "package/inx_package.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as temporary:
            artifact, manifest = release.build_release(f"v{source['version']}", Path(temporary))
            document = json.loads(manifest.read_text(encoding="utf-8"))
            self.assertEqual(document["artifact"]["name"], artifact.name)
            self.assertEqual(document["reference"], source["reference"])
            self.assertEqual(document["engine"], source["engine"])
            self.assertEqual(artifact.read_bytes()[:8], b"INXPKG\0\0")
            self.assertGreater(artifact.stat().st_size, 1024)
        self.assertTrue((root / "package/plugin_pages/media/overview.png").is_file())
        for name in ("README.md", "README.zh-CN.md"):
            self.assertIn("package/plugin_pages/media/overview.png", (root / name).read_text(encoding="utf-8"))

    def test_reject_mismatched_tag(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError, "Release tag must match"):
                release.build_release("v999.0.0", Path(temporary))
            self.assertEqual(list(Path(temporary).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
