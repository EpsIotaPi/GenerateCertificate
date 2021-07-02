import time
from TextProcess import *
from InfoSource import Entries


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

    def __splitBody(self):
        sp1 = 24
        sp2 = 56

        L1 = self.bodyText[:sp1]
        L2 = self.bodyText[sp1:sp2]
        L3 = self.bodyText[sp2:]
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
