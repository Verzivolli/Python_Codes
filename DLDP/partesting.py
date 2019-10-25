import backend
import os
# line1 = backend.readlines('testingData\\empty.txt')[0] + ".txt"
folder = "testingData"
emprtydoc = "empty.txt"
folderpath = r"F:\LOT 1\Ani\Box_Sync\Finished\Codes\Python\DLDP\testingData"
# print(backend.readlines(os.path.join(folder,line1)))
# print(len(backend.readlines(os.path.join(folder,emprtydoc)))) # returns 0

doc_title = "Vend-depozitimi: " # heading 1
doc_normal_heading = "Rezultati final për Vend-depozitimin %s, e lokalizuar në koordinatat E: %s N: %s në Bashkinë e %s, Qarku %s."
# doc_normal_heading style "Body text"

# caption
# tabela e pikeve
# tabela emri

# add table

# body text
table_point1 = "Komente për rezultatin e vend-depozitimit së mbetjeve. (Gjendja e vend-depozitimit / Risqet kryesore mjedisore / Risqet kryesore lidhur me popullatën)"
table_point2 = "A ka ndonjë vend-hedhje mbeturinash afër? A ka ndonjë vend turistik të dukshëm nga vend-depozitimi e mbeturinave? Ose ndonjë zone të përcaktuar me VKM?"
table_point3 = "Harta / Fotografia / Skicat e vend-depozitimit së mbeturinave"

# print(backend.get_files_in_folder(r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\WM-20180411T124506Z-001\Ministria e Turizmit dhe Mjedisit-WM\foto\foto_id",".png"))

# backend.get_files_in_folder(folder,".xlsx")
# backend.get_table_from_xls_to_word("140", folderpath)

folder_final = r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\Code\ExcelMasaOutput"
csv_folder = r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\Code"
csv_file = r"Relacion.csv"
my_data = backend.readlines(os.path.join(csv_folder,csv_file))
splitted_data = []
for data in my_data:
	splitted_data.append(data.split(","))
for data in splitted_data:
	if str(data[0]) != "KodiUnik":
		try:
			backend.create_rel(str(data[0]), folder_final,str(data[9]),str(data[4]),str(data[5]),str(data[2]),str(data[3]))
			# backend.add_photos_to_rel(str(data[0]), folder_final) # not working
			backend.add_google_photos(str(data[0]), folder_final)
			backend.add_streetview_photos(str(data[0]), folder_final)
			backend.add_asig_photos(str(data[0]), folder_final)
			backend.add_other_photos(str(data[0]), folder_final)
			# backend.testgetimages(str(data[0]))
		except:
			print(str(data[0]) + " ---- nuk u kry!")


# backend.getwordstyles("140", folderpath)

# create_rel(kodi,folder,x,y,bashkia,qarku):
'''

from win32com import client
excel = client.Dispatch("Excel.Application")
word = client.Dispatch("Word.Application")
doc = word.Documents.Open("C:/word_file.docx")
book = excel.Workbooks.Open("C:/excel_file.xlsx")
sheet = book.Worksheets(1)
sheet.Range("A1:D20").Copy()
doc.Content.PasteExcelTable(False,False,False)

'''