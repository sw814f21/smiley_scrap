import xml.etree.ElementTree as ET
from random import sample
import json
import csv

FILENAME = 'smiley_xml.xml'
BRANCHEKODER_WHITELIST = 'DD.56.10.99'

tree = ET.parse(FILENAME)
root = tree.getroot()
rows = [r for r in list(root) if r[6].text.lower(
) == 'detail' and r[4].text.upper() == BRANCHEKODER_WHITELIST]



with open('smallcities.csv', newline='\n') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for entry in csv_reader:
        lat_lwr_bnd = entry[4]
        lat_upr_bnd = entry[2]
        lng_lwr_bnd = entry[3]
        lng_upr_bnd = entry[5]

        result = {}
        for row in rows:
            lng_txt = row[23].text
            if not lng_txt:
                continue
            lat_txt = row[24].text
            if not lat_txt:
                continue
            e_lng = float(lng_txt)
            e_lat = float(lat_txt)
            if not (lat_lwr_bnd < e_lat and e_lat < lat_upr_bnd):
                continue
            if not (lng_lwr_bnd < e_lng and e_lng < lng_upr_bnd):
                continue
            newobj = {}
            for column in list(row):
                newobj[column.tag.lower()] = column.text
            result[row[0].text] = newobj

        print(f'{entry[0]}: {len(result.keys())}')
        curr_filename = f'data_{entry[0]}.json'

        with open(curr_filename, 'w') as outfile:
            json.dump(result, outfile, indent=2, sort_keys=True)
