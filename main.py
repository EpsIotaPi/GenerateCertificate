'''
批量生产电子奖状
'''

from TextProcess import *
from GenCertificateInfo import CertificateInformation

newCert = CertificateInformation()
newCert.addText()

save_adress = 'zout.png'
tempImg.save(save_adress)
print("荣誉证书制作完成")