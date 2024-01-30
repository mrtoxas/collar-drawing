from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os.path

collar = {
    'length':{
        'coord':    (676,506),
        'msg':      'Длина'
    },
    'min':{
        'coord':    (464,330),
        'msg':      'min'
    },
    'max':{
        'coord':    (617,418),
        'msg':      'max'
    },
    'width':{
        'coord':    (1188,205),
        'msg':      'Ширина'
    },
    'holes':{
        'coord':    (723,330),
        'msg':      'Расстояние между дырками'
    }
}

img = Image.open("template/template.jpg")
unit = 'cm'
fontSize = 22
font = ImageFont.truetype("template/gost.ttf",fontSize)
draw = ImageDraw.Draw(img)
for i in collar:
    value = input((collar[i]['msg']+'(' + unit + '): ')) +unit
    wText = draw.textsize(value)[0]
    hText = draw.textsize(value)[1]
    draw.text(((collar[i]['coord'][0]-wText),collar[i]['coord'][1]-(hText+fontSize)), value, fill="black", font=font)
img.save("gotovo.jpg")