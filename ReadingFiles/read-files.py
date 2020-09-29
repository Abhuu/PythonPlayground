import json


def main():
    #read_csv_file()
    read_json_file()
    read_text_file()


def read_csv_file():
    print("-----------Reading from csv file--------------")
    with open('countries.txt', 'r') as reader:
        for line in reader:
            country_code, country_name = line.split("|")
            print("Country Code: {}\nCountry Name: {}".format(country_code, country_name.strip()))
    print("-------------End of CSV File----------------")


def read_json_file():
    print("-----------Reading from json file--------------")
    with open('countries.json', 'r') as reader:
        data = reader.read()
        json_data = json.loads(data)
        for country_detail in json_data:
            print("Country Code: {}\nCountry Name: {}".format(country_detail['abbreviation'], country_detail['country']))
    print("-------------End of JSON File----------------")


def read_text_file():
    print("-----------Reading from txt file--------------")
    with open('countries.txt', 'r') as reader:
        for line in reader:
            country_code, country_name = line.split("|")
            print("Country Code: {}\nCountry Name: {}".format(country_code, country_name.strip()))
    print("-------------End of TEXT File----------------")


if __name__ == '__main__':
    main()