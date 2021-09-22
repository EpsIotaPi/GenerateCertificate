'''
制作电子奖状预览
'''

from GenCertificateInfo import *
import fitz
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
previewSavePath = templateInfo.previewSavePath

tempImg = Image.open(tempFileName)
tempDraw = ImageDraw.Draw(tempImg)
tempCert = Entries(id=2021012345,
                   name="飞向太空",
                   school="杭州电子科技大学",
                   classifed="人工智能应用",
                   author=["作者一", "作者二", "作者三", "作者四", "作者五"],
                   teacher=["指导教师一", "指导教师二"],
                   award="一等奖")
newCert = CertificateInformation(tempCert)
newCert.addText(draw=tempDraw)
tempImg.save(tempSavePath)

png2pdf(sourcePath=tempSavePath, desPath=previewSavePath)
print("预览生成完成")
