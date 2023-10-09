import xlrd
from xlrd import open_workbook

book = open_workbook("../resources/file_example_XLS_10.xls")
print(f"Количество листов {book.nsheets}")
print(f"Имена листов{book.sheet_names()}")
sheet = book.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(9, 3))
for rx in range(sheet.nrows):
    print(sheet.row(rx))

