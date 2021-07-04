
from PIL import Image, ImageDraw, ImageFont

text = '杭州师范大学作品《智能社区健康管理系统》在2021年'

testFN = r'Source/Template/BlankTemp.png'
testImg = Image.open(testFN)
testDraw = ImageDraw.Draw(testImg)
STKaiti = 'Source/Fonts/STKaiti.ttf'
body_font = ImageFont.truetype(STKaiti, size=75)

print(testDraw.textsize(text, font=body_font)[0])