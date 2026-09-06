# Windows Platform

![Build workflow](media/overview.png)

Build Windows x64 Players using the precompiled Player, CPython runtime and optional parallel module shipped in this plugin. Ordinary exports assemble these files with cooked project content; no engine checkout, CMake, or compiler SDK is required.

## Before building

Infernux 0.4.0 for Windows x64 with Python 3.13. This plugin owns the matching precompiled Player payload. The resulting Player uses Vulkan.

## Host boundary

This is a native-host exporter: Windows builds Windows. Installing this package on Linux does not enable Windows cross-compilation. Disabling or uninstalling it removes its build target.

## Output and troubleshooting

Export a game directory containing its executable, runtime dependencies and packaged game data. Keep the complete output together when distributing it. Project content is cooked into the engine's binary package, not published as the editable Assets/Library tree. Packaging is not DRM.

If the target is absent, check that the package is enabled and the editor is Windows x64. If the build reports missing or incompatible Player files, explicitly install a compatible complete platform release through the plugin's Versions tab.
