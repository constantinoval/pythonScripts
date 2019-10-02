import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='json file with tasks')
rez = parser.parse_args()
tasks = json.load(open(rez.input))

for task in tasks['tasks']:
    exec(open('solve.py').read(), {'task': task})
    exec(open('plot.py').read(), {'task_name': task['name']})
    exec(open('rez_to_doc.py').read(), {'task': task, 'doc_path': tasks['doc_path']})
