
# with open("task1.txt", "r") as file:
        # dict_key: dict
        # i = 0
        # for line in file:
        #     if i == 1:
        #         a = file.readline()
        #         b = file.readline()
        #         dict_key[a] = b
        #         i = i - 1
        #     elif i == 0:
        #         b = file.readline()
        #         a = file.readline()
        #         dict_key[a] = b
        #         i = i + 1
        # print(dict_key)


        # for line in file:
        #     a = file.readline()
        #     a = a.replace("\n", '')
        #     print(a)


# with open(r"task2", "rb") as task_2:
#     x = pickle.load(task_2)
#     print(x)
#     mean_of_numbers = sum(x) / len(x)
# print(mean_of_numbers)


import openpyxl
class ExcelDoc(object):
    def __init__(self, path):
        self.excel_file = path
        self.reserve_file = openpyxl.load_workbook(self.path)

    def __enter__(self):
        return self.excel_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.excel_file.save(self.path)
            self.excel_file.close()
        else:
            print("\nYou have error")
            self.excel_file.close()
            return True


with ExcelOpen("Excel.xlsx") as excel_file:
    first_sheet = excel_file.active
    text = first_sheet.cell(row=1, column=1)
    print(first_sheet["A1"].value)
    text.value = '11111'
