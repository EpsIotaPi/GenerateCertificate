# from docx.shared import RGBColor
from PIL.ImageColor import getrgb
from PIL import ImageFont
from config import templateInfo

# 定义字体
STKaiti = templateInfo.STKaiti

class TextStyle:
    font_fp = STKaiti
    size = 100
    color = getrgb('#000000')

    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def makeFont(self):
        fonts = ImageFont.truetype(self.font_fp, size=self.size)
        return fonts

    def addText(self, text, img):
        x = self.x
        y = self.y
        font = self.makeFont()
        img.text((x, y), text, font=font, fill=self.color)

class awardStyle(TextStyle):
   size = templateInfo.awardSize
   color = templateInfo.awardColor

class bodyStyle(TextStyle):
   size = templateInfo.bodySize
   color = templateInfo.bodyColor

class infoStyle(TextStyle):
   size = templateInfo.infoSize
   color = templateInfo.infoColor

class dateStyle(TextStyle):
   size = templateInfo.dateSize
   color = templateInfo.dateColor


awardTag = awardStyle(templateInfo.awardTag_pos)
bodyLine1 = bodyStyle(templateInfo.bodyLine1_pos)
bodyLine2 = bodyStyle(templateInfo.bodyLine2_pos)
bodyLine3 = bodyStyle(templateInfo.bodyLine3_pos)
authorInfo = infoStyle(templateInfo.authorInfo_pos)
teacherInfo = infoStyle(templateInfo.teacherInfo_pos)
classifiedInfo = infoStyle(templateInfo.classifiedInfo_Pos)
numInfo = infoStyle(templateInfo.numInfo_pos)
yearDate = dateStyle(templateInfo.yearDate_pos)
monDate = dateStyle(templateInfo.monDate_pos)