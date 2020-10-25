import xlrd
from win10toast import ToastNotifier


def workbook_data(file_name):
    """打开Excel文件并读取数据"""
    list_all_data = []
    workbook = xlrd.open_workbook(file_name)
    all_sheet = workbook.sheet_names()
    for i in all_sheet:
        list_data = []
        dict_data = {}
        sheet = workbook.sheet_by_name(i)
        if sheet.nrows > 0:
            for j in range(1, sheet.nrows):
                list_data.append(sheet.row_values(j))
        dict_data["deviceId"] = i
        dict_data["data"] = list_data
        list_all_data.append(dict_data)
    return list_all_data

def workbook_sheet(file_name):

    workbook = xlrd.open_workbook(file_name)
    all_sheet = workbook.sheet_names()
    return all_sheet

# print(workbook_data(R'C:\Users\admin\Desktop\device.xlsx'))
# print(workbook_sheet(r'C:\Users\admin\Desktop\device.xlsx'))
