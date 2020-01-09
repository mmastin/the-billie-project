import glob
import json

# read_files = glob.glob('*.json')
# with open('merged_lyrics.json', 'wb') as outfile:
#     outfile.write('[{}]'.format(
#         ','.join([open(f, 'rb').read() for f in read_files])))

result = []
for f in glob.glob('*.json'):
    with open(f, 'rb') as infile:
        result.append(json.load(infile))

with open('merged_lyrics.json', 'wb') as outfile:
    json.dump(result, outfile)