from PIL import Image, ImageDraw, ImageFont


def makeMeme(fname, text):
    image = Image.open(f'images/{fname}.png')
    size=45
    font = ImageFont.truetype('impact.ttf', size)
    draw = ImageDraw.Draw(image)
    w,h = font.getsize(text)
    if w<512:
        draw.text(xy=((512-w)/2,20), text=text, fill=(0,0,0), font=font)
    else:
        # Need to find the middle word
        x = int(len(text)/2)
        for i in range(int(len(text)/2)):
            if text[i] ==' ':
                x = i
        # x is the position of the last space before the middle of the text
        w,h = font.getsize(text[x:len(text)])
        while True:
            if w<495:
                break
            else:
                size-=1
                font = ImageFont.truetype('impact.ttf', size)
                w,h = font.getsize(text[x:len(text)])
        w1,h1 = font.getsize(text[0:x])
        w2,h2 = font.getsize(text[x:len(text)])
        draw.text(xy=((512-w1)/2,0), text=text[0:x], fill=(0,0,0), font=font)
        draw.text(xy=((512-w2)/2,42), text=text[x:len(text)], fill=(0,0,0), font=font)
    image.save('out.png')
    
# makeMeme('chungus', 'Hello World')