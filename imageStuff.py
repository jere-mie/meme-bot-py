from PIL import Image, ImageDraw, ImageFont


def makeMeme(fname, text):
    image = Image.open(f'images/{fname}.png')
    font = ImageFont.truetype('impact.ttf', 40)
    draw = ImageDraw.Draw(image)
    if len(text)>27:
        lim=27
        for i in range(27):
            if text[i]==' ':
                lim=i
        draw.text(xy=(5,0), text=text[0:lim], fill=(0,0,0), font=font)
        draw.text(xy=(0,42), text=text[lim:len(text)], fill=(0,0,0), font=font)
    else:
        draw.text(xy=(5,0), text=text, fill=(0,0,0), font=font)
    image.save('out.png')
    
    