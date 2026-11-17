from PIL import Image, ImageOps, ImageEnhance, ImageFilter

if __name__ == "__main__":
    with Image.open("TH.jpg") as im:
        # 1. Test du redimensionnement relatif (ex: contain)
        size = (100, 150)
        img_contain = ImageOps.contain(im, size)
        img_contain.save("TH_contain.jpg")
        
        # 2. Test d'un filtre (ex: DETAIL)
        img_filtered = im.filter(ImageFilter.DETAIL)
        img_filtered.save("TH_filtered.jpg")
        
        # 3. Test d'amélioration du contraste
        enh = ImageEnhance.Contrast(im)
        img_contrast = enh.enhance(1.3)
        img_contrast.save("TH_contrast.jpg")
        
        print("Succès ! Tous les tests d'optimisation et d'enhancement ont été générés.")