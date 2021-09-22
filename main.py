'''
批量制作电子奖状
'''

from GenCertificateInfo import *
from InfoSource.dealExcel import read_xlsx
import fitz
import os
from config import templateInfo, configuration



def png2pdf(sourcePath='./', desPath='./out'):
    imgdoc = fitz.open(sourcePath)
    pdfBytes = imgdoc.convert_to_pdf()
    imgpdf = fitz.open('pdf', pdfBytes)
    if desPath[-4:] != '.pdf':
        desPath += '.pdf'
    imgpdf.save(filename=desPath)

tempFileName = templateInfo.tempFileName
tempSavePath = templateInfo.tempSavePath
nameList = configuration.NameList
pdfSavePath = configuration.pdfSavePath

if os.path.exists(pdfSavePath):
    os.rmdir(pdfSavePath)
    print("文件夹 {} 已被清空".format(pdfSavePath))
else:
    os.mkdir(pdfSavePath)
    print("创建文件夹 {}".format(pdfSavePath))

CertInfo = read_xlsx(nameList)

for i in range(len(CertInfo)):

    tempImg = Image.open(tempFileName)
    tempDraw = ImageDraw.Draw(tempImg)

    newCert = CertificateInformation(CertInfo[i])
    newCert.addText(draw=tempDraw)
    tempImg.save(tempSavePath)
    schoolName = newCert.entrie.Entries_school
    certID = newCert.id
    dirPath = os.path.join(configuration.pdfSavePath, "{}/".format(schoolName))
    filePath = os.path.join(dirPath, "{0}_{1}".format(schoolName, certID))

    if os.path.isdir(dirPath) == False:
        os.mkdir(dirPath)
        print("创建文件夹 {}".format(dirPath))

    png2pdf(sourcePath=tempSavePath, desPath=filePath)
    print("荣誉证书_"+ certID +"_制作完成，进度：{}/{}".format(i+1, len(CertInfo)))

if os.path.isfile(tempSavePath):
    os.remove(tempSavePath)