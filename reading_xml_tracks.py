import xml.etree.ElementTree as ET

tree = ET.parse('Data/movienonoise4_Tracks_DM.xml')
root = tree.getroot()

t_list = []
for elem in root:
    myList = []
    for j in range(0, int(elem.get('nSpots'))):
        myList.append(
            (float(elem[j].get('t')), float(elem[j].get('x')), float(elem[j].get('y')), float(elem[j].get('z'))))

    t_list.append(myList)
