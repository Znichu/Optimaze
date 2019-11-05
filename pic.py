#!/usr/bin/python3

from bs4 import BeautifulSoup
import mammoth
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




for infile in glob.glob("*.docx"):
    file, ext = os.path.splitext(infile)
    Docx = open(infile, 'rb')
    html = open("out.html", 'wb')
    document = mammoth.convert_to_html(Docx)
    html.write(document.value.encode('utf8'))
    Docx.close()
    html.close()

with open('out.html', 'r') as file:
    fcontent = file.read()

soup = BeautifulSoup(fcontent, 'html.parser')
tag = soup.p

for tag in soup.find_all('p'):
    tag_name = 'p'
    tag['style'] = 'ext-align: justify; text-indent: 20px;'
print ('Done!!!') 

with open('out.html', 'w') as fp:
    fp.write(soup.prettify())



