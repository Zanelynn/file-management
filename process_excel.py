import pyexcel
import sys

def process_excel_file(filename):
    sheet = pyexcel.get_sheet(file_name=filename)
    for i in range(6, 1000):
        data = sheet.row[i]
        if data[0] == '':
            break
        print sheet.row[i]

if __name__ == '__main__':
    process_excel_file(sys.argv[1])
