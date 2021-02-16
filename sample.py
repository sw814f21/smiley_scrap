import xml.etree.ElementTree as ET
from random import sample
import json

FILENAME = 'smiley_xml.xml'
SAMPLE_SIZE = 50
FILES = 4
OUTPUT = 'sample'
BRANCHEKODER_WHITELIST = 'DD.56.10.99'


tree = ET.parse(FILENAME)
root = tree.getroot()
rows = [r for r in list(root) if r[6].text.lower(
) == 'detail' and r[4].text.upper() == BRANCHEKODER_WHITELIST]

selected_rows = sample(rows, SAMPLE_SIZE * FILES)

result = []
for row in selected_rows:
    newobj = {}
    for a in list(row):
        newobj[a.tag] = a.text
    result.append(newobj)

start = 0
for i in range(FILES):
    curr = f'sample{i}.json'
    end = i * SAMPLE_SIZE + SAMPLE_SIZE + 1
    currarr = result[start:end]
    start = end
    print("Start:" + str(start) + " End: " + str(end))
    with open(curr, 'w') as outfile:
        json.dump(currarr, outfile, indent=2, sort_keys=False)
