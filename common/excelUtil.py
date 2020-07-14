#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : excelUtil.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import xlrd
from common.Logger import Logger


class excelUtil:

    def __init__(self):
        self.logger = Logger(logger="excelUtil").getlog()


    def getAllRowsBySheetIndex(self, sheetIndex, xlsFilePath):
        '''
        获取行视图
        根据Sheet序号获取该Sheet包含的所有行，返回值类似[ ['a', 'b', 'c'], ['1', '2', '3'] ]
        sheetIndex指示sheet的索引，0表示第一个sheet，依次类推
        xlsFilePath是Excel文件的相对或者绝对路径
        '''
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[sheetIndex]

        rows = []
        rowNum = table.nrows  # 总共行数
        rowList = table.row_values
        for i in range(rowNum):
            rows.append(rowList(i))  # 等价于rows.append(i, rowLists(i))

        return rows

    def getRow(self, sheetIndex, rowIndex, xlsFilePath):
        '''
        获取某个Sheet的指定序号的行
        sheetIndex从0开始
        rowIndex从0开始
        '''
        rows = self.getAllRowsBySheetIndex(sheetIndex, xlsFilePath)
        return rows[rowIndex]

    def getAllColsBySheetIndex(self, sheetIndex, xlsFilePath):
        '''
        获取列视图
        根据Sheet序号获取该Sheet包含的所有列，返回值类似[ ['a', 'b', 'c'], ['1', '2', '3'] ]
        sheetIndex指示sheet的索引，0表示第一个sheet，依次类推
        xlsFilePath是Excel文件的相对或者绝对路径
        '''
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[sheetIndex]

        cols = []
        colNum = table.ncols  # 总共列数
        colList = table.col_values
        for i in range(colNum):
            cols.append(colList(i))

        return cols

    def getCol(self, sheetIndex, colIndex, xlsFilePath):
        '''
        获取某个Sheet的指定序号的列
        sheetIndex从0开始
        colIndex从0开始
        '''
        cols = self.getAllColsBySheetIndex(sheetIndex, xlsFilePath)

        return cols[colIndex]

    def getCellValue(self, sheetIndex, rowIndex, colIndex, xlsFilePath):
        '''
        获取指定sheet的指定行列的单元格中的值
        '''
        workBook = xlrd.open_workbook(xlsFilePath)
        table = workBook.sheets()[sheetIndex]
        return table.cell(rowIndex, colIndex).value  # 或者table.row(0)[0].value或者table.col(0)[0].value

    def getDict(self, sheetIndex, rowIndex, colIndex, xlsFilePath):
        '''
        对预置数据(返回的是string)做转换，转成字典
        '''
        str1 = self.getCellValue(sheetIndex, rowIndex, colIndex, xlsFilePath)
        if str1.endswith(';'):
            str1 = str1[:-1]
            rcpList = str1.split(';')
        else:
            rcpList = str1.split(';')
        # rcpList = str1.split(';')
        rcpDict = {}
        for List in rcpList:
            rcpDict.update(self.listTODcit(List.split('=')))
        self.logger.info("测试数据为:%s" % rcpDict)
        return rcpDict

    def listTODcit(self, List):
        '''
        把列表转换成字典
        '''
        return ({List[0].strip(): List[1].strip()})

if __name__ == "__main__":
    ex = excelUtil()
    testData = ex.getDict(1,3,7,r'D:\anjouAutoTest\config\AnjouTestCase.xls')
    print(testData["filepath"])



