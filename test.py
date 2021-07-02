
from GenCertificateInfo import CertificateInformation
from InfoSource.dealExcel import read_xlsx


tbFP = 'Source/NameList/nameList.xlsx'

readE = read_xlsx(tbFP)

cert = CertificateInformation(readE[0])
print(cert.id)