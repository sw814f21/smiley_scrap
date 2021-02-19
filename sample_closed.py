import re
import subprocess
import json

FIRST_COMMIT = '0ded3034c1bf2add232fc4cba5dfbb72398a0d7b'
FILENAME = 'smiley_json.json'

def process_match(match):
    return int(match.group(1))


cmd = ['git', 'diff', '--no-color', '--patch', f'{FIRST_COMMIT}..HEAD', FILENAME]
result = subprocess.run(cmd, stdout=subprocess.PIPE)
resultstr = result.stdout.decode('utf-8')

regex = re.compile(r'-\s+"navnelbnr": "(\d+)",')
closed_entrynos = regex.findall(resultstr)


cmd = ['git', 'show', f'{FIRST_COMMIT}:{FILENAME}']
result = subprocess.run(cmd, stdout=subprocess.PIPE)
resultstr = result.stdout.decode('utf-8')

first_smiley_data = json.loads(resultstr)

closed_data = [first_smiley_data[entry] for entry in closed_entrynos]

with open('data_closed.json', 'w') as outfile:
    json.dump(closed_data, outfile, indent=2)
    
