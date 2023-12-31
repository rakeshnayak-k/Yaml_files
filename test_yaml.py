import yaml
import json


with open('first.yml','r') as file:
    try:
        print(yaml.safe_load(file))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    stream = open("sample.yml", 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    try:
        for key, value in dictionary.items():
            print (key + " : " + str(value))
        json_data_string = json.dumps(dictionary)
        # print(json_data_string)
    except Exception as e:
        print("e",e)