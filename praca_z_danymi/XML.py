#SAX is read-only, while DOM allows changes to the XML file.

from xml.dom import minidom

#otwieramy plik w parserze
DOMTree = minidom.parse('example_xml.xml')

#print(DOMTree.toxml())

new_value = "Tomek"

cNodes = DOMTree.childNodes

for i in cNodes[0].getElementsByTagName("osoba"):
    if(i.getElementsByTagName("imie")[0].childNodes[0].nodeValue == "Zygmunt"):
        i.getElementsByTagName("imie")[0].childNodes[0].nodeValue = new_value

tmp_config = 'C:\\Users\\MONIKA\\Desktop\\Programowanie_w_pythonie\\ProgrammingInPython\\praca_z_danymi\\xml_modified.xml'
f = open(tmp_config, 'w')
DOMTree.writexml( f )
f.close()