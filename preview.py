'''
制作电子奖状预览
'''

from GenCertificateInfo import *
from PIL import Image
from config import templateInfo, configuration

def png2pdf(sourcePath='./', desPath='./out'):
    image_1 = Image.open(sourcePath)
    im_1 = image_1.convert('RGB')
    im_1.save(desPath)

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
