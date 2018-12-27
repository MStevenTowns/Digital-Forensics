'''
Michael Steven Towns

Requires python 2.7 and Python Image Library(PIL)
PIL webpage: http://pythonware.com/products/pil/

Requires the desired image to be in the same folder as this program
to find the copyright run the program without modifications
to find the hidden message, comment the for "copyright lines" and uncomment the "for hidden message" lines

both require the file to be named as specified in the Image.open() lines
'''

from PIL import Image
import binascii

img=Image.open("DCIM_2837.png") #for copyright

#img=Image.open("mountain (copy).png") #for hidden message

pix = img.load()
w,h = img.size
string='0b'
for y in range(h):
    for x in range(w):
        r,g,b = pix[x,y]
        string+=str(g%2) #for copyright
        #string+=str(r%2) #for hidden message
n=int(string,2)
print(binascii.unhexlify('%x' % n))
