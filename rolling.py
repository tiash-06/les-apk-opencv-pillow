from PIL import Image

def roll(im: Image.Image, delta: int) -> Image.Image:
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im


if __name__ == "__main__":
    #commande manokatra an ilay sariko ao amn dossier pillow
    with Image.open("TH.jpg") as im:
        # manome an ilay decalage roll
        resultat = roll(im, 100)
        
        # Sauvegarde le résultat
        resultat.save("TH_rolee.jpg")
        print("Succès ! Image modifiée et sauvegardée sous 'TH_rolee.jpg'.")