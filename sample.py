import xml.etree.ElementTree as ET
from random import sample
import json

FILENAME = 'smiley_xml.xml'
BRANCHEKODER_WHITELIST = 'DD.56.10.99'
coords = [('bjerringbro', 56.3446694, 9.7106217, 0.05, 0.05),
          ('brande', 55.93161, 8.947574, 0.10, 0.10)]


tree = ET.parse(FILENAME)
root = tree.getroot()
rows = [r for r in list(root) if r[6].text.lower(
) == 'detail' and r[4].text.upper() == BRANCHEKODER_WHITELIST]

for entry in coords:
    lat_lwr_bnd = entry[1] - entry[3]
    lat_upr_bnd = entry[1] + entry[3]
    lng_lwr_bnd = entry[2] - entry[4]
    lng_upr_bnd = entry[2] + entry[4]


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
        if not (lng_lwr_bnd < e_lng and e_lng < lat_lwr_bnd):
            continue
        newobj = {}
        for column in list(row):
            newobj[column.tag] = column.text
        result[row[0].text] = newobj

    print(f'{entry[0]}: {len(result.keys())}')
    curr_filename = f'data_{entry[0]}.json'

    with open(curr_filename, 'w') as outfile:
        json.dump(result, outfile, indent=2, sort_keys=True)
