# AsciiArt

## Some Amazing examples
[1. A Beautiful Girl drawed by me](http://zhoudaxia.eu/AsciiArt/examples/test1.html)  
[2. Famous Yaoming's Face](http://zhoudaxia.eu/AsciiArt/examples/yaoming.html)  
[3. My Avatar](http://zhoudaxia.eu/AsciiArt/examples/avatar.html)

---
## To do list
- [x] Asciify an image into `txt` & `html`
- [ ] Asciify many images parallelly
- [ ] Asciify a GIF
- [ ] Asciify a video

---
## Requirements
1. `Python3`
2. `Pillow-5.1.0` (Only this version has been tested, other versions may also work)

---

## Usage
```
./main.py avatar.png
```
You can use `--scaling_ratio` to specify the scaling ratio of the output with respect to the input image. The default value is `0.5`.  
```
./main.py avatar.png --scaling_ratio 0.1
```

You can use `--output_format` to specify the format of the output file.  
>`0` represents for `.txt` format  
`1` represents for `.html` format  
`2` represents for both `.txt` format & `.html` format

The default value is `2`.
```
./main.py avatar.png --output_format 1
```

You can use `--line_height` to specify the height of each line of ascii characters in the output file. The default value is `0.65`.
```
./main.py avatar.png --line_height 0.65
```

You can use `--font_size` to specify the font size of ascii characters in the output file. The default value is `5`.
```
./main.py avatar.png --font_size 8
```
