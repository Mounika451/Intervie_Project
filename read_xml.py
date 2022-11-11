import json
from pymongo import MongoClient
import xmltodict
import os


client = MongoClient('mongodb://xxx:yyyy@00.00.00.00/?authSource=admin', 27017)

db = client["data_us"] 
collection = db["testing_xml_data_10112022"]
print("--------collection",collection)

cwd = os.getcwd()+"\PythonTask\Abc.xml"
with open(cwd) as xml_file:
     
    data_dict = xmltodict.parse(xml_file.read())
    # xml_file.close()
     
    # generate the object using json.dumps()
    # corresponding to json data
     
    json_data = json.dumps(data_dict)

json_data_fin=json.loads(json_data)
if "metar_report_by_region" in json_data_fin and "metar_reports" in json_data_fin["metar_report_by_region"] and len(json_data_fin["metar_report_by_region"]["metar_reports"])>0:
    final_data=json_data_fin["metar_report_by_region"]["metar_reports"]
    for record in final_data:
        print("---------",record)
        # collection.insert_one(record)
        # 
# print(type(json_data_fin),"------",json_data_fin)
# for report in json_data:
#    print("-----",report)
# print(json_data)