# README

## Project Overview
This project aims to perform denoising on multimodal data (including images, videos, and audio) by calculating the Signal-to-Noise Ratio (SNR). The specific process and implementation details are as follows:

## 1. Image Denoising
For image data, the project uses `Deep Image Prior` for denoising. The steps are as follows:

### 1.1 Configure Path
- Open the `Deep-image-prior/utils/test.py` file.
- Modify the second line of the code:
  ```python
  fname = 'path to test image'
  ```
  Replace `'path to test image'` with the actual path to the image to be tested.

### 1.2 Run Denoising
- After running the code, the denoised image will be saved in the `../output_images` folder.
- The SNR curve during the denoising process will be saved in `../snr_curve.png`.
- The final SNR value will be printed to the console.

## 2. Video Denoising
For video data, the project denoises by extracting video sequences as images. The steps are as follows:

### 2.1 Extract Video Sequence
- Open the `Fastdvdnet-master/video_to_images.py` file.
- Modify the video file path to the video you wish to process:
  ```python
  path to video
  ```
- After running the code, the video will be converted to an image sequence and saved in the specified path `path to image_sequence`.

### 2.2 Denoise
- Open the `Fastdvdnet-master/` directory and the `test.py` file.
- Modify the `parser.add_argument("--test_path", type=str, default="image_sequence", help='path to sequence to denoise')` line to the path of the extracted image sequence.
- After running the denoising program, the denoised image sequence will be saved in the `../results` folder, and the SNR values will be written to the `../results/log.txt` file.

## 3. Audio Denoising
For audio data, this project provides two denoising methods depending on your computational resources:

### 3.1 Strong Local Computing Power
If your local computing power is strong enough, use the following method for audio denoising:
- Open the `Dual-Path-RNN-Pytorch-master/dualrnn_test_wav.py` file.
- Modify the `parser.add_argument('-mix_scp', type=str, default='sample-9s.wav', help='Path to mix scp file.')` line to your own audio file path.
- After running the code, the denoised audio will be saved in the `./test` folder.

### 3.2 Weak Local Computing Power
If your local computing power is weaker, you can use the following method:
- Run `resemble-enhance-main/app.py` and drag and drop the audio file to upload.
- Download the denoised file from the website.

After obtaining the denoised audio using either method, open the `SI-SNR_to_SNR.py` file. Modify the paths in the file, replacing the original and denoised audio addresses:
  ```python
  x_signal, sr = load_wav('original_path')  # Noisy signal
  s_signal, sr = load_wav('denoised_path')  # Clean signal as the reference signal
  ```
  Replace `'original_path'` and `'denoised_path'` with the actual paths to the original and denoised audio files. 

After running the code, the SNR value will be printed.

## 项目概述

本项目旨在通过计算信噪比（SNR）对多模态数据（包括图片、视频和音频）进行降噪。具体的流程和实现细节如下：

## 1. 图片数据降噪

对于图片数据，项目利用`Deep Image Prior`进行降噪。步骤如下：

### 1.1 配置路径
- 打开 `Deep-image-prior/utils/test.py` 文件。
- 修改第二行代码：
  ```python
  fname = 'path to test image'
  ```
  将 `'path to test image'` 替换为待测图片的实际路径。

### 1.2 运行降噪
- 运行代码后，降噪后的图片将保存在 `../output_images` 文件夹中。
- 降噪过程中，SNR的变化曲线会保存在 `../snr_curve.png`。
- 最终的SNR数值将打印在输出台。

## 2. 视频数据降噪

对于视频数据，项目通过将视频序列提取为图像进行降噪。步骤如下：

### 2.1 提取视频序列
- 打开 `Fastdvdnet-master/video_to_images.py` 文件。
- 修改视频文件路径为待处理视频：
  ```python
  path to video
  ```
- 运行代码后，视频将被转换为图像序列，保存在指定路径 `path to image_sequence`。

### 2.2 进行降噪
- 打开 `Fastdvdnet-master/` 目录下的 `test.py` 文件。
- 修改 `parser.add_argument("--test_path", type=str, default="image_sequence", help='path to sequence to denoise')` 中的路径为提取的图片序列路径。
- 运行降噪程序后，降噪后的图像序列将保存在 `../results` 文件夹中，SNR数值将写入 `../results/log.txt` 文件。

## 3. 音频数据降噪

对于音频数据，本项目提供两种降噪方式，具体选择取决于你的计算资源：

### 3.1 本地计算能力较强
如果你的本地计算能力足够强，使用以下方式进行音频降噪：
- 打开 `Dual-Path-RNN-Pytorch-master/dualrnn_test_wav.py` 文件。
- 修改 `parser.add_argument('-mix_scp', type=str, default='sample-9s.wav', help='Path to mix scp file.')` 中的路径为你自己的音频文件路径。
- 运行代码后，降噪后的音频将保存在 `./test` 文件夹中。

### 3.2 本地计算能力较弱
如果你的本地计算能力较弱，可以使用以下方式：
- 运行 `resemble-enhance-main/app.py`，通过拖拽上传待处理音频文件。
- 在网站上下载降噪后的文件。

无论你选择哪种方法得到降噪后的音频后，打开 `SI-SNR_to_SNR.py` 文件。
修改文件中的路径，替换原始音频和降噪音频的地址：
  ```python
  x_signal, sr = load_wav('original_path')  # Noisy signal
  s_signal, sr = load_wav('denoised_path')  # Clean signal as the reference signal
  ```
  将 `'original_path'` 和 `'denoised_path'` 替换为原始音频和降噪音频的实际路径。
  运行代码后，SNR数值将被打印出来。

