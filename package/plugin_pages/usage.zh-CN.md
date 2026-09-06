# Windows 平台

![构建流程](media/overview.png)

使用 Windows 引擎 wheel 中的原生运行时构建 Windows x64 Player。插件负责注册 Windows 导出器，不重复携带引擎本体或完整编译工具链。

## 构建前准备

Windows x64 的 Infernux 0.4.0，包含原生 Player 和 Python 3.13 运行时包。导出的 Player 使用 Vulkan。

## 宿主边界

这是原生宿主导出器：Windows 构建 Windows。在 Linux 上安装此包不会获得 Windows 交叉编译能力。禁用或卸载插件会移除对应构建目标。

## 输出与排错

输出目录包含游戏可执行文件、运行依赖和打包后的游戏数据，分发时须保留完整目录。项目内容经过 cook 进入引擎二进制包，不以可编辑的 Assets/Library 目录树发布；二进制打包不等于 DRM。

目标未出现时，检查插件是否启用，以及编辑器是否为 Windows x64。若提示原生 Player 或 Python 运行时缺失，应修复引擎安装；重新安装这个小型插件不能补齐引擎运行时。
