import requests
import re
from urllib import parse
import csv
import os

# with open("tel_shengshi.csv", "w", newline="") as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(("tel", "province", "city"))

f_01=open("tel_shengshi_detail.csv", "w", newline="")
csv_writer = csv.writer(f_01)
csv_writer.writerow(("tel", "name","parents","grade","nickname","province", "city"))

def query(tel):
    resq=requests.get("https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_name=guishudi&query=%s"%tel)
    # print(resq)
    content=resq.text
    # print(content)
    # print(resq.text)
    province=re.search('"prov":"(.*?)",',content)
    city=re.search('"city":"(.*?)",',content)
    # content=content.decode("gbk")
    # province=parse.unquote(province.group(1))
    # city=parse.unquote(city.group(1))
    return (province.group(1),city.group(1))
    # csv_writer.writerow((tel,province.group(1),city.group(1)))


if __name__ == '__main__':
    tel_arr_copy=[]
    i=1
    with open("tel_shengshi_detail.txt",encoding="utf-8-sig") as f:
        tel_arr=f.readlines()
        # print(tel_arr)
        for tel in tel_arr:
            tel_arr_02=tel.split("\t")
            tel_arr_02_copy=[]
            # print(tel_arr_02)
            telephone=tel_arr_02[0]
            # print(telephone)
            location = query(telephone)
            province=location[0]
            city=location[1]
            for info in tel_arr_02:
                info=info.strip()
                tel_arr_02_copy.append(info)
                # print(tel_arr_02_copy)
            tel_arr_02_copy.append(province)
            tel_arr_02_copy.append(city)
            # print(tel_arr_02_copy)
            csv_writer.writerow(tel_arr_02_copy)
            i+=1
            print(i)
    f_01.close()
        # print(type(tel_arr),len(tel_arr),tel_arr)
        # print(tel_arr)
    #     for  tel in tel_arr:
    #         tel=tel.strip()
    #         tel_arr2.append(tel)
    # print(tel_arr2)
    # for tel in tel_arr2:
    #     location=query(tel)
    # f.close()