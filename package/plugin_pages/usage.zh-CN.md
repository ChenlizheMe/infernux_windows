# Windows 平台

![构建流程](media/overview.png)

插件携带预编译 Windows Player、CPython 运行时和可选并行模块。普通导出只组装这些文件和项目 cook 内容，不需要引擎源码、CMake 或编译工具链。

## 构建前准备

Windows x64 的 Infernux 0.4.0（Python 3.13）。对应的预编译 Player 载荷由本插件提供。导出的 Player 使用 Vulkan。

## 宿主边界

这是原生宿主导出器：Windows 构建 Windows。在 Linux 上安装此包不会获得 Windows 交叉编译能力。禁用或卸载插件会移除对应构建目标。

## 输出与排错

输出目录包含游戏可执行文件、运行依赖和打包后的游戏数据，分发时须保留完整目录。项目内容经过 cook 进入引擎二进制包，不以可编辑的 Assets/Library 目录树发布；二进制打包不等于 DRM。

目标未出现时，检查插件是否启用，以及编辑器是否为 Windows x64。若提示 Player 载荷缺失或不兼容，请通过插件的版本页显式安装兼容的完整平台制品。
