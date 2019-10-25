import pandas
import os
folder = "testingData"
csv_file = "perrel.csv"

df = pandas.read_csv(os.path.join(folder,csv_file))