'''
批量生产电子奖状
'''

from TextProcess import *
from GenCertificateInfo import CertificateInformation
from InfoSource.dealExcel import read_xlsx

sourceFP = 'Source/NameList/nameList.xlsx'

awardInfo = read_xlsx(sourceFP)
newCert = CertificateInformation(awardInfo[0])



newCert.addText()

save_adress = 'zout.png'
tempImg.save(save_adress)
print("荣誉证书制作完成")