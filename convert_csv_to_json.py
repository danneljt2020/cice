import csv, json

with open("municipios.csv", mode="r", encoding="utf8") as file:
    csv_reader = list(csv.reader(file, delimiter=";"))
    header = csv_reader[0]
    data = csv_reader[1:]
    data_json = {'municipios':[]}
    for row in data:
        json_format={}
        for k,v in zip(header,row):
            json_format[k]=v
        data_json['municipios'].append(json_format)

with open('nuevo.json','w') as json_file:
    json.dump(data_json,json_file)





