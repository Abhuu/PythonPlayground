def main():
    read_text_file()


def read_text_file():
    print("-----------Reading file from txt file--------------")
    with  open('countries.txt', 'r') as reader:
        for line in reader:
            country_code, country_name = line.split("|")
            print("Country Code: {}\nCountry Name: {}".format(country_code, country_name.strip()))
    print("-------------End of File----------------")

if __name__ == '__main__':
    main()