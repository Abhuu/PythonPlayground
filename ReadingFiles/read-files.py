import json, yaml, sys


def main():
    switch_dict = {
        "0": exit_app,
        "1": read_csv_file,
        "2": read_json_file,
        "3": read_text_file,
        "4": read_yaml_file
    }

    while True:
        print('''
            0: "Exit Program"
            1: "Read CSV File"
            2: "Read JSON File"
            3: "Read TEXT File"
            4: "Read YAML File"
        ''')

        choice = input("Enter your choice ")
        if choice in switch_dict:
            switch_dict.get(choice)()


def exit_app():
    print("Exiting Application")
    sys.exit()

def read_csv_file():
    print("-----------Reading from countries.csv file--------------")
    with open('countries.txt', 'r') as reader:
        for line in reader:
            country_code, country_name = line.split("|")
            print("Country Code: {}\nCountry Name: {}".format(country_code, country_name.strip()))
    print("-------------End of CSV File----------------")


def read_json_file():
    print("-----------Reading from countries.json file--------------")
    with open('countries.json', 'r') as reader:
        data = reader.read()
        json_data = json.loads(data)
        for country_detail in json_data:
            print("Country Code: {}\nCountry Name: {}".format(country_detail['abbreviation'], country_detail['country']))
    print("-------------End of JSON File----------------")


def read_text_file():
    print("-----------Reading from countries.txt file--------------")
    with open('countries.txt', 'r') as reader:
        for line in reader:
            country_code, country_name = line.split("|")
            print("Country Code: {}\nCountry Name: {}".format(country_code, country_name.strip()))
    print("-------------End of TEXT File----------------")


def read_yaml_file():
    print("-----------Reading from countries.yaml file--------------")
    with open('countries.yaml', 'r') as reader:
        country_details = yaml.full_load(reader)
        #print(country_details)
        for placeholder, countries in country_details.items():
            for country_code, country_name in countries.items():
                print("Country Code: {}\nCountry Name: {}".format(country_code, country_name))
    print("-------------End of YAML File----------------")


if __name__ == '__main__':
    main()