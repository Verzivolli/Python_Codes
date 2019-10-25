import os
folder = r"F:\Dropbox\Projekte UTS-01\DLDP - Venddepozitime\WM-20180411T124506Z-001\Ministria e Turizmit dhe Mjedisit-WM\PerDorezim"
paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk(folder)
        for filename in filenames)

for path in paths:
    # the '#' in the example below will be replaced by the '-' in the filenames in the directory
    newname = path.replace('__.pdf', '-preventiv nga MTM.pdf')
    if newname != path:
        os.rename(path, newname)