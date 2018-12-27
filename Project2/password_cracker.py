'''
Michael Steven Towns

Requires python 2.7
'''

import string
import hashlib

a=b=c=False
for char1 in string.ascii_lowercase:
    for char2 in string.ascii_lowercase:
        for char3 in string.ascii_lowercase:
            for char4 in string.ascii_lowercase:
                for char5 in string.ascii_lowercase:
                    h=char1+char2+char3+char4+char5
                    if hashlib.md5(h).hexdigest() =="9aeaed51f2b0f6680c4ed4b07fb1a83c":
                        print("Jkirk.zip: "+h)
                        a=True
                    elif hashlib.md5(h).hexdigest() == "172346606e1d24062e891d537e917a90":
                        print("Lmccoy.zip: "+h)
                        b=True
                    elif hashlib.md5(h).hexdigest() == "fa5caf54a500bad246188a8769cb9947":
                        print("Cchapel.zip: "+h)
                        c=True
                    if a and b and c:
                        exit()

'''
Jkirk.zip - troll
9aeaed51f2b0f6680c4ed4b07fb1a83c
Lmccoy.zip - lolol
172346606e1d24062e891d537e917a90
Cchapel.zip - polar
fa5caf54a500bad246188a8769cb9947
'''
