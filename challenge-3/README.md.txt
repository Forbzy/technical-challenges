Challenge #3
We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.

 
Example Inputs
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
 
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a
 
Hints
We would like to see some tests. A quick read to help you along the way


for item in data['object']:
    print object['object']
	
	
	
	
The script reads the data in the `key` file and separates the letters using the delimiter `/`. It then creates an array containing the letters. It then reads the JSON data into an JSON object from the `object.json` file and uses the letters from the key as variables to access the value.

To run the script use python 3.x
python challenge-3.py