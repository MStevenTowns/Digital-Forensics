import base64

#outFile=file("out.txt","w")
inFile=file("corrupted.docx")
file1=file("f1.jpeg","w")
file2=file("f2.pdf","w")
file3=file("f3.gif","w")
file4=file("f4.png","w")
file5=file("f5.docx","w")


decoded=base64.b64decode(inFile.read())

#outFile.write(decoded)

f2Start=decoded.find("%PDF")
f2End=decoded.find("EOF")+3
f3Start=decoded.find("GIF8")
f3End=decoded.find("PNG")-16
f4Start=decoded.find("PNG")-1
f4End=decoded.find("IEND")+8
f5Start=decoded.find("PK")



file1.write(decoded[14:f2Start-11])
file2.write(decoded[f2Start:f2End+1])
file3.write(decoded[f3Start:f3End])
file4.write(decoded[f4Start:f4End])
file5.write(decoded[f5Start:-45])

#outFile.close()
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()




'''
File 1: c3a04e65e43b4a862b010927fae9aab1 - JPEG
	start: ff d8 ff
	end: ff d9
File 2: 3b2f3b12ee4b04d4d0384adeee21e4d4 - PDF
	start: %PDF
    end: EOF
File 3: 06d08f17d7b2efbc0dc0d303398196d0 - GIF
	GIF87a or GIF89a
File 4: aec49002f8b02c2099152df1ec18b6c1 - PNG
	start: 89 50 4e 47 0d 0a 1a 0a
    end: 73 69 78 68
File 5: - DOCX
    start: PK
'''
