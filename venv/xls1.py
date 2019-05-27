import xlsxwriter

workbook = xlsxwriter.workbook('Expenses01.xlsx') #创建或者打开xlsx

worksheet = workbook.add_worksheet() #创建或者打开一个sheet

# 创建数据，用（）代表元组，用[]代表列表；每个[]代表一行，以‘,’相隔，[]内 每个‘,’代表相隔一列
expense = (
    ['Rent',1000],
    ['Gas',100],
    ['Food',300],
    ['Gym',50],
)

#从第一个单元格开始,行和列为零索引
row = 0
col = 0

#基础写法：worksheet.wrte(行，列，数据，格式)
# worksheet.write_row（单元格位置，数据）写行，
# worksheet.write_column（单元格位置，数据）写列,

worksheet.write_row('A1',expense[0])
worksheet.write_row('A2',expense[1])
worksheet.write_row('A3',expense[2])
worksheet.write_row('A4',expense[3])


