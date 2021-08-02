import json

def findValue(v1,v2,v3):
	with open('object.json') as object_file:
		data = json.load(object_file);
		item = data[v1][v2][v3]
		print("value = " + item)	

def splitKey():
	list = []
	key_file=open('key')
	key_items=key_file.read().split('/')
	for item in key_items:
		list.append(item)
	findValue(list[0],list[1],list[2])

if __name__ == '__main__':
    splitKey()