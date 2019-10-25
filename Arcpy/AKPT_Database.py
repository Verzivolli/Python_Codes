tipologjite_arr = [['TH1','Struktura individuale (vila) te veçuara'],['TH2','Struktura individuale (vila) te ngjitura'],['TH3','Struktura individuale (vila) te grupuara'],['TH4','Struktura kolektive (pallat) te veçuara'],['TH5','Struktura kolektive (pallat) te ngjitura'],['TH6','Struktura kolektive (pallat) paralele'],['TH7','Struktura kolektive (pallat) te grupuara'],['TH8','Objekte industriale te veçuara'],['TH9','Tipologji te vecanta ne varesi te funksionit']]
sisteme_arr = [['UB', 'Urban'], ['U', 'Ujor'], ['B', 'Bujqesor'], ['N', 'Natyror'], ['IN', 'Infrastrukturor']]
fazat_arr = [['1', '0-3'], ['2', '4-6'], ['3', '7-9'], ['4', '10-12'], ['5', '13-15']]
kategori_arr = [['A','Banim'],['S','Shërbime'],['IE','Industri Ekonomi'],['IS','Institucione'],['AS','Arsim'],['SH','Shëndetësi'],['SHA','Aktivitete Shoqërore & Argëtimi'],['M','Monumente'],['ZU','Zona ushtarake '],['V','Varrezë'],['INT','Infrastrukturë Transporti'],['IEN','Infrastrukturë Energjitike'],['ITK','Infrastrukturë Telekomunikacioni'],['IUK','Infrastrukturë Ujësjellës - Kanalizime'],['IMB','Infrastrukturë Menaxhimi Mbetjesh'],['B','Tokë Bujqësore'],['IB','Infrastrukturë Bujqësore'],['EB','Ekonomi Bujqësore'],['BA','Bujqësi - Banim'],['N','Tokë Natyrore'],['NAR','Natyrë dhe Argëtim'],['U','Ujëra']]
nenkategori_arr = [['A1','Banim'],['A2','Banim dhe Shërbime'],['S1','Shërbime Akomodimi dhe Argëtimi'],['S2','Shërbime Tregtare dhe Biznese'],['IE1','Industri e Lehtë'],['IE2','Industri e Rëndë'],['IE3','Aktivitet Ekonomik Kompleks'],['IS2','Shërbim Publik'],['IS3','Shërbim Social'],['IS4','Shërbim Diplomatik'],['IS5','Institucione Financiare'],['IS6','Institucion Fetar'],['AS1','Arsim Parashkollor'],['AS2','Arsim i Ulët'],['AS3','Arsim i Mesëm'],['AS4','Arsim i Lartë'],['SH1','Shërbim Ambulator'],['SH2','Shërbim Spitalor'],['AR1','Hapësira Publike'],['AR2','Aktivitete Kulturore'],['AR3','Aktivitete Sportive'],['M1','Monument Kulture'],['ZU1','Infrastrukturë Ushtarake'],['V1','Varreza publike'],['V2','Varreza Dëshmorësh'],['V3','Memorial'],['INT1','Infrastrukturë Rrugore'],['INT2','Infrastrukturë Hekurudhore'],['INT3','Infrastrukturë Transporti Ujor'],['INT4','Infrastrukturë Transporti Ajror'],['INT5','Infrastrukturë Multimodale'],['IEN1','Elektike'],['IEN2','Hidrike'],['IEN3','Hidrokarbure'],['IEN4','Eolike'],['IEN5','Diellore'],['ITK1','Stacion telekomunikacioni'],['ITK2','Antena'],['IUK1','Ujësjellës'],['IUK2','Kanalizime'],['IMB1','Trajtim Mbetjesh'],['IMB2','Depozitim Mbetjesh'],['B1','Kultura të Përhershme'],['B2','Kultura Sezonale'],['B3','Tokë Djerrë'],['IB3','Infrastrukturë Vaditje dhe Kullimi'],['EB1','Struktura në Funksion të Bujqësisë'],['EB2','Struktura në Funksion të Blegtorisë'],['EB3','Agroturizëm'],['BA1','Bujqësi - Banim'],['N1','Pyje'],['N2','Kullotë'],['N3','Livadh'],['N4','Shkurre'],['N5','Tokë Pa Frut'],['NAR1','Park Natyror'],['NAR2','Plazh'],['NAR3','Shtigje'],['NAR4','Ekoturizëm'],['U1','Det'],['U2','Lagunë'],['U3','Kënetë'],['U4','Liqen'],['U5','Lumë'],['U6','Përrua'],['U7','Burim ujor']]


