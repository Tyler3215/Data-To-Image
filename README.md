# Data-To-Video
A script that encodes text itself or text from a file into an image. The application, of course, also decodes from an image to just text or a text file. This script offers a simple yet effective way to encode textual data into images for various purposes like data hiding, transmission, or encryption.
- This Python script only supports characters from the ascii table.
## Features:
1. Encoding Functions:
   - `Text-to-Image Encoding:` Converts text data into images by mapping characters to grayscale values and storing them as pixels in an image file.
   - `File Encoding:` Reads text from a file and encodes it into images.
3. Decoding Functions:
   - `Image-to-Text Decoding:` Retrieves text data from encoded images.
   - `Decoding to File:` Writes decoded text data to a new text file.
## Usage:
- You can simply use a dedicated menu `menu.py`.  
- You can call the methods yourself `main.py`. The script provides two classes:
   - `Encoder:` Handles the encoding of text data into images. Methods:
     - `EncodeFile:` Encodes text from a file.
     - `EncodeString:` Encodes a provided string.
     - `SetResolution:` Sets the resolution for the output images.
   - `Decoder:` Handles the decoding of images back into text.
     - `DecodeToFile:` Decodes images and writes the text to a file.
     - `DecodeToString:` Decodes images and returns the text as a string.
## Example of how it works:
https://github.com/Tyler3215/Data-To-Image/assets/144626638/818b4f86-8614-4afc-9c72-93cf246d54af
## Requirements:
- Python 3.x
- PIL (Python Imaging Library)
## How to install and run on linux:  
```
pip3 install -r requirements.txt
python3 menu.py
```

## How to install and run on Windows:  
```
py -m pip install -r requirements.txt
py menu.py
```
