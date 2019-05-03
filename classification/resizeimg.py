from PIL import Image
from os import listdir

files = [f for f in listdir("./train-fullsize/noncriminal/")]

for file in files:
    img = Image.open("./train-fullsize/noncriminal/"+file)
    newIMG = img.resize((300,300))
    newIMG.save("train-300/noncriminal/"+file[0:-4]+".png", "PNG")

files = [f for f in listdir("./train-fullsize/criminal/")]

for file in files:
    img = Image.open("./train-fullsize/criminal/"+file)
    newIMG = img.resize((300,300))
    newIMG.save("train-300/criminal/"+file[0:-4]+".png", "PNG")
