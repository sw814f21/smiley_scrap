import xml.etree.ElementTree as ET
from random import sample
import json


FILENAME = 'smiley_xml.xml'
OUTPUT = 'smiley_json.json'

tree = ET.parse(FILENAME)
root = tree.getroot()

result = {}
for row in list(root):
  newobj = {}
  for column in row:
    newobj[column.tag] = column.text
  key = row[0].text
  result[key] = newobj

with open(OUTPUT, 'w') as outfile:
  json.dump(result, outfile, indent=2, sort_keys=True)