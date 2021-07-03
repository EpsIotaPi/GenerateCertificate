import time
from TextProcess import *
from InfoSource import Entries
import string

body_font = ImageFont.truetype(STKaiti, size=75)

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
        self.AwardClass =  entrie.Entries_award
        self.bodyText = entrie.Entries_school + '作品《' + entrie.Entries_name + '》在 2021 年（第 14 届）中国大学生计算机设计大赛中获'
        self.author = nameSplic(entrie.Entries_author)
        self.teacher = nameSplic(entrie.Entries_teacher)
        self.classified = entrie.Entries_classifed
        self.id = entrie.Entries_id

    def splitText(self, text:str, warpSize:int):
        splitPos = len(text)
        while tempDraw.textsize(text[0:splitPos], font=body_font)[0] > warpSize:
            if splitPos == 0:
                break
            splitPos -= 1

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
            if tempDraw.textsize(text[strat:splitPos], font=body_font)[0] > tempDraw.textsize(text[splitPos:end], font=body_font)[0]:
                splitPos = end
            else:
                splitPos = strat
        print(tempDraw.textsize(text[0:splitPos], font=body_font))
        return splitPos



    def __splitBody(self):
        pos1 = self.splitText(self.bodyText, 1800)
        pos2 = self.splitText(self.bodyText[pos1:], 2000)
        pos2 += pos1
        print(pos1)
        L1 = self.bodyText[0:pos1]
        L2 = self.bodyText[pos1:pos2]
        L3 = self.bodyText[pos2:]
        return L1, L2, L3

    def __getDateInfo(self):
        Year  = time.localtime(time.time()).tm_year
        Mon = time.localtime(time.time()).tm_mon
        return str(Year), str(Mon)

    def addText(self):
        AwardTag.addText(self.AwardClass)

        L1, L2, L3 = self.__splitBody()
        bodyLine1.addText(L1)
        bodyLine2.addText(L2)
        bodyLine3.addText(L3)

        authorInfo.addText(self.author)
        teacherInfo.addText(self.teacher)
        classifiedInfo.addText(self.classified)
        NumInfo.addText(self.id)

        year, month = self.__getDateInfo()
        yearDate.addText(year)
        monDate.addText(month)
