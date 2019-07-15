import xlrd
import os


def readExcel(name):
    
    workbook = xlrd.open_workbook(name)
    print (f"workbook:{workbook.sheet_names()}") #返回excel中所有sheets的名字
    print (workbook.sheet_loaded('Sheet1')) #加载成功返回True
    
    sheets = workbook.sheets() #返回excel所有sheet对象列表
    
    sheet1_index = workbook.sheet_by_index(0) #sheet索引从0开始
    sheet1_name = workbook.sheet_by_name('Sheet1') #获取名字为Sheet1的工作表
    print (f"sheet1_index:{sheet1_index}")
    print (f"sheet1_name:{sheet1_name}")
    
    #sheet的名称，行数，列数
    sheet1 = sheet1_index
    print (sheet1.name,sheet1.nrows,sheet1.ncols)
    
    #获取整行和整列的值
    rows = sheet1.row_values(3) #获取第四行全部单元格内容
    cols = sheet1.col_values(1) #获取第二列全部单元格内容 
    print (f"rows:{rows},cols:{cols}")
    
    #获取单元格内容
    print (type(sheet1.cell(1,0))) #获取第2行1列单元对象
    print (sheet1.cell_value(1,0)) #获取第2行1列数据
    
    print (sheet1.row(3)[3].value) #获取第四行（list）第4个值
if __name__ == "__main__":
    #或许脚本所在路径
    path = os.path.split(os.path.realpath(__file__))[0]
    xpath = os.path.join(path,'case','test.xlsx')
    print(f"xpath:{xpath}")
    
    readExcel(xpath)