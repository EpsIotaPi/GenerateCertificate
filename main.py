'''
批量生产电子奖状
'''

from GenCertificateInfo import *
from InfoSource.dealExcel import read_xlsx
import fitz
import os
os.mkdir("4C2021/")

def png2pdf(sourcePath='./', desPath='./out'):
    imgdoc = fitz.open(sourcePath)
    pdfBytes = imgdoc.convert_to_pdf()
    imgpdf = fitz.open('pdf', pdfBytes)
    if desPath[-4:] != '.pdf':
        desPath += '.pdf'
    imgpdf.save(filename=desPath)

tempFN = r'Source/Template/BlankTemp.png'



sourceFP = 'Source/NameList/20210817.xlsx'
tempSavePath = 'zout.png'

awardInfo = read_xlsx(sourceFP)

for i in range(len(awardInfo)):

    tempImg = Image.open(tempFN)
    tempDraw = ImageDraw.Draw(tempImg)

    newCert = CertificateInformation(awardInfo[i])
    newCert.addText(draw=tempDraw)
    tempImg.save(tempSavePath)
    schoolName = newCert.entrie.Entries_school
    certID = newCert.id
    dirPath = "4C2021/{}/".format(schoolName)
    filePath = dirPath + "{0}_{1}".format(schoolName, certID)

    if os.path.isdir(dirPath) == False:
        os.mkdir(dirPath)
        print("mkdir {}".format(dirPath))

    png2pdf(sourcePath='zout.png', desPath=filePath)
    print("荣誉证书制作完成_" + certID + "_{}/{}".format(i+1, len(awardInfo)))
