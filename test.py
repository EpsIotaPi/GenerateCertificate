import fitz
import os
import glob

def png2pdf(sourcePath='./', desPath='./out'):
    imgdoc = fitz.open(sourcePath)
    pdfBytes = imgdoc.convert_to_pdf()
    imgpdf = fitz.open('pdf', pdfBytes)
    if desPath[-4:] != '.pdf':
        desPath += '.pdf'
    imgpdf.save(filename=desPath)



png2pdf(sourcePath='./zout.png', desPath='./outPDF/zout')