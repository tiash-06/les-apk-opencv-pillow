from PIL import Image

# 1. Préparation an ireo verison an imagen ilay sary Th.png 
with Image.open("TH.jpg") as im:
    img1 = im.copy()
    img2 = im.rotate(90)
    img3 = im.rotate(180)
    img4 = im.rotate(270)

images = [img1, img2, img3, img4]

# 2. Sauvegarder an ireo sary tsirairay ho lasa gif 
images[0].save(
    "TH_animated.gif",
    save_all=True,
    append_images=images[1:],
    duration=500,  # Durée de chaque image en millisecondes (0.5 seconde)
    loop=0,        # Boucle infinie
)

print("Succès ! GIF animé créé sous 'TH_animated.gif'.")