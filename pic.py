#!/usr/bin/python3


from PIL import Image
import glob, os

size = 988, 988

for infile in glob.glob("*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    rgb_im = im.convert('RGB')
    rgb_im.save(file + ".JPEG")

filelist = glob.glob("*.png")
for f in filelist:
    os.remove(f)   


for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + ".JPEG", optimize=True)


filelist = glob.glob("*.jpg")
for f in filelist:
    os.remove(f)    


for infile in glob.glob("*.JPG"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + ".JPEG", optimize=True)


filelist = glob.glob("*.JPG")
for f in filelist:
    os.remove(f)





