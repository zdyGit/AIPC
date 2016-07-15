from xml.etree import ElementTree as ET


def GetKeyValue(keyName):
	tree = ET.parse("source.xml")
	root = tree.getroot()

	baseDataNode = root.find("BaseData")
	for node in baseDataNode:
		if node.tag.lower() == keyName.lower():
			return node.text

	baseDataNode = root.find("LastData")
	for node in baseDataNode:
		if node.tag.lower() == keyName.lower():
			return node.text 

def SetKeyValue(keyName,value):
	tree = ET.parse("source.xml")
	root = tree.getroot()

	baseDataNode = root.find("LastData")
	for node in baseDataNode:
		if node.tag.lower() == keyName.lower():
			node.text = str(value)

	tree.write("source.xml")
