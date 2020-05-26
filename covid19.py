import os
import csv
import requests

url = 'https://api.covid19india.org/state_district_wise.json'
headers = ['state/ut', 'cnfrmd', 'actv', 'rcvd', 'dcsd']
def get_covid_data(url):
    raw = requests.get(url)
    raw_dict = raw.json()
    working_path = "C:/Users/SAMIKSHA SENGAR/Documents/covid_india"

     #print(raw_dict)
    for state in raw_dict.keys():
        state_data = raw_dict[state]["districtData"]
        name = state.replace(' ', '_')+".csv"
        file_name = name + ".csv"
        file_path = os.path.join(working_path, file_name)
        with open(file_path, "w") as fp:
            csv_writer = csv.writer(fp)
            for key, value in state_data.items():
               temp_row = [key, value["confirmed"], value["active"], value["recovered"], value["deceased"]]
               csv_writer.writerow(headers)
               csv_writer.writerow(temp_row)


get_covid_data(url)
