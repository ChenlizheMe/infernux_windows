# Infernux Windows 平台插件

这是 [Infernux](https://github.com/ChenlizheMe/Infernux) 游戏引擎的官方 Windows 构建插件。安装后，编辑器就能把项目导出为原生 Windows x64 游戏；Player 和 Python 运行时已经随插件准备好，普通用户不需要下载引擎源码，也不需要自己运行 CMake。

[English](README.md) · [Infernux 引擎](https://github.com/ChenlizheMe/Infernux) · [插件模板](https://github.com/ChenlizheMe/infernux_plugin_template) · [发布制品](https://github.com/ChenlizheMe/infernux_windows/releases)

![Infernux Windows 导出流程](package/plugin_pages/media/overview.png)

## 插件提供什么

- 编辑器中的 `windows-x64` 构建目标
- 预编译的原生 Player、CPython 3.13 运行时和并行模块
- Vulkan 渲染与 Windows 导出流程
- 二进制游戏内容包，不直接暴露可编辑的 `Assets`、`Library` 目录

| 包标识 | 版本 | 适配引擎 | 构建环境 | 目标平台 |
| --- | --- | --- | --- | --- |
| `infernux/platform-windows` | 0.2.0 | Infernux 0.4.0 | Windows x64 | Windows x64 |

## 安装与导出

在 Infernux 中打开**插件**窗口，从官方列表选择 **Infernux Windows Platform**，导入并启用即可。官方安装会优先使用 Infernux 分发服务；该渠道不可用时，编辑器会改用 GitHub Releases。也可以从本仓库的 Releases 页面下载 `infernux.platform-windows.inxpkg` 手动导入。

随后在构建设置中选择 `windows-x64` 并导出。生成目录包含游戏程序、运行库和打包后的项目内容，发布时请保持整个目录完整。该插件只负责 Windows 原生构建，不提供从 Linux 交叉构建 Windows 的能力。

## 仓库说明

真正进入插件包的内容都在 `package/` 中。根目录的打包脚本、测试、CI、文档源文件和原生构建配置只服务于开发与发布，不会进入 `.inxpkg`。

```text
package/
  inx_package.json
  editor/infernux_windows/
  plugin_pages/
```

维护者通过引擎的 `windows-msvc-player` preset 直接把 Player 产出到本仓库。已有载荷可用下面的命令校验和生成发布文件：

```powershell
python package.py dist/infernux.platform-windows.inxpkg
python release.py v0.2.0
```

推送与插件版本一致的 `v<version>` 标签后，GitHub Actions 会自动发布 `.inxpkg` 和对应的 release manifest。

## 许可证

[MIT](LICENSE)。随包提供的第三方组件继续遵守各自的许可证。