arcpy.env.overwriteOutput = True
arcpy.env.workspace = ws = r"F:\LOT 1\Ani\00 VauDejes\Faza3t\ArcMap\Output\Test\Per_Database_AKPT.gdb"

Njesite = "Njesite"
NjesiteC = "NjesiteCopy"
Sisteme = "Sistemet_Territoriale"

try:
	arcpy.CopyFeatures_management("Njesite", NjesiteC)
except arcpy.ExecuteError:
	print(arcpy.GetMessages(2))
	quit()
except Exception as e:
	print(e.message)
	quit()

float_codeblock = """
def to_float(num, errval):
	try:
		return float(num)
	except:
		return errval"""


int_codeblock = """
def to_int(num, errval):
	try:
		return int(num)
	except:
		return errval"""

def to_calc(newfield, oldfield, i, d_type, codeblock, function):
	field_name = newfield + "_" + str(i)
	search_field = oldfield + "_" + str(i)
	try:
		arcpy.AddField_management(NjesiteC, field_name, d_type)
		arcpy.CalculateField_management(NjesiteC, field_name, function+"(!"+search_field+"!, 0)", "PYTHON_9.3", float_codeblock)
	except:
		arcpy.AddField_management(NjesiteC, "temp_field", d_type)
		arcpy.CalculateField_management(NjesiteC, "temp_field", function + "(!" + search_field + "!, 0)", "PYTHON_9.3", float_codeblock)
		arcpy.DeleteField_management(NjesiteC, field_name)
		arcpy.AddField_management(NjesiteC, field_name, d_type)
		arcpy.CalculateField_management(NjesiteC, field_name, "!temp_field!", "PYTHON_9.3", "#")
		arcpy.DeleteField_management(NjesiteC, "temp_field")

# Sistemet_Territoriale


arcpy.Dissolve_management (NjesiteC, Sisteme, dissolve_field = "Sistemi", multi_part = "SINGLE_PART")
arcpy.AddField_management(Sisteme, "Lloji", "Text")
arcpy.CalculateField_management(Sisteme, "Lloji", "!Sistemi!", "PYTHON_9.3")
arcpy.DeleteField_management(Sisteme, "Sistemi")


arcpy.AddField_management(NjesiteC, "Bashkia", "Text")
arcpy.CalculateField_management(NjesiteC, "Bashkia", '"Vau-Dejës"', "PYTHON_9.3", "#")
# arcpy.DeleteField_management(NjesiteC, "Sistemi")
arcpy.AddField_management(NjesiteC, "Njësia", "Text")
arcpy.CalculateField_management(NjesiteC, "Njësia", "!KodiUnik!", "PYTHON_9.3")
arcpy.DeleteField_management(NjesiteC, "KodiUnik")
arcpy.AddField_management(NjesiteC, "Nr_Banorësh", "Short")
arcpy.CalculateField_management(NjesiteC, "Nr_Banorësh", "to_int(!Banorë!, 0)", "PYTHON_9.3", int_codeblock)
# arcpy.DeleteField_management(NjesiteC, "KodiUnik")
arcpy.AddField_management(NjesiteC, "Dendësia", "Double")
arcpy.CalculateField_management(NjesiteC, "Dendësia", "to_float(!Dendësi!, 0)", "PYTHON_9.3", float_codeblock)
# arcpy.DeleteField_management(NjesiteC, "KodiUnik")
arcpy.AddField_management(NjesiteC, "Temp", "Short")
arcpy.CalculateField_management(NjesiteC, "Temp", "to_int(!Vendparkime!, 0)", "PYTHON_9.3", int_codeblock)
arcpy.CalculateField_management(NjesiteC, "Vendparkime", "!Temp!", "PYTHON_9.3")
arcpy.DeleteField_management(NjesiteC, "Temp")
# arcpy.DeleteField_management(NjesiteC, "KodiUnik")
arcpy.AddField_management(NjesiteC, "Mënyra_e_ndërhyrjes", "Text")
arcpy.CalculateField_management(NjesiteC, "Mënyra_e_ndërhyrjes", "!Menyra_e_nderhyrjes!", "PYTHON_9.3")
for i in range(1, 6):
	t_field = "Përdorim_Specifik"
	field_name = t_field + "_" + str(i)
	arcpy.AddField_management(NjesiteC, field_name, "Text")
	arcpy.CalculateField_management(NjesiteC, field_name, '"-"', "PYTHON_9.3")
	to_calc("I", "Intensiteti", i, "Double", float_codeblock, "to_float")
	to_calc("Ksht", "KSHT", i, "Double", float_codeblock, "to_float")
	to_calc("Kshp", "KSHP", i, "Double", float_codeblock, "to_float")
	to_calc("Kshr", "KSHR", i, "Double", float_codeblock, "to_float")
	to_calc("Lartësia_Kate", "Lartesi_Kate", i, "Short", int_codeblock, "to_int")
	to_calc("Lartësia_Metra", "Lartesi_Metra", i, "Short", int_codeblock, "to_int")
	to_calc("Përqindja_e_Përdorimit", "Perqindjet_e_perdorimit", i, "Float", float_codeblock, "to_float")
	to_calc("Parcela_Minimale", "Sip_Min_Parc", i, "Double", float_codeblock, "to_float")

