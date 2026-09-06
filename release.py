"""Build this repository's standalone InxPackage and GitHub release manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import package

RUNTIME_ENGINE_VERSION = "0.4.0"


def player_payload() -> tuple[Path, tuple[str, ...]]:
    """Require the complete CMake-built payload before publishing a release."""
    root = Path(__file__).resolve().parent
    platform = json.loads((root / "package/inx_package.json").read_text(encoding="utf-8"))["reference"].rsplit("-", 1)[1]
    payload = root / "package/editor" / f"infernux_{platform}" / "player"
    document = json.loads((payload / "Player.inxmanifest").read_text(encoding="utf-8"))
    expected = {
        "engine_version": RUNTIME_ENGINE_VERSION,
        "python_abi": "cp313",
        "platform": "win32" if platform == "windows" else "linux",
        "distribution": "platform-plugin",
    }
    if any(document.get(key) != value for key, value in expected.items()) or (
        str(document.get("machine", "")).casefold() not in {"amd64", "x86_64"}
    ):
        raise ValueError("Player payload does not match the platform plugin's engine/ABI contract")
    host = "InfernuxPlayerHost.exe" if platform == "windows" else "InfernuxPlayerHost"
    for name, magic in (("Runtime.inxrt", b"INXPKG\0\0"), ("Parallel.inxmod", b"INXPKG\0\0"),
                        (host, b"MZ" if platform == "windows" else b"\x7fELF")):
        with (payload / name).open("rb") as source:
            if source.read(len(magic)) != magic:
                raise ValueError(f"Invalid precompiled Player payload: {name}")
    return payload, ("Player.inxmanifest", "Runtime.inxrt", "Parallel.inxmod", host)


def build_release(tag: str | None = None, output: Path | None = None) -> tuple[Path, Path]:
    root = Path(__file__).resolve().parent
    metadata = json.loads((root / "package/inx_package.json").read_text(encoding="utf-8"))
    expected = f"v{metadata['version']}"
    if tag is None:
        tag = expected
    if tag != expected:
        raise ValueError(f"Release tag must match package version: {expected}")
    player_payload()
    destination = output if output is not None else root / "dist"
    destination.mkdir(parents=True, exist_ok=True)
    stem = metadata["reference"].replace("/", ".")
    artifact = package.build(destination / f"{stem}.inxpkg")
    manifest = destination / f"{stem}.release.json"
    document = {
        "$schema": "infernux.plugin_release",
        "reference": metadata["reference"],
        "version": metadata["version"],
        "engine": metadata["engine"],
        "artifact": {"name": artifact.name},
        "generator": "Infernux platform package release.py",
        "release_tag": tag,
    }
    manifest.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return artifact, manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag", nargs="?", help="v followed by package/inx_package.json version")
    arguments = parser.parse_args()
    for path in build_release(arguments.tag):
        print(path)
