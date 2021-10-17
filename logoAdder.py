###~ Author : Antoine Boiteau ~###
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
import time

###~ Functions ~###

def retail(image, logo, pourcentage):
    width,height = image.shape[0],image.shape[1]
    if width < height :
        size_of_squarred_logo = int(width*pourcentage)
        return logo.resize((size_of_squarred_logo, size_of_squarred_logo))
    size_of_squarred_logo = int(height*pourcentage)
    return logo.resize((size_of_squarred_logo, size_of_squarred_logo))

###~ Script ~###

start_time = time.time()

pathInput = os.getcwd()
pathOutput= pathInput + "/Images_avec_logo"
print ("Travail en cours dans : %s \n" % pathInput)

if not os.path.isdir(pathInput + "/Images_avec_logo"):   
    os.mkdir(pathOutput)

for filename in os.listdir(pathInput):
    if filename[len(filename)-1] == "g" and filename != 'logo_test.png':

        print("Traitement de l'image : %s" % filename)
        img = Image.open(os.path.join(pathInput,filename))
        img = np.array(img)

        logo = Image.open('logo.png')
        logo = retail(img, logo, 0.2)
        logo = np.array(logo)
    
        width = img.shape[0]-logo.shape[0]
        height = img.shape[1]-logo.shape[1]

        margin = int(min(width,height)*0.01)
        width-= margin
        height-= margin

        for j in range (0,logo.shape[0]-1):
            for i in range (0,logo.shape[1]-1):
                if logo[j,i,3] != 0:
                    img[width+j,height+i,0:3] = logo[j,i,0:3]*(logo[j,i,3]/255)

        plt.imshow(img)
        imgASave = Image.fromarray(img)
        imgASave.save(pathOutput+"/modif_"+filename)

print("\nTerminé !!")
print("---Temps d'exécution : %ss ---" % (time.time() - start_time))

###~ End of script ~###