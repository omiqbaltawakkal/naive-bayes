import xlrd
import numpy as np

def getData(filename, index_sheet):
	data = xlrd.open_workbook(filename)
	sheet = data.sheet_by_index(index_sheet)
	return sheet
	
# print getData("dummy.xls",0)
data = getData("dummy.xls",0)
sheet_row = data.nrow
sheet_cols = data.ncols

def getDataInput(atribut):
	datainput = []
	for i in range(1, sheet_row):
		datainput.append(data.row(i)[atribut].value)
	return datainput

# print getDataInput(1)

def tabellikeli(atribut, kelas):
	num_yes=0
	num_no=0
	prob_yes = 0
	prob_no = 0
	listdata=[]
	for i in range(getDataInput(atribut)):
		if data.row(i)[atribut].value != datainput:
			listdata.append(data.row(i)[atribut].value)
		if data.row(i)[kelas].value == "Yes":
			num_yes++
		else:
			num_no++
  #kuran numpy
 
