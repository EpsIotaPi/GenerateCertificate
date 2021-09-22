1. 所需依赖包

```shell
pip install Pillow python-doxc xlrd==1.2.0 fitz lxml==4.3 networkx==2.0 PyMuPDF

或

pip install -r requirement.txt
```

2. 获奖名单格式（）

| 作品编号   | 作品名称 | 参赛学校         | 作品类别     | 作者1-5 | 指导教师1-2 | 获奖等级 |
| ---------- | -------- | ---------------- | ------------ | ------- | ----------- | -------- |
| 2021012345 | 飞向太空 | 杭州电子科技大学 | 人工智能应用 | 作者    | 指导教师    | 一等奖   |
* 作者不足五位，指导教师不足两位，空余列填写「无」。
* 应为 `xlsx` 格式，信息列顺序不得随意改动。
* 模版参考 `Source/NameList/nameList.xlsx`

3. 配置信息

	1. 预览配置

	```python
	配置模版存储位置 tempFileName
	配置模版预览存储位置 previewSavePath
	配置字体样式（可配置字号 ***Size，字体颜色 ***Color）
	配置文本位置 ***_pos
	
	运行 preview.py
	```

	2. 导出配置

	```python
	配置获奖名单存储位置 NameList
	配置导出PDF文件存储位置 pdfSavePath
	配置日期时间设置
	默认情况下使用当前的年月信息，设置 useLocalTime = True
	当 useLocalTime == False 时，使用 Year，与 Month 指定时间（使用 int 或 str）
	
	运行 main.py
	```

	
