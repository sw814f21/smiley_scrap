import xml.etree.ElementTree as ET
from random import sample
from util import sort_navnelbnr, xmlelement_to_dict
import json
import csv

FILENAME = 'smiley_xml.xml'
BRANCHEKODER_WHITELIST = 'DD.56.10.99'
SAMPLE_SIZE = 3
SPLITS = 2

tree = ET.parse(FILENAME)
root = tree.getroot()
rows = [r for r in list(root) if r[6].text.lower(
) == 'detail' and r[4].text.upper() == BRANCHEKODER_WHITELIST]

# From https://stackoverflow.com/a/312464

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


curr_arr = [xmlelement_to_dict(e) for e in list(root)]

selected_rows = sample(curr_arr, SAMPLE_SIZE * SPLITS)
split_data = list(chunks(selected_rows, SAMPLE_SIZE))

for i in range(len(split_data)):
    current_filename = f'data_random{i}.json'
    current_arr = split_data[i]
    sort_navnelbnr(current_arr)

    for data in split_data[i]:
        print(f'{i}: {data["navnelbnr"]}')

    with open(current_filename, 'w') as outfile:
        json.dump(current_arr, outfile, indent=2)
