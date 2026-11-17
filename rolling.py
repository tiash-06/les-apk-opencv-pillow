from PIL import Image

def merge(im1: Image.Image, im2: Image.Image) -> Image.Image:
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im


if __name__ == "__main__":
    # Commande manokatra an'ilay sariko ao amin'ny dossier pillow
    with Image.open("TH.jpg") as im1:
        # Manao ny fusion (ampiarahina indroa ilay sary ho an'ny test)
        resultat = merge(im1, im1)
        
        # Sauvegarde le résultat
        resultat.convert("RGB").save("TH_fusion.jpg")
        print("Succès ! Images fusionnées et sauvegardées sous 'TH_fusion.jpg'.")