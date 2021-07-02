import xlrd
from InfoSource import Entries

tbFP = 'Source/NameList/nameList.xlsx'


def read_xlsx(tbfp):

    tbFile = xlrd.open_workbook(filename=tbfp)  # 打开文件
    sheet = tbFile.sheet_by_index(0)  # 通过索引获取表格

    read_Entries = []
    for row_id in range(1, sheet.nrows):
        row = sheet.row_values(row_id)

        ent = Entries(id=row[0],
                      name=row[1],
                      school=row[2],
                      classifed=row[3],
                      author=row[4:9],
                      teacher=row[9:11],
                      award=row[11])
        read_Entries.append(ent)
    return read_Entries

readE = read_xlsx(tbFP)


