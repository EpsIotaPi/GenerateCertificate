
from TextProcess import *

STKaiti = 'Source/Fonts/STKaiti.ttf'

body_font = ImageFont.truetype(STKaiti, size=75)

text = '杭州电子科技大学作品《针对医学血液细胞显微图片的细胞检测技术》在 2021 年（第 14 届）中国大学生计算机设计大赛中获'

def splitText(text: str, warpSize: int):
    splitPos = len(text)
    while tempDraw.textsize(text[0:splitPos], font=body_font)[0] > warpSize:
        if splitPos == 0:
            break
        splitPos -= 1
    print(text[:splitPos])

    punc = ['》', '）']
    if text[splitPos] in punc:
        splitPos += 1

    def isAorD(idx):
        c = text[idx]
        return c.encode('UTF-8').isalpha() or c.encode('UTF-8').isdigit() or c == ' '

    if isAorD(splitPos):
        strat = splitPos
        end = splitPos
        while isAorD(strat):
            strat -= 1
        strat += 1
        while isAorD(end):
            end += 1
        if tempDraw.textsize(text[strat:splitPos], font=body_font)[0] > \
                tempDraw.textsize(text[splitPos:end], font=body_font)[0]:
            splitPos = end
        else:
            splitPos = strat
    print(tempDraw.textsize(text[0:splitPos], font=body_font))
    return splitPos

sp1 = splitText(text, 1800)
sp2 = splitText(text[sp1:], 2000)


tempDraw.text((498, 502), text[0:sp1], font=body_font, fill=RGBColor(179, 75, 0))
tempDraw.text((370, 604), text[sp1:sp1+sp2], font=body_font, fill=RGBColor(179, 75, 0))
tempDraw.text((370, 709), text[sp1+sp2:], font=body_font, fill=RGBColor(179, 75, 0))

save_adress = './zout.png'
tempImg.save(save_adress)
print("荣誉证书制作完成")