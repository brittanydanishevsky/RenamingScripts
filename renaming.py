import os
import xlrd

loc = "/Users/brittanydanishevsky/Desktop/rename.xlsx"

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

i = 0

for i in range(sheet.nrows):
    dst = "/Users/brittanydanishevsky/Desktop/Renamed/" + \
        sheet.cell_value(i, 1)
    src = "/Users/brittanydanishevsky/Desktop/Images/" + sheet.cell_value(i, 0)
    os.rename(src, dst)
    print(src + " has been changed to " + dst)
    i += 1
