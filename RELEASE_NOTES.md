# Infernux Windows Platform 0.2.0

Official platform package for Infernux ==0.4.0.

- Ships the CMake-precompiled native Player, CPython runtime and optional parallel module in the plugin.
- Removes source checkout, CMake and engine compilation from ordinary game export.
- Registers windows-x64 and its platform build integration.
- Includes English and Simplified Chinese documentation with a build workflow illustration.
- Ships an installable InxPackage and the engine's compatible-release manifest.

## Requirements

Infernux 0.4.0 for Windows x64 with Python 3.13. This plugin owns the matching precompiled Player payload. The resulting Player uses Vulkan.

Download the .inxpkg asset to install the plugin. The automatic source archives are for plugin development. See the README for setup, output and troubleshooting details.
