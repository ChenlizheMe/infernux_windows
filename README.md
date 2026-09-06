# Infernux Windows Platform

[简体中文](README.zh-CN.md) · [Releases](https://github.com/ChenlizheMe/infernux_windows/releases) · [Infernux](https://github.com/ChenlizheMe/Infernux)

![Windows build workflow](package/plugin_pages/media/overview.png)

Build Windows x64 Players using the native runtime shipped with the Windows engine wheel. This package registers the Windows exporter; it does not contain a second copy of the engine or an entire compiler SDK.

## At a glance

| Item | Value |
| --- | --- |
| Package | `infernux/platform-windows` |
| Plugin version | 0.1.0 |
| Engine compatibility | >=0.4.0,<0.5 |
| Target | `windows-x64` |
| Build host | Windows x64 |
| Rendering | Native Player / Vulkan |

## Install

1. Open your project in Infernux 0.4.0 and open the Plugins panel.
2. Select Infernux Windows Platform in the official list, then import and enable it.
3. Open the build settings and select the target. Resolve the reported prerequisites before exporting.

If your editor's bundled catalog predates this repository, add `https://github.com/ChenlizheMe/infernux_windows` as a GitHub plugin source, or import `infernux.platform-windows.inxpkg` from [Releases](https://github.com/ChenlizheMe/infernux_windows/releases/latest). GitHub's automatic source ZIP is the author repository, not the installable plugin artifact.

## Requirements

A Windows x64 installation of Infernux 0.4.0 with its native Player and Python 3.13 runtime pack. The resulting Player uses Vulkan.

## Host boundary

This is a native-host exporter: Windows builds Windows. Installing this package on Linux does not enable Windows cross-compilation. Disabling or uninstalling it removes its build target.

## Output and troubleshooting

Export a game directory containing its executable, runtime dependencies and packaged game data. Keep the complete output together when distributing it. Project content is cooked into the engine's binary package, not published as the editable Assets/Library tree. Packaging is not DRM.

If the target is absent, check that the package is enabled and the editor is Windows x64. If the build reports missing native Player or Python runtime files, repair the engine installation; reinstalling this small plugin cannot replace those files.

## Develop and package

Only `package/` becomes the InxPackage payload. The outer README, SVG illustration sources, release automation and build scripts remain repository files. In-editor documentation is separate, under `package/plugin_pages/`.

```text
package/
  inx_package.json
  editor/infernux_windows/
  plugin_pages/
package.py
release.py
README.md
README.zh-CN.md
```

Run `python package.py dist/infernux.platform-windows.inxpkg` to package locally. This standalone script uses only Python's standard library and does not require an engine installation. Build outside package/, then place the files to ship inside package/ before packaging.

Maintainers run `python release.py v0.1.0` to create the archive and its release manifest. Pushing a matching version tag publishes both files through GitHub Actions. The editor uses that manifest to select a compatible release.

## License

[MIT](LICENSE). Third-party SDKs and the engine runtime keep their own licenses; they are not relicensed by this plugin.
