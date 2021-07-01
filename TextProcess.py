from docx.shared import Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont

tempFN = r'BlankTemp.png'
tempImg = Image.open(tempFN)
tempDraw = ImageDraw.Draw(tempImg)

# 定义字体
STKaiti = './STKaiti.ttf'

class TextStyle:
    font_fp = STKaiti
    size = 100
    color = RGBColor(0, 0, 0)

    def makeFont(self):
        fonts = ImageFont.truetype(self.font_fp, size=self.size)
        return fonts

class awardStyle(TextStyle):
   size = 144
   color = RGBColor(179, 75, 0)

   def __init__(self, x, y):
       self.x = x
       self.y = y

   def addText(self, text, img=tempDraw):
       x = self.x
       y = self.y
       font = self.makeFont()
       img.text((x, y), text, font=font, fill=self.color)

class bodyStyle(TextStyle):
   size = 75
   color = RGBColor(58, 85, 112)

   def __init__(self, x, y):
       self.x = x
       self.y = y

   def addText(self, text, img=tempDraw):
       x = self.x
       y = self.y
       font = self.makeFont()
       img.text((x, y), text, font=font, fill=self.color)

class infoStyle(TextStyle):
   size = 46
   color = RGBColor(58, 85, 112)

   def __init__(self, x, y):
       self.x = x
       self.y = y

   def addText(self, text, img=tempDraw):
       x = self.x
       y = self.y
       font = self.makeFont()
       img.text((x, y), text, font=font, fill=self.color)

class dateStyle(TextStyle):
   size = 56
   color = RGBColor(58, 85, 112)

   def __init__(self, x, y):
       self.x = x
       self.y = y

   def addText(self, text, img=tempDraw):
       x = self.x
       y = self.y
       font = self.makeFont()
       img.text((x, y), text, font=font, fill=self.color)

AwardTag = awardStyle(1125, 780)
bodyLine1 = bodyStyle(498, 502)
bodyLine2 = bodyStyle(370, 604)
bodyLine3 = bodyStyle(370, 709)
authorInfo = infoStyle(422, 965)
teacherInfo = infoStyle(511, 1045)
classifiedInfo = infoStyle(511, 1124)
NumInfo = infoStyle(511, 1203)
yearDate = dateStyle(2200, 1460)
monDate = dateStyle(2384, 1460)