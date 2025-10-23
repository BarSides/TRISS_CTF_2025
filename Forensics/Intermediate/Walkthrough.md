# Overview

> ## Really Subtle
> **Description**\
> There's something different about these two files, but I can't quite put my finger on it.\
Sometimes differences are as obvious as black and white -- other times they're just the littlest bit off.
>
> **Assets**\
> mod.png\
> orig.png

# Walkthrough

When viewing the two images, there is no obvious visible difference. The mod.png file is larger than orig.png by about 5 Kb, so we're going to check for hidden data:
```bash
binwalk mod.png   

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 150 x 150, 8-bit/color RGB, non-interlaced
2240          0x8C0           Zlib compressed data, default compression
21070         0x524E          Zip archive data, encrypted at least v2.0 to extract, compressed size: 1360, uncompressed size: 2360, name: flag.pdf
22544         0x5810          End of Zip archive, footer length: 22

```
Binwalk shows there is an encrypted zip archive that contains a flag.pdf file.
That seems promising, but we'll need a password. We can extract the zip archive to 524E.zip for later using:
```bash
binwalk -e mod.png
```
Checking strings on on mod.png, we get a lot of data, including a suspicious string:
```VGhpcyBpc24ndCB0aGUgYmFzZSB5b3UncmUgbG9va2luZyBmb3I=```\
However...
```
echo "VGhpcyBpc24ndCB0aGUgYmFzZSB5b3UncmUgbG9va2luZyBmb3I=" | base64 -d
This isn't the base you're looking for  
```
Since many of the strings looked like EXIF data, we can try:
```
exiftool mod.png
```
Indeed, there is a lot of metadata in the image, but we do see this section near the end:
```
...
Security Level                  : Obscurity
Extra Compression               : Zip
Extra Encoding                  : Ascii85
Extra Access                    : F*1;8;I=K$@ra@a?ViS*H?V&@A2,hq1c5
...
```
Ascii85 is another encoding scheme also known as Base85. This may be the base we're looking for!\
We can put the value of ```Extra Access``` into [CyberChef](https://gchq.github.io/CyberChef/) using the "From Base85" operation to get\
```suP3R_s3cr37_P4zzw0Rd12345```

Trying 7zip extraction with that password is successful
```
7za x -psuP3R_s3cr37_P4zzw0Rd12345 524E.zip                                                                     

...

Everything is Ok

Size:       2360
Compressed: 1496
```

We open flag.pdf expecting to find the flag, but instead find another password request

![password required](images/pwd_req.png)

The flag.pdf file seems to be just a pdf file, and there doesn't look to be any extra information hidden in it.

Before extracting and trying to crack the hash, let's go back to the description for any clues.\
The phrase _"the littlest bit"_ may hint at Least Significant Bit (LSB) Steganography. 

We can use [StegOnline](https://georgeom.net/StegOnline/upload) to check LSB Data, but we will need to separate the image in mod.png from the attached zip archive since it causes problems on the site. 

We can separate the png image out by using ```dd``` with the offset of the zip archive we learned from ```binwalk``` earlier.
```
dd if=mod.png of=split.png bs=1 count=21070
```
When we upload split.png and choose "LSB Half", we see what looks like a QR Code in the background behind the logo.

![lsb half](images/lsb_half.png)

Not exactly LSB Steganography, but we are a step closer.

Since we haven't used the orig.png file yet, we think to try using that image to cancel out the logo from in front of the QR Code. We load both images into GIMP, and place the modified image in a layer above the original. Next, we change the blend modes on the top layer to see if any of them result in something useful. 

The "Grain extract" mode looks like it could work

![grain extract](images/grain_extract.png)

We'll have to make the shades stand out a little more, which we can do by using "Colors > Map > Color Exchange".\
We start by setting the background, the color at the edges, to white.

![color exchange](images/color_exchange.png)

At this point, we can either scan the code with a phone app, or save and upload the image to a site like [ScanQR](https://scanqr.org/) to find\
```Th1s1sT00L0ngT0Typ3F0rAS1mpl3PDF```

Using that password to open the pdf, we find a single sentence near the top of an otherwise blank page:\
**AI can see the flag, can you?**

Thinking about how AI could see something that we couldn't, we are reminded about prompt injection techniques in malicious emails... we key ```Ctl+a``` to select all and find the flag hidden in white text on a white background.
```
BarSides{hum4n_1ntu1t10n_ftw}
``` 

### _Alternate method for QR code extraction_
If GIMP is not available, the differences between orig.png and mod.png can be extracted as an image using python.
```python
from PIL import Image

# Load each image
img1 = Image.open('orig.png').convert("RGB")
img2 = Image.open('mod.png').convert("RGB")

# Get the width and height
width, height = img1.size

# Create a same size image with a white background to hold the qr code
qr = Image.new("RGB", (width, height), (255, 255, 255))
qr_pixels = qr.load()

# Loop through the image dimensions
# Set the qr pixel to black if the source images are different
for x in range(width):
    for y in range(height):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))

        if pixel1 != pixel2:
            qr_pixels[x, y] = (0, 0, 0)

qr.save('extracted_qr.png')
```
![extracted qr](images/extracted_qr.png)