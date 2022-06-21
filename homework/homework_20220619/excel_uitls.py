# -- coding: utf-8 --
# @Time : 2022/6/20 11:05
import xlrd, xlwt, os
excel_path = os.path.join(os.path.abspath(__file__), "../data/zentao_login_cookies.xlsx")
class ExcelUtils:
    def __init__(self, excel_path=excel_path):
        self.excel_path = excel_path

    def write_excel(self):
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('zentao_cookies')
        row_list = [["name", "value", "Domain", "path"],
                    ['zentaosid', 'l97vmm6ovptiq8c47s6unb2e31', '47.107.178.45', '/'],
                    ['theme', 'default', '47.107.178.45', '/zentao/www/'],
                    ['device', 'desktop', '47.107.178.45', '/zentao/www/'],
                    ['lang', 'zh-cn', '47.107.178.45', '/zentao/www/']]
        for i in range(0, len(row_list)):
            data = row_list[i]
            for j in range(0, len(data)):
                sheet.write(i, j,data[j])
        wb.save(self.excel_path)

    def read_excel(self):
        wk = xlrd.open_workbook(self.excel_path)
        sheet = wk.sheet_by_name("zentao_cookies")
        rows = sheet.nrows
        cols = sheet.ncols
        cookies_list = []
        for i in range(cols + 1):
            cookie_list = []
            for j in range(rows - 1):
                cookie_list.append(sheet.cell_value(i, j))
            cookies_list.append(cookie_list)
        return cookies_list

    def list_to_change_dic(self):
        c= []
        for i in range(0, 4):
            b = []
            for j in range (1,5):
             a = {self.read_excel()[0][j-1]: self.read_excel()[i+1][j-1]}
             b.append(a)
            c.append(b)
        return c

if __name__ == '__main__':
    ecl_util = ExcelUtils()
    ecl_util.write_excel()
    # ecl_util.read_excel()
    # for i in range(0,4):
    # print(ecl_util.list_to_change_dic())
