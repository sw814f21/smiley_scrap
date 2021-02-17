import xml.etree.ElementTree as ET
from random import sample
import json

FILENAME = 'smiley_xml.xml'
BRANCHEKODER_WHITELIST = 'DD.56.10.99'
coords = [('arden', 56.7692490644841, 9.86446022289761, 0.0134348306200351, 0.0254813301888905),
          ('loegstoer', 56.949546637211, 9.28228189977112,
           0.0703610531056427, 0.140620765468453),
          ('ranum', 56.8629514049343, 9.27041043335154,
           0.100397231514748, 0.223891956174242),
          ('als', 56.7507552082723, 10.2841983239859,
           0.0579528647824716, 0.120191995111888),
          ('oester-hurup', 56.8023111825913, 10.2683069334017,
           0.0410011446366454, 0.0644833661922952),
          ('ejstrupholm', 55.9907347931213, 9.27691434671396,
           0.0890878133514121, 0.15095645173127),
          ('naesbjerg', 55.6101769850203, 8.7050547566135, 0.044881561481958, 0.251878442978755)]

tree = ET.parse(FILENAME)
root = tree.getroot()
rows = [r for r in list(root) if r[6].text.lower(
) == 'detail' and r[4].text.upper() == BRANCHEKODER_WHITELIST]

for entry in coords:
    lat_lwr_bnd = entry[1] - entry[3]
    lat_upr_bnd = entry[1]
    lng_lwr_bnd = entry[2]
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
