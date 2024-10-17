# TimeLapseToolkit: 图片到视频/GIF转换工具

[English](README.md) | 中文

这是一个图片处理工具集，专为批量处理图片、创建视频和GIF而设计。非常适合处理延时摄影的结果，也可用于其他需要批量处理图片的场景。

## 示例输出

### 示例GIF
![示例GIF](output/output-ffmpeg.gif)

### 示例视频
[点击此处查看示例视频](output/output_video.mp4)

## 主要功能

1. 批量压缩图片
2. 将图片序列转换为视频
3. 将图片序列转换为GIF

## 环境设置

1. 确保您的系统已安装Python 3.6或更高版本。

2. Windows用户注意：本项目的脚本需要在类似Git Bash的环境中运行。如果您还没有安装Git Bash，请从[官方网站](https://git-scm.com/download/win)下载并安装。

3. 克隆仓库

4. 运行初始化脚本：
   - Windows (在Git Bash中): `./init_project.sh`
   - Mac/Linux: `bash init_project.sh`

5. 激活虚拟环境：
   - Windows (在Git Bash中): `source venv/Scripts/activate`
   - Mac/Linux: `source venv/bin/activate`

6. 安装FFmpeg（如果尚未安装）：
   - 运行 `bash install_ffmpeg.sh`

7. 如果在Windows上遇到编解码器问题：
   - 运行 `bash install_openh264.sh`

## 使用说明

### 1. 压缩图片

运行命令：`python compress_images.py`

按提示输入以下信息：
- 源图片文件夹路径（默认：'input_images'）
- 压缩后图片保存路径（默认：'input_images_zipped'）
- 压缩质量（1-100，默认：85）
- 是否使用无损压缩（y/n，默认：n）
- 是否调整图片大小（输入缩放因子，如0.5表示缩小一半，2表示放大一倍）

### 2. 创建视频

运行命令：`python create_video_from_images.py`

按提示输入以下信息：
- 输入文件夹（包含PNG图片）
- 输出文件夹
- 输出视频文件名
- 每张图片的帧数
- 视频帧率
- 选择编解码器（avc1, mp4v, X264, H264）

### 3. 创建GIF

运行命令：`python create_gif_from_images.py`

按提示输入以下信息：
- 输入文件夹（包含图片）
- 输出文件夹
- 输出GIF文件名
- 输出尺寸百分比（1-100）
- GIF帧率
- 压缩级别（1-3）
- 选择创建方法（1: ffmpeg, 2: imageio）

## 注意事项

- 确保输入文件夹中的图片尺寸一致。
- 对于视频和GIF创建，建议使用PNG格式的图片以获得最佳质量。
- 如果遇到性能问题，可以尝试调整压缩级别或输出尺寸。
- Windows用户请确保在Git Bash或类似的Unix-like环境中运行所有脚本。

## 故障排除

- 如果遇到"FFmpeg not found"错误，请确保已正确安装FFmpeg并添加到系统PATH中。
- 对于Windows用户，如果遇到编解码器问题，尝试运行`install_openh264.sh`脚本。
- 如果在Windows上运行脚本时遇到问题，请确保您使用的是Git Bash或类似的环境，而不是普通的命令提示符或PowerShell。

如果您在使用过程中遇到任何问题，欢迎提出issue或联系我们寻求帮助。
