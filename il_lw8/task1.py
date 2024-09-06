import xmltodict

fin = open('10-2.osm', 'r', encoding='utf-8')
dct = xmltodict.parse(fin.read())
fin.close()

nodeDict = {}
wayDict = {}
typeDict = {}
acc = 0.001

for node in dct['osm']['node']:
    node_id = node['@id']
    nodeDict[node_id] = node

for way in dct['osm']['way']:
    way_id = way['@id']
    wayDict[way_id] = way

benchCounter = 0
benchBusStops = 0
justBench = 0
benchCounterNearPharmacy = 0

for node in dct['osm']['node']:
    if 'tag' in node and isinstance(node['tag'], list):
        flag1 = 0
        for tag in node['tag']:
            if tag['@k'] == 'bench':
                benchCounter += 1
                benchBusStops += 1
            if flag1 == 1:
                typeDict.setdefault(str(f"{tag['@k']}.{tag['@v']}"), 0)
                typeDict[str(f"{tag['@k']}.{tag['@v']}")] += 1
            if tag['@k'] == 'amenity' and tag['@v'] == 'bench':
                flag1 = 1
                benchCounter += 1
                justBench += 1

    elif 'tag' in node and isinstance(node['tag'], dict):
        if node['tag']['@k'] == 'bench' or (node['tag']['@k'] == 'amenity' and node['tag']['@v'] == 'bench'):
            benchCounter += 1
            justBench += 1

for node in dct['osm']['node']:
    latB = 0
    lonB = 0
    if 'tag' in node and isinstance(node['tag'], list):
        for tag in node['tag']:
            if tag['@k'] == 'bench' or (tag['@k'] == 'amenity' and tag['@v'] == 'bench'):
                latB = float(node['@lat'])
                lonB = float(node['@lon'])

                for node1 in dct['osm']['node']:
                    latP = 0
                    lonP = 0
                    if 'tag' in node1 and isinstance(node1['tag'], list):
                        for tag1 in node1['tag']:
                            if (tag1['@k'] == 'amenity' and tag1['@v'] == 'pharmacy'):
                                latP = float(node1['@lat'])
                                lonP = float(node1['@lon'])


                    elif 'tag' in node1 and isinstance(node1['tag'], dict):
                        if (node1['tag']['@k'] == 'amenity' and node1['tag']['@v'] == 'pharmacy'):
                            latP = float(node1['@lat'])
                            lonP = float(node1['@lon'])

                    if ((abs(latB - latP) < acc) and (abs(lonB - lonP) < acc)):
                        benchCounterNearPharmacy += 1

    elif 'tag' in node and isinstance(node['tag'], dict):
        if node['tag']['@k'] == 'bench' or (node['tag']['@k'] == 'amenity' and node['tag']['@v'] == 'bench'):
            benchCounter += 1
            justBench += 1

print(f"Total benches: {benchCounter}")
print(f"Just benches: {justBench}\nBenches at bus stops: {benchBusStops}")
print(f"Benches near pharmacy: {benchCounterNearPharmacy}")
print(typeDict)
