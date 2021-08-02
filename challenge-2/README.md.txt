Challenge #2
Summary
We need to write code that will query the meta data of an instance within aws and provide a json formatted output. The choice of language and implementation is up to you.
 
Bonus Points
The code allows for a particular data key to be retrieved individually

Hints
· Aws Documentation
· Azure Documentation
· Google Documentation




The script must be run on the EC2 instance. You'll need to provide user input. When you run the script it'll list the keys defined in the metadata. You must provide the key UID to proceed. The script will retry on this step if you enter a UID that can't be found in the metadata. You'll then be shown the available key formats and must provide user input. After this step it will show you the key contents. 

To run the script use python 3.x
python -m pip install requests
python challenge-2.py