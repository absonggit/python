import csv

path = r"csv01.csv"
class csvFile(object):
    def __init__(self, path):
        self.path = path
        self.infoList = []
    def readCsv(self):
        with open(self.path, "r") as f:
            for row in csv.reader(f):
                self.infoList.append(row)
        return self.infoList

    def writeCsv(self, data):
        print(data)
        with open(self.path, "a", newline='') as f:
            writer = csv.writer(f)
            for rowData in data:
                writer.writerow(rowData)

c = csvFile(path)
c.writeCsv([['4', 'ddd', '44']])
print(c.readCsv())