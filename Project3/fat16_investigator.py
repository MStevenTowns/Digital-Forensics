import struct

#https://www.win.tue.nl/~aeb/linux/fs/fat/fat-1.html
 
f = open("Image.img", "rb")
print("1. Boot block bytes")
print("512")

print("\n2. Bytes per sector")
f.seek(11)
bytesPerSector=struct.unpack("<H",f.read(2))[0] #512
print(bytesPerSector)

print("\n3. Sectors per cluster")
sectorsPerCluster=struct.unpack("<B",f.read(1))[0] #8
print(sectorsPerCluster)

print("\n4. Reserved sectors")
reservedSectors=struct.unpack("<H",f.read(2))[0] #8
print(reservedSectors)

print("\n5. how many File Allocation Tables?") 
FATTables=struct.unpack("<B",f.read(1))[0] #2
print(FATTables)

print("\n6. Root Directory Entries") 
rootDirectoryEntries=struct.unpack("<H",f.read(2))[0] #512
print(rootDirectoryEntries)

sectors=struct.unpack("<H",f.read(2))[0]

f.seek(22)
print("\n7. Sectors per File Allocation Table") 
sectorsPerFAT=struct.unpack("<H",f.read(2))[0] #8
print(sectorsPerFAT)

print("\n8. Byte offset of first File Allocation Table")
firstStart=reservedSectors*bytesPerSector+512

print("\n9. Byte offset of second FAT table")
secondStart=firstStart+sectorsPerFAT*bytesPerSector
print(secondStart)

print("\n10. Byte offset of first Root Directory entry")
firstRoot=secondStart+sectorsPerFAT*bytesPerSector
print(firstRoot)

print("\n11. Byte offset of first Data Block")


print("\n12. How much User data(bytes) can disk partition hold?")
