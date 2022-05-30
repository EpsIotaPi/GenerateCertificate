from PIL.ImageColor import getrgb


class templateInfo:

# 模版存储位置
    tempFileName = r'Source/Template/BlankTemp.png'
# 模版预览效果存储位置
    previewSavePath = "preview.pdf"
    tempSavePath = 'zout.png'

# 字体文件
    STKaiti = 'Source/Fonts/STKaiti.ttf'

# 字体样式配置信息
    # 获奖等级
    awardSize = 144
    awardColor = getrgb('#B34B00')       # 179, 75, 0
    awardTag_pos = (1125, 780)

    # 正文
    bodySize = 75
    bodyColor = getrgb('#3A5570')               # 58, 85, 112
    bodyLine1_pos = (498, 502)      # 第一行
    bodyLine2_pos = (370, 604)      # 第二行
    bodyLine3_pos = (370, 709)      # 第三行

    # 附加信息
    infoSize = 46
    infoColor = getrgb('#3A5570')                # 58, 85, 112
    authorInfo_pos = (422, 965)     # 作者信息
    teacherInfo_pos = (511, 1045)   # 教师信息
    classifiedInfo_Pos = (511, 1124) # 作品分类信息
    numInfo_pos = (511, 1203)       # 作品编号信息

    # 日期
    dateSize = 56
    dateColor = getrgb('#3A5570')                  # 58, 85, 112
    yearDate_pos = (2200, 1460)     # 年份
    monDate_pos = (2384, 1460)      # 月份

class configuration:

    # 获奖名单
    NameList = 'Source/NameList/nameList.xlsx'

    # 导出PDF文件存储路径
    pdfSavePath = "4C2021/"

    # 日期时间设置
    useLocalTime = True
    Year = None
    Month = None

