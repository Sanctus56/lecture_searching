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


def pattern_search(sequence, searched_pattern):
    pattern_length = len(searched_pattern)
    list_of_positions = []
    number_of_operations = 0
    for position in range(len(sequence) - pattern_length):
        is_same = True
        for subind in range(len(searched_pattern)):
            number_of_operations = number_of_operations + 1
            if sequence[position+subind] == searched_pattern[subind]:
                is_same = is_same and True
            else:
                is_same = is_same and False
                # Break
        if is_same:
            list_of_positions.append(position+pattern_length //2)
    print(number_of_operations)
    return {'positions': list_of_positions, 'count': len(list_of_positions)}









def main():
    sequential_data = read_data("sequential.json", "dna_sequence") #upravit field podla toho co hladam
    print(sequential_data)
    print(linear_search(sequential_data, 0))
    print(pattern_search(sequential_data, "ATA"))
    pass




if __name__ == '__main__':
    main()