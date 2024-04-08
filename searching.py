import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data_file:
        data = json.load(data_file)
    return data[field]



def linear_search(sequence, number):
    """
    Sus
    """
    list = []
    pocet = 0
    slovník = {'positions': 0, "count": 0}
    for i in range(len(sequence)):
        if sequence[i] == number:
            list.append(i)
            pocet = pocet + 1
    slovník['positions'] = list
    slovník['count'] = pocet

    return slovník


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 0))
    pass




if __name__ == '__main__':
    main()