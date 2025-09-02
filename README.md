# WinOCR CLI

WinOCR CLI is a command-line tool for performing Optical Character Recognition (OCR) on images in Windows environments.
This project uses the [winocr library](https://github.com/GitHub30/winocr)

## Features

- Extract text from images
- Supports multiple languages
- Simple command-line interface

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/WinOCR_cli.git
    ```
2. Navigate to the project directory:
    ```bash
    cd WinOCR_cli
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python winocr_cli.py --input path/to/image --output result.txt
```

### Options

| Option         | Description                       |
| -------------- | --------------------------------- |
| `--input`      | Path to input image               |
| `--output`     | Path to save extracted text       |
| `--lang`       | Language code (default: eng)      |

## Example

```bash
python winocr_cli.py --input sample.png --output output.txt --lang en
```

## Building Windows binary

To build a standalone Windows executable, use the following Windows command-line instruction in the project root:

```cmd
pyinstaller --onefile winocr_cli.py
```
