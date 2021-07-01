import time
from TextProcess import *

class CertificateInformation:
    AwardClass = '零'
    bodyText = '占位符'
    author = '占位符'
    teacher = '占位符'
    classified = '占位符'
    numbers = '占位符'

    def __splitBody(self):
        L1, L2, L3 = self.bodyText, '', ''
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
        NumInfo.addText(self.numbers)

        year, month = self.__getDateInfo()
        yearDate.addText(year)
        monDate.addText(month)
