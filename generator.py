"""
pip install -r requirments.txt
"""

import pandas as pd
import json
class genetate():
    def __init__(self, filename="a.xlsx"):
        self.df = pd.read_excel(filename)
        self.json_data = json.loads(self.df.to_json())
        self.hour=-1
        self.oneday=-1
        self.oneweek=-1
        self.onemonth=-1
        self.threemonths=-1
        self.sixmonths=-1
        self.oneday=-1
        self.unknown=-1
    def filetype(self, money):
        money=float(money)
        if money==0.5:
            self.onehour+=1
            return "onehour", self.onehour
        if money==1:
            self.oneday+=1
            return "oneday", self.oneday
        if money==3:
            self.oneweek+=1
            return "oneweek", self.oneweek
        if money==10:
            self.onemonth+=1
            return "onemonths", self.onemonth
        if money==13:
            self.threemonths+=1
            return "threemonths", self.threemonths
        if money==23:
            self.sixmonths+=1
            return "sixmonths", self.sixmonths
        if money==35:
            self.oneyear+=1
            return "oneyear", self.oneyear
        else:
            self.unknown+=1
            return "unknown", self.unknown
    def main(self):
        json_data=self.json_data
        for i in zip(json_data[list(json_data)[3]].values(),json_data[list(json_data)[2]].values()):
            print(i)
            filetype=self.filetype(float(i[1]))
            with open(f"{filetype[0]}{filetype[1]}.txt", mode='x') as f:
                f.write(i[0])
                f.close()
        #print(a)
        print("Task Completed")
if __name__ == '__main__':
    filename=input("ExcelFileName: ")
    a=genetate("a.xlsx" if filename==""else filename)
    a.main()
