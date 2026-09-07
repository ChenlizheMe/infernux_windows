# Infernux Windows Platform

The official Windows build plugin for [Infernux](https://github.com/ChenlizheMe/Infernux), an open-source game engine with a C++17/Vulkan core and Python authoring layer. Install this plugin to export an Infernux project as a native Windows x64 game without compiling the engine yourself.

[简体中文](README.zh-CN.md) · [Infernux Engine](https://github.com/ChenlizheMe/Infernux) · [Plugin Template](https://github.com/ChenlizheMe/infernux_plugin_template) · [Releases](https://github.com/ChenlizheMe/infernux_windows/releases)

![Infernux Windows export workflow](package/plugin_pages/media/overview.png)

## What this plugin provides

- The `windows-x64` build target in the Infernux Editor
- A precompiled native Player, CPython 3.13 runtime, and parallel module
- Vulkan rendering and the Windows export pipeline
- Binary game-content packaging instead of an editable `Assets`/`Library` tree

| Package | Version | Compatible engine | Build host | Target |
| --- | --- | --- | --- | --- |
| `infernux/platform-windows` | 0.2.0 | Infernux 0.4.0 | Windows x64 | Windows x64 |

## Install and use

Open **Plugins** in Infernux, select **Infernux Windows Platform** from the official catalog, then import and enable it. Official installs use the Infernux distribution service first and GitHub Releases if that channel is unavailable. You can also download `infernux.platform-windows.inxpkg` from this repository's Releases page and import it manually.

Open the build settings, choose `windows-x64`, and export. The result contains the executable, runtime libraries, and packaged game data; distribute the complete output directory together. Users do not need an engine checkout, CMake, or a compiler toolchain.

This is a native-host exporter: Windows builds Windows. Installing it on Linux does not add Windows cross-compilation.

## Repository guide

The installable plugin lives in `package/`. `package.py`, `release.py`, tests, CI, documentation sources, and native build configuration are maintainer tooling and are not included in the `.inxpkg`.

```text
package/
  inx_package.json
  editor/infernux_windows/
  plugin_pages/
```

Maintainers build the engine's `windows-msvc-player` preset, which writes the Player directly into this repository. To validate an existing payload locally:

```powershell
python package.py dist/infernux.platform-windows.inxpkg
python release.py v0.2.0
```

Pushing a matching `v<version>` tag makes GitHub Actions build and publish the `.inxpkg` and its release manifest.

## License

[MIT](LICENSE). Bundled third-party components retain their own licenses.
