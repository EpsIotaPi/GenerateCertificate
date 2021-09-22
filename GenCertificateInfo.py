import time
from TextProcess import *
from InfoSource import Entries
from PIL import Image, ImageDraw
from config import templateInfo, configuration

body_font = ImageFont.truetype(STKaiti, size=75)

testFN = templateInfo.tempFileName
testImg = Image.open(testFN)
testDraw = ImageDraw.Draw(testImg)


def nameSplic(names):
    s = ''
    for i in names:
        s += i + '、'
    return s[:-1]

class CertificateInformation:
    AwardClass = '零'
    bodyText = '占位符'
    author = '占位符'
    teacher = '占位符'
    classified = '占位符'
    id = '占位符'

    def __init__(self, entrie:Entries):
        self.entrie = entrie
        self.AwardClass =  entrie.Entries_award
        self.bodyText = entrie.Entries_school + '作品《' + entrie.Entries_name + '》在 2021 年（第 14 届）中国大学生计算机设计大赛浙江省级赛中荣获'
        self.author = nameSplic(entrie.Entries_author)
        self.teacher = nameSplic(entrie.Entries_teacher)
        self.classified = entrie.Entries_classifed
        self.id = entrie.Entries_id


    def __isAorD(self, text, idx):
            c = text[idx]
            return c.encode('UTF-8').isalpha() or c.encode('UTF-8').isdigit()

    def __splitText(self, text:str, warpSize:int):
        splitPos = len(text)
        while testDraw.textsize(text[0:splitPos], font=body_font)[0] > warpSize:
            if splitPos == 0:
                break
            splitPos -= 1

        if splitPos == len(text):
            return splitPos

        punc_front = ['《', '（']
        if  text[splitPos-1] in punc_front:
            splitPos -= 1

        punc_back = ['》', '）']
        if  text[splitPos] in punc_back:
            splitPos += 1

        if self.__isAorD(text, splitPos):
            strat = splitPos
            end = splitPos
            while self.__isAorD(text, strat):
                strat -= 1
            strat += 1
            while self.__isAorD(text, end):
                end += 1
            if testDraw.textsize(text[strat:splitPos], font=body_font)[0] > testDraw.textsize(text[splitPos:end], font=body_font)[0]:
                splitPos = end
            else:
                splitPos = strat
        return splitPos

    def __addBlank(self, text):
        textWithBlank = ''
        isAlpha = True
        for i in range(len(text)):
            if self.__isAorD(text, i):
                if isAlpha:
                    textWithBlank += ' '
                    isAlpha = False
            else:
                if not isAlpha:
                    textWithBlank += ' '
                    isAlpha = True
            textWithBlank += text[i]
        return textWithBlank

    def __splitBody(self):
        # textWithoutBlank = self.bodyText.replace(' ','')
        text = self.bodyText
        pos1 = self.__splitText(text, 1830)
        pos2 = self.__splitText(text[pos1:], 2000)
        pos2 += pos1
        L1 = text[0:pos1]
        L2 = text[pos1:pos2]
        L3 = text[pos2:]

        return L1, L2, L3

    def __getDateInfo(self):
        Year  = time.localtime(time.time()).tm_year
        Mon = time.localtime(time.time()).tm_mon
        if configuration.useLocalTime:
            return str(Year), str(Mon)
        return str(configuration.Year), str(configuration.Month)

    def addText(self, draw):
        awardTag.addText(self.AwardClass, draw)

        L1, L2, L3 = self.__splitBody()
        bodyLine1.addText(L1, draw)
        bodyLine2.addText(L2, draw)
        bodyLine3.addText(L3, draw)

        authorInfo.addText(self.author, draw)
        teacherInfo.addText(self.teacher, draw)
        classifiedInfo.addText(self.classified, draw)
        numInfo.addText(self.id, draw)

        year, month = self.__getDateInfo()
        yearDate.addText(year, draw)
        monDate.addText(month, draw)
