import os
import csv

# dir=os.listdir("F:\氪涵外呼数据")
# print(len(dir))
# print(dir)
f=open("tel.csv","w",newline="")
csv_writer=csv.writer(f)
csv_writer.writerow(("tel",))
for dir in os.listdir("F:\氪涵外呼数据"):
    dir_list=dir.split(".")
    tel=dir_list[0]
    csv_writer.writerow((tel,))
    print(tel)

