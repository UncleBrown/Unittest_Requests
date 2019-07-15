#读取excel方法
import os
from testFile import getpathInfo
from xlrd import open_workbook

path = getpathInfo.get_path()

class readExcel():
    
    def get_xls(self,xls_name,sheet_name):
        #xls_name 填写用例的Excel名称 ，sheet_name该Excel的sheet名称
        cls = []
        #获取用例路径
        xlsPath = os.path.join(path,'case',xls_name)
        book = open_workbook(xlsPath) #获得打开Excel的sheet
        #获取sheet内容行数
        sheet = book.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        #print (nrows)
        for i in range(nrows):#根据行数做循环
            #如果这个Excel的这个sheet第i行的第一列 != case_name，则将该行添加至cls[]
            #table.row_values(rowx) 返回rowx行所有单元格数据list
            #sheet.row_values(i)[j] 返回i+1行第j+1个单元格数据（j从0开始计数）
            #print(f"start for loop:{i}")
            #print(sheet.row_values(i)[0])
            if sheet.row_values(i)[0] != 'case_name':
               # print (f"{i}:",sheet.row_values(i))
                cls.append(sheet.row_values(i))
            #print(cls)
        return cls
if __name__ == "__main__":
    print(readExcel().get_xls('userCase.xlsx','login'))
    print(readExcel().get_xls('userCase.xlsx','login')[0][1])
    print(readExcel().get_xls('userCase.xlsx','login')[1][2])
        
