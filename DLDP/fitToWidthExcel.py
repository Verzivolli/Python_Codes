def get_files_in_folder(folder,extension):
	import os
	file_list = []
	for file in os.walk(folder):
		if file.endswith(extension):
			file_list.append(os.path.join(folder,file))
	return file_list
import openpyxl, os
folder = r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\WM-20180411T124506Z-001\Ministria e Turizmit dhe Mjedisit-WM\PerDorezim"
paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk(folder)
        for filename in filenames)



for f in paths:
	# print(f)
	if f.endswith(".xlsx"):
		wb = openpyxl.load_workbook(f)
		ws = wb.active
		ws.sheet_properties.pageSetUpPr.fitToPage = 1
		ws.page_setup.fitToHeight = 0
		wb.save(f)