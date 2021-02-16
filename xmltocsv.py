import xml.etree.ElementTree as ET
from random import sample
import csv

FILENAME = 'smiley_xml.xml'
BRANCHEKODER_WHITELIST = 'DD.56.10.99'
coords = [('bjerringbro', 56.3446694, 9.7106217, 0.05, 0.05),
          ('brande', 55.93161, 8.947574, 0.10, 0.10)]


tree = ET.parse(FILENAME)
root = tree.getroot()
rows = [r for r in list(root) if r[6].text.lower(
) == 'detail' and r[4].text.upper() == BRANCHEKODER_WHITELIST]

selected_rows = sample(rows, 20)

with open('sample.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  keys = [c.tag for c in list(selected_rows[0])]
  writer.writerow(keys)
  for row in selected_rows:
    values = [c.text for c in list(row)]
    writer.writerow(values)
