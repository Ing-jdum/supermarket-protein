from itertools import combinations_with_replacement
from collections import Counter
import json
import os

# Your data
my_dict = {
    "pork": 270,
    "chicken": 474,
    "egg": 148.2,
    "tuna": 181.25,
    "turkey": 154,
    "canned_tuna": 71.76
}


def combine(arr):
    return [x for x in combinations_with_replacement(arr, 7) if (max(Counter(x).values()) <= 2)]


def compress_tuple(tuple_values):
    tuple_counts = Counter(tuple_values)
    result_dict = {key: tuple_counts[my_dict[key]] for key in my_dict}
    return result_dict


def convert_to_notion_format(input_list: list):
    database_id = os.getenv("DB")
    output_list = []
    for input_dict in input_list:
        cluster_list = []
        for item, quantity in input_dict.items():
            if quantity > 0:
                formatted_item = {
                    "parent": {"type": "database_id", "database_id": database_id},
                    "properties": {
                        "Name": {
                            "type": "title",
                            "title": [{"type": "text", "text": {"content": item}}],
                        },
                        "Quantity": {"type": "number", "number": quantity},
                    },
                }
                cluster_list.append(formatted_item)
        output_list.append(cluster_list)
    return output_list


def write_data_to_file(data: list, filename: str):
    json_data = json.dumps(data, indent=2)
    with open(filename, 'w') as json_file:
        json_file.write(json_data)


data = combine(list(my_dict.values()))
compressed_data = [compress_tuple(tuple_values) for tuple_values in data]
notion_data = convert_to_notion_format(compressed_data)
write_data_to_file(notion_data, 'notion_data.json')

