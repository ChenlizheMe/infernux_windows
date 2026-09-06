# Infernux Windows 平台插件

[English](README.md) · [发布制品](https://github.com/ChenlizheMe/infernux_windows/releases) · [Infernux](https://github.com/ChenlizheMe/Infernux)

![Windows 构建流程](package/plugin_pages/media/overview.png)

插件携带预编译 Windows Player、CPython 运行时和可选并行模块。普通导出只组装这些文件和项目 cook 内容，不需要引擎源码、CMake 或编译工具链。

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 包标识 | `infernux/platform-windows` |
| 插件版本 | 0.2.0 |
| 引擎兼容范围 | ==0.4.0 |
| 构建目标 | `windows-x64` |
| 构建宿主 | Windows x64 |

## 安装

1. 在 Infernux 0.4.0 中打开项目，进入插件面板。
2. 在官方列表选择 Infernux Windows Platform，导入并启用。
3. 打开构建设置，选择目标，按诊断补齐依赖后导出。

如果编辑器仍使用旧版内置目录，可以手动添加 GitHub 源 `https://github.com/ChenlizheMe/infernux_windows`，或从 [Releases](https://github.com/ChenlizheMe/infernux_windows/releases/latest) 下载 `infernux.platform-windows.inxpkg` 后导入。GitHub 自动生成的源码 ZIP 是作者仓库，不是插件安装制品。

## 环境要求

Windows x64 的 Infernux 0.4.0（Python 3.13）。对应的预编译 Player 载荷由本插件提供。导出的 Player 使用 Vulkan。

## 宿主边界

这是原生宿主导出器：Windows 构建 Windows。在 Linux 上安装此包不会获得 Windows 交叉编译能力。禁用或卸载插件会移除对应构建目标。

## 输出与排错

输出目录包含游戏可执行文件、运行依赖和打包后的游戏数据，分发时须保留完整目录。项目内容经过 cook 进入引擎二进制包，不以可编辑的 Assets/Library 目录树发布；二进制打包不等于 DRM。

目标未出现时，检查插件是否启用，以及编辑器是否为 Windows x64。若提示 Player 载荷缺失或不兼容，请通过插件的版本页显式安装兼容的完整平台制品。

## 开发与打包

只有 `package/` 内的内容进入 InxPackage。外层 README、SVG 配图源文件、发布流程和构建脚本属于仓库，不进入插件。引擎内文档独立位于 `package/plugin_pages/`。

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

运行 `python package.py dist/infernux.platform-windows.inxpkg` 本地打包。脚本仅使用 Python 标准库，不需要导入或安装 Infernux。在外层进行构建，最后将需要交付的文件放进 package/ 即可。

维护者构建引擎的 `windows-msvc-player` CMake preset。它直接将载荷产出到本仓库的 `package/editor/infernux_windows/player/`，将最终 `.inxpkg` 和发布清单产出到 `dist/`。发布 CI 在 Windows 宿主上，用对应引擎发布线构建本插件的精确版本；不生成或传递中间运行时 ZIP，也没有独立压缩包中转渠道。

维护者运行 `python release.py v0.2.0` 生成插件和发布清单；推送与插件版本一致的标签后，由 GitHub Actions 打包并上传两个文件。编辑器根据发布清单选择兼容版本。

## 许可证

[MIT](LICENSE)。第三方 SDK 和引擎运行时各自遵守原有许可证，不因本插件而改变。
