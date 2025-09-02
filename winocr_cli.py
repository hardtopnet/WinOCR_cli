import argparse
import asyncio
import os
import winocr
from PIL import Image

async def main():
    parser = argparse.ArgumentParser(description="Windows OCR command-line tool with line breaks")
    parser.add_argument("-i", "--input", required=True, help="Input image file")
    parser.add_argument("-o", "--output", required=True, help="Output text file")
    parser.add_argument("-l", "--lang", default="fr", help="OCR language (default: en)")

    args = parser.parse_args()

    # only delete the output file if it is a text file.
    text_files = {".txt", ".md", ".csv", ".json", ".xml", ".html"}  
    if os.path.exists(args.output) and os.path.splitext(args.output)[1].lower() in text_files:
        os.remove(args.output)

    img = Image.open(args.input)
    result = (await winocr.recognize_pil(img, args.lang))
    output = "\n".join([line.text for line in result.lines])

    if os.path.exists(args.output):
        print(f"Error: the output file '{args.output}' already exists.")
        return

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    asyncio.run(main())
