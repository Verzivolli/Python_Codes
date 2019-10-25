# import pandas
# import os
# folder = "testingData"
# csv_file = "perrel.csv"
# import sys
# from importlib import reload
# reload(sys)
# import codecs
# def readlines(fname):
# 	with open(fname) as f:
# 		return f.read().splitlines()
# # sys.setdefaultencoding("utf-8")
# encoding = sys.getdefaultencoding()
# # df = pandas.DataFrame()
# # df = pandas.read_csv(os.path.join(folder,csv_file),  encoding = encoding)
# from numpy import genfromtxt
# my_data = readlines(os.path.join(folder,csv_file))
# splitted_data=[]
# for data in my_data:
# 	splitted_data.append(data.split(","))
# for data in splitted_data:
# 	if
# 	print(data[0],data[1])

csv_folder = r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\Code"
csv_file = r"Relacion.csv"
def readlines(folder,fname):
	import os
	with open(os.path.join(folder,fname)) as f:
		return f.read().splitlines()
my_data = readlines(csv_folder,csv_file)
splitted_data = []
for data in my_data:
	splitted_data.append(data.split(","))
for data in splitted_data:
	# print(data[1])
	if str(data[1])=="":
		print("empty line found!")