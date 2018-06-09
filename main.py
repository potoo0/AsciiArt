#! /usr/bin/env python3
# coding: utf-8
from PIL import Image

class AsciiArt():
    def __init__(self, img_path):
        self.path = img_path
        self.gray_scale = r'@%#*+=-:. '    # r' .:-=+*#%@'
        self.size = ()
    
    def select_ascii_char(self, pixel):
        unit = 256 / len(self.gray_scale)
        return self.gray_scale[int(pixel/unit)]

    def convert_to_ascii(self, scaling_ratio):
        img = Image.open(self.path).convert('L')
        width, height = img.size
        img = img.resize((int(width*scaling_ratio), int(height*scaling_ratio)), Image.LANCZOS)    # Image.NEAREST Image.BILINEAR Image.BICUBIC Image.LANCZOS
        self.size = width_new, height_new = img.size
        ascii = ''
        for row in range(height_new):
            for col in range(width_new):
                pixel = img.getpixel((col, row))
                ascii += self.select_ascii_char(pixel)
            ascii += '\n'
        return ascii
    
    def save_as_txt_file(self, scaling_ratio=0.5):
        ascii = self.convert_to_ascii(scaling_ratio)
        with open('imgtoascii.txt', 'w') as f:
            f.write(ascii)
    
    def save_as_html_file(self, scaling_ratio=0.5):
        ascii = self.convert_to_ascii(scaling_ratio)
        html = '''<!DOCTYPE HTML>
                <html>
                <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                <style type="text/css">
                    pre {
                    word-wrap: break-word;      /* IE 5.5-7 */
                    white-space: -moz-pre-wrap; /* Firefox 1.0-2.0 */
                    white-space: pre-wrap;      /* Modern browsers */
                    font-family: 'Courier New', 'Monaco', 'Consolas', 'Inconsolata';
                    line-height: 1.0;
                    font-size: %dpx;
                    }
                </style>
                </head>
                <body>
                <pre>%s</pre>
                </body>
                </html>
                '''
        html = html % (6, ascii)
        with open('imgtoascii.html', 'w') as f:
            f.write(html)



if __name__ == '__main__':
    AsciiArt('avatar.png').save_as_txt_file(0.1)
    AsciiArt('avatar.png').save_as_html_file(0.1)