odb=session.odbs.values()[0]
exclLabs=[]
for i in range(4):
	name='CLOUD_NODES-FASTENERS-{}'.format(i+1)
	ns=odb.rootAssembly.nodeSets[name].nodes
	for n in ns:
	    if n[0].instanceName=='BOCHKA_FULL-1':
	        break
	for nn in n:
	    exclLabs.append(nn.label)
elLabs=[]
dopN=[]
es=odb.rootAssembly.instances['BOCHKA_FULL-1'].elementSets['UBKA'].elements
for e in es:
    nns=e.connectivity
    c=0
    for n in nns:
        if n in exclLabs:
            c+=1
    if c>=3:
        dopN+=list(nns)
    if not c:
        elLabs.append(e.label)
els=odb.rootAssembly.instances['BOCHKA_FULL-1'].ElementSetFromElementLabels(name='UBKA-FAST', elementLabels=elLabs)

elLabs=[]
dopN=[]
es=odb.rootAssembly.instances['BOCHKA_FULL-1'].elementSets['USIL'].elements
for e in es:
    nns=e.connectivity
    c=0
    for n in nns:
        if n in exclLabs:
            c+=1
    if c>=3:
        dopN+=list(nns)
    if not c:
        elLabs.append(e.label)
els=odb.rootAssembly.instances['BOCHKA_FULL-1'].ElementSetFromElementLabels(name='USIL-FAST', elementLabels=elLabs)
