# Infernux Windows 平台插件

[English](README.md) · [发布制品](https://github.com/ChenlizheMe/infernux_windows/releases) · [Infernux](https://github.com/ChenlizheMe/Infernux)

![Windows 构建流程](package/plugin_pages/media/overview.png)

使用 Windows 引擎 wheel 中的原生运行时构建 Windows x64 Player。插件负责注册 Windows 导出器，不重复携带引擎本体或完整编译工具链。

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 包标识 | `infernux/platform-windows` |
| 插件版本 | 0.1.0 |
| 引擎兼容范围 | >=0.4.0,<0.5 |
| 构建目标 | `windows-x64` |
| 构建宿主 | Windows x64 |

## 安装

1. 在 Infernux 0.4.0 中打开项目，进入插件面板。
2. 在官方列表选择 Infernux Windows Platform，导入并启用。
3. 打开构建设置，选择目标，按诊断补齐依赖后导出。

如果编辑器仍使用旧版内置目录，可以手动添加 GitHub 源 `https://github.com/ChenlizheMe/infernux_windows`，或从 [Releases](https://github.com/ChenlizheMe/infernux_windows/releases/latest) 下载 `infernux.platform-windows.inxpkg` 后导入。GitHub 自动生成的源码 ZIP 是作者仓库，不是插件安装制品。

## 环境要求

Windows x64 的 Infernux 0.4.0，包含原生 Player 和 Python 3.13 运行时包。导出的 Player 使用 Vulkan。

## 宿主边界

这是原生宿主导出器：Windows 构建 Windows。在 Linux 上安装此包不会获得 Windows 交叉编译能力。禁用或卸载插件会移除对应构建目标。

## 输出与排错

输出目录包含游戏可执行文件、运行依赖和打包后的游戏数据，分发时须保留完整目录。项目内容经过 cook 进入引擎二进制包，不以可编辑的 Assets/Library 目录树发布；二进制打包不等于 DRM。

目标未出现时，检查插件是否启用，以及编辑器是否为 Windows x64。若提示原生 Player 或 Python 运行时缺失，应修复引擎安装；重新安装这个小型插件不能补齐引擎运行时。

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

维护者运行 `python release.py v0.1.0` 生成插件和发布清单；推送与插件版本一致的标签后，由 GitHub Actions 打包并上传两个文件。编辑器根据发布清单选择兼容版本。

## 许可证

[MIT](LICENSE)。第三方 SDK 和引擎运行时各自遵守原有许可证，不因本插件而改变。
