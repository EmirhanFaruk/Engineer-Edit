
# Modification date: Sun Mar 28 14:15:14 2021

# Production date: Sun Sep  3 15:43:43 2023

from PIL import Image
from clear_screen import clear


#ex 2)

img = Image.open("Engineer.png")


for i in range(184):
    for j in range(184):
        RVB = img.getpixel((i, j))
        R00 = (RVB[0], 0, 0)
        img.putpixel((i, j), R00)

img.save("EngiFEAR.png", "png")
print("EngiFEAR saved!")

#img.show()




#ex 3)


#Bleu

img = Image.open("Engineer.png")


for i in range(184):
    for j in range(184):
        RVB = img.getpixel((i, j))
        _00B = (0, 0, RVB[2])
        img.putpixel((i, j), _00B)

img.save("BLUEngie.png", "png")
print("BLUEngie saved!")

#img.show()

#Vert

img = Image.open("Engineer.png")


for i in range(184):
    for j in range(184):
        RVB = img.getpixel((i, j))
        _0V0 = (0, RVB[1], 0)
        img.putpixel((i, j), _0V0)

img.save("GREEngie.png", "png")
print("GREEngie saved!")

#img.show()



#Blanc et Noir

img = Image.open("Engineer.png")

for i in range(184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    if RVB[0] + RVB[1] + RVB[2] < 255:
      img.putpixel ((i, j) ,(255, 255, 255))
    else:
      img.putpixel ((i, j) ,(0, 0, 0))


img.save("WhiteBlackEngie.png","png")
print("WhiteBlackEngie saved!")


#img.show()


#Noir et Blanc

img = Image.open("Engineer.png")

for i in range(184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    if RVB[0] + RVB[1] + RVB[2] < 255:
      img.putpixel ((i, j) ,(0, 0, 0))
    else:
      img.putpixel ((i, j) ,(255, 255, 255))


img.save("BlackWhiteEngie.png","png")
print("BlackWhiteEngie saved!")


#img.show()



#rotation de 180 degré 

img = Image.open("Engineer.png")

img = img.rotate(180)

img.save("180degrEngie.png","png")
print("180degrEngie saved!")


#img.show()


#rotation de 90 degré 

img = Image.open("Engineer.png")

img = img.rotate(90)

img.save("90degrEngie.png","png")
print("90degrEngie saved!")


#img.show()


#Pixelisation

img = Image.open("Engineer.png")

imgS = img.resize((24, 24),resample=Image.BILINEAR)

img = imgS.resize(img.size,Image.NEAREST)

img.save("PixEngie.png","png")
print("PixEngie saved!")


#img.show()


#Combination de deux images

img = Image.open("Engineer.png")

image = Image.open("Ubered_Engineer.png")

for i in range(0, 184, 2):
    for j in range(0, 184, 2):
        imagepixel = image.getpixel((i, j))
        img.putpixel ((i, j), imagepixel)

for i in range(1, 183, 2):
    for j in range(1, 183, 2):
        imagepixel = image.getpixel((i, j))
        img.putpixel ((i, j), imagepixel)
        

img.save("RagEngie.png","png")
print("RagEngie saved!")


#img.show()




#Combination à l'aide d'un fond vert

img = Image.open("Engineer.png")

image = Image.open("UseMoreGun.png")

for i in range(184):
    for j in range(184):
        px = image.getpixel((i, j))
        if not(px[1] >= 252):
            img.putpixel ((i, j), px)


img.save("GiveMeTheMoney.png","png")
print("GiveMeTheMoney saved!")


#img.show()


#correction d'un image

img = Image.open("Photo.png")#256 * 256

for i in range(1, 254):
  for j in range(1, 254):
    l = []
    for m in range(i-1, i+2):
      for n in range(j-1, j+2):
        pl = img.getpixel((m, n))
        l.append(pl)
    l.sort()
    img.putpixel((i, j), (l[4]))

img.save("PPhoto.png","png")
print("PPhoto saved!")
    
#img.show()


#gri

img = Image.open("Engineer.png")

for i in range(184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    tone = int((RVB[0] + RVB[1] + RVB[2])/3)
    img.putpixel ((i, j) ,(tone, tone, tone))

img.save("GrayEngie.png","png")
print("GrayEngie saved!")


#img.show()


#EngiignE

img = Image.open("Engineer.png")

list = []

for i in range(92, 184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    l = [RVB]
    list.append(l)

temporary_list = []

m = 0
n = 92
for i in range(92):
    m = 1
    n -= 1
    for j in range(184):
        temporary_list.append(list[m + ((n * 184)-1)])
        m += 1
        


        
m = 0
for i in range(92):
    hash = m // 1000
    lines = 16 - hash
    clear()
    print("<" + hash * "#" + lines * "-" + ">")
    for j in range(184):
      R = temporary_list[m][0][0]
      V = temporary_list[m][0][1]
      B = temporary_list[m][0][2]
      m += 1
      img.putpixel((i, j), (R, V, B))




img.save("EngiignE.png","png")
print("EngiignE saved!")


#img.show()


#neerreen

img = Image.open("Engineer.png")

list = []

for i in range(92):
  for j in range(184):
    RVB = img.getpixel((i, j))
    l = [RVB]
    list.append(l)

temporary_list = []

m = 0
n = 92
for i in range(92):
    m = 1
    n -= 1
    for j in range(184):
        temporary_list.append(list[m + ((n * 184)-1)])
        m += 1
        


        
m = 0
for i in range(92, 184):
    clear()
    hash = m // 1000
    lines = 16 - hash
    print("<" + hash * "#" + lines * "-" + ">")
    for j in range(184):
      R = temporary_list[m][0][0]
      V = temporary_list[m][0][1]
      B = temporary_list[m][0][2]
      m += 1
      img.putpixel((i, j), (R, V, B))




img.save("neerreen.png","png")
print("neerreen saved!")


#img.show()
    

#MutatEngie

img = Image.open("Engineer.png")

list = []

for i in range(92, 184):
  for j in range(184):
    RVB = img.getpixel((i, j))
    l = [RVB]
    list.append(l)

temporary_list = []

m = 0
n = 92
for i in range(92):
    m = 0
    n -= 1
    for j in range(184):
        temporary_list.append(list[m + ((n * 183)-1)])
        m += 1
        
        
m = 0
for i in range(92):
    clear()
    hash = m // 1000
    lines = 16 - hash
    print("<" + hash * "#" + lines * "-" + ">")
    for j in range(184):
      R = temporary_list[m][0][0]
      V = temporary_list[m][0][1]
      B = temporary_list[m][0][2]
      m += 1
      img.putpixel((i, j), (R, V, B))




img.save("MutatEngie.png","png")
print("MutatEngie saved!")


#img.show()

















