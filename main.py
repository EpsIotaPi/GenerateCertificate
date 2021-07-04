'''
批量生产电子奖状
'''

from GenCertificateInfo import *
from InfoSource.dealExcel import read_xlsx
import fitz

def png2pdf(sourcePath='./', desPath='./out'):
    imgdoc = fitz.open(sourcePath)
    pdfBytes = imgdoc.convert_to_pdf()
    imgpdf = fitz.open('pdf', pdfBytes)
    if desPath[-4:] != '.pdf':
        desPath += '.pdf'
    imgpdf.save(filename=desPath)

tempFN = r'Source/Template/BlankTemp.png'



sourceFP = 'Source/NameList/nameList.xlsx'
tempSavePath = 'zout.png'

awardInfo = read_xlsx(sourceFP)

for i in range(len(awardInfo)):
    tempImg = Image.open(tempFN)
    tempDraw = ImageDraw.Draw(tempImg)

    newCert = CertificateInformation(awardInfo[i])
    newCert.addText(draw=tempDraw)
    tempImg.save(tempSavePath)
    filename = newCert.id

    png2pdf(sourcePath='zout.png', desPath='outPDF/'+filename)
    print("荣誉证书制作完成_" + filename)