cursor = arcpy.da.UpdateCursor(NjesiteC, ["Sistemi"])
for row in cursor:
	for data in sisteme_arr:
		#Must use STR on real data when kodifinal is string
		if str(data[0]) == str(row[0]):
			row[0] = str(data[1])
	cursor.updateRow(row)
del cursor

for i in range(1, 6):
	field = "Kategori"
	field_name = field + "_" + str(i)
	cursor = arcpy.da.UpdateCursor(NjesiteC, [field_name])
	for row in cursor:
		for data in kategori_arr:
			if str(data[0]) == str(row[0]):
				row[0] = str(data[0]) + "." + str(data[1])
		cursor.updateRow(row)
	field = "Nënkategori"
	field_name = field + "_" + str(i)
	f2 = "Nenkategori"
	field_name2 = f2 + "_" + str(i)
	arcpy.AddField_management(NjesiteC, field_name, "Text")
	cursor = arcpy.da.UpdateCursor(NjesiteC, [field_name2, field_name])
	for row in cursor:
		for data in nenkategori_arr:
			if str(data[0]) == str(row[0]):
				row[1] = str(data[0]) + "." + str(data[1])
		cursor.updateRow(row)

field = "Tipologjia_Hapësinore"
arcpy.AddField_management(NjesiteC, field, "Text")
cursor = arcpy.da.UpdateCursor(NjesiteC, ["Tipologjia_hapsinore_1", field])
for row in cursor:
	for data in tipologjite_arr:
		if str(data[0]) == str(row[0]):
			row[1] = str(data[1])
	cursor.updateRow(row)

field = "Fazat_e_Zhvillimit"
field_name = field
f2 = "Fazat"
field_name2 = f2
arcpy.AddField_management(NjesiteC, field_name, "Text")
cursor = arcpy.da.UpdateCursor(NjesiteC, [field_name2, field_name])
for row in cursor:
	for data in fazat_arr:
		if str(data[0]) == str(row[0]):
			row[1] = str(data[0]) + "." + str(data[1])
	cursor.updateRow(row)




## Kufizime_Ligjore
# Përshkrim

## Arr Calc
# Sistemi
# Tipologjia_Hapësinore
# Fazat_e_Zhvillimit
## Iterator
# Kategori_1
# Nënkategori_1

## ITerator




####
# Done
###
# Përdorim_Specifik_1
# I_1 # Double # No null values
# Ksht_1
# Kshp_1
# Kshr_1
# Lartësia_Kate_1 # Short # no null
# Lartësia_Metra_1 # Short # no null
# Përqindja_e_Përdorimit_1
# Parcela_Minimale_1