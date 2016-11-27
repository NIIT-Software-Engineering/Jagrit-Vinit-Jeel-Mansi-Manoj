from tesserocr import PyTessBaseAPI
import sys
import os

first_arg = sys.argv[1]

indir = first_arg
images = []
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        images.append(f)
images.sort()
#print images

#images = ['1.jpg', '2.jpg', '3.png', '4.png', '5.jpg']
#images = ['1.jpg']
f= open(indir + ".txt","a+")


with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(indir + '/' + img)
        output = api.GetUTF8Text()
        if isinstance(output, unicode):
            converted = output.encode('UTF-8')
        #print type(converted)
        f.write(converted)
        #print api.AllWordConfidences()

f.close()
