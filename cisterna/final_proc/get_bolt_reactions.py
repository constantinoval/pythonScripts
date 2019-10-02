import odbAccess
import re
import json
pattern = re.compile(r'SOF(\d).*H(\d+)')
odb=session.odbs.values()[0]
step=odb.steps.values()[0]
reactions = {}
for hr in step.historyRegions.values():
    for k, v in hr.historyOutputs.items():
        search_rez = pattern.search(k)
        if not search_rez:
            continue
        dof, hole_number = search_rez.groups(0)
        hole_name = 'H{}'.format(hole_number)
        if not hole_name in reactions:
            reactions[hole_name] = [0,0,0]
        reactions[hole_name][int(dof)-1] = hr.historyOutputs[k].data[-1][-1]
json.dump(reactions, open('bolts.json', 'w'))
# hr=step.historyRegions.values()[0]
# hr.historyOutputs.keys()
# ho=hr.historyOutputs.values()[0]
# ho.data
