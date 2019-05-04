from util.opera_excel import OperaExcel

class ConfigData:
    def __init__(self,filename=None):
        self.filename = filename
        self.op = OperaExcel(self.filename)

    def get_data_for_excel(self):
        num = self.op.row_count()
        #data = []
        # for i in num:
        #     data.append(self.op.row_data(i))
        data = [self.op.row_data(i) for i in range(num)]
        return data

if __name__ == "__main__":
    c = ConfigData()
    print(c.get_data_for_excel())