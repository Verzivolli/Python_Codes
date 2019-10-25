
def read_lines(fname):
	with open(fname) as f:
		return f.read().splitlines()

def write_txt(fname,txt):
	with open("out1/GP_Largim_Lunj_GP_Minimale_2.csv","w+"):
		f.write(txt)

# import time # to set time in while loop
# # time.sleep(3000)

# current_mxd = arcpy.mapping.MapDocument("CURRENT")
# elm_list= arcpy.mapping.ListLayoutElements(current_mxd,"TEXT_ELEMENT")
# for elm in elm_list:
# 	eg = elm.fontSize
# 	elm.fontSize = eg * 1.5

# jupyter nbconvert my_notebook.ipynb --to html --CSSHTMLHeaderPreprocessor.enabled=True