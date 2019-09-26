import os
import os.path
import xlrd

from os import path

loc = "/Users/brittanydanishevsky/Desktop/rename.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

i = 0
x = 0

for i in range(sheet.nrows):
    src = "/Users/brittanydanishevsky/Desktop/Images/" + sheet.cell_value(i, 0)

    if (path.exists(src) == False):
        print(src + " does not exist")
        x = x + 1

    i += 1

print(str(x) + " files do not exist")
