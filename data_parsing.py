import xmltodict
import pprint
import json, csv, sys
import requests
import dicttoxml
import pandas as pandas


response_json = ''
"""Method that makes a JSON call"""
def json_call(response_json):
    country = input("Input a country name to get covid19 data:\n")
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"format":"undefined","name": country}
    headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "953fcaf3b5mshcce9e313ebbfc41p1ae5ffjsncb5d84292712"
            }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response_str = response.text
    response_json = json.loads(response_str)[0]
    return response_json

"""Method to save JSON to a file"""
def json_save_file(response_json):
    response_json = json_call(response_json)
    file_name = input('Write a JSON file name to be created: \n')
    with open(file_name+'.json', 'w') as jsfile:
        json.dump(response_json, jsfile)
    print('Saved as '+file_name+'.json\n')

"""Method to parse XML to JSON"""
def xml_to_json():
    file = input('Input an XML file name to parse:\n')
    with open(file) as f:
        doc = xmltodict.parse(f.read())
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(doc))


"""Method that parses JSON to XML"""
def json_to_xml(response_json):
    response_json = json_call(response_json)
    response_xml = dicttoxml.dicttoxml(response_json)
    print('The XML data: \n')
    print(response_xml)
    choice = int(input('Would you like to save the XML file locally?: \nPress 1 for YES \nPress 2 for NO\n'))
    xml_name = ''
    response_xml_str = str(response_xml)
    if choice == 1:
        xml_name = input('Name the xml file to be created: \n')
        with open(xml_name+'.xml', 'w') as f:
            f.write(response_xml_str)
            print('Saved as '+xml_name+'.xml\n')
    else:
        pass


"""Method to parse JSON to CSV"""
def json_to_csv():
    file_to_open = input('Write the name of the file to open:\n')
    with open (file_to_open, 'r') as json_file_open:
        json_file_text = json_file_open.read()
    json_file = json.loads(json_file_text)
    file_to_write = input('Name the file to be created:\n')
    with open(file_to_write+'.csv', 'w') as f:
        for key in json_file.keys():
            f.write("%s,%s\n"%(key,json_file[key]))
    print('Saved as '+file_to_write+'.csv\n')


def csv_to_json():
    file_to_open = input('Write the CSV file name to open:\n')
    data = {}
    with open(file_to_open) as csv_f:
        csvReader = csv.DictReader(csv_f)
        for row in csvReader:
           json.dump(row,file_to_open)
           file_to_open.write('\n')
    json_file = input('Write the name of JSON file to be created:\n')
    with open(json_file, 'w') as json_f:
        json_f.write(json.dumps(data, indent=4))
    print('Saved as '+json_file+'.json\n')

def xml_to_csv():
    pass

def csv_to_xml():
    pass

def json_to_xlsx():
    pass

def xlsx_to_json():
    pass

def xml_to_xlsx():
    pass

def xlsx_to_xml():
    pass

def csv_to_xlsx():
    pass

def csv_to_xml():
    pass

def main():
   """ print('\nJSON to XML:\n')
    json_to_xml(response_json)
    print('XML to JSON:\n')
    xml_to_json()
    print('\n\nSaving JSON file\n')
    json_save_file(response_json)
    print('\nParsing JSON to a CSV file\n')
    json_to_csv()"""
   print('\nParsing CSV to a JSON file\n')
   csv_to_json()
main()
