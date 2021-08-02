import requests
from requests.structures import CaseInsensitiveDict

def getToken():
		url = "http://169.254.169.254/latest/api/token"
		headers = CaseInsensitiveDict()
		headers["X-aws-ec2-metadata-token-ttl-seconds"] = "21600"
		headers["Content-Length"] = "0"
		resp = requests.put(url, headers=headers)
		return resp.content.decode('utf-8')

def listKeys():
		url = "http://169.254.169.254/latest/meta-data/public-keys"
		headers = CaseInsensitiveDict()
		headers["X-aws-ec2-metadata-token"] = getToken()
		resp = requests.get(url, headers=headers)
		print("Listing available keys:")
		print(resp.content.decode('utf-8'))
		return resp.status_code
		
def getKeyFormat(uid):
		url = "http://169.254.169.254/latest/meta-data/public-keys/" + uid
		headers = CaseInsensitiveDict()
		headers["X-aws-ec2-metadata-token"] = getToken()
		resp = requests.get(url, headers=headers)
		print("Listing available key formats:")
		print(resp.content.decode('utf-8'))
		return resp.status_code
		
def getKey(uid,format):
		url = "http://169.254.169.254/latest/meta-data/public-keys/" + uid + "/" + format
		headers = CaseInsensitiveDict()
		headers["X-aws-ec2-metadata-token"] = getToken()
		resp = requests.get(url, headers=headers)
		print("Getting key content:")
		print(resp.content.decode('utf-8'))
		return resp.status_code

if __name__ == '__main__':
		statusCode = 0
		while statusCode != 200:
			statusCode = listKeys()
		statusCode = 0
		while statusCode != 200:
			uid = input("Enter key UID:")
			statusCode = getKeyFormat(uid)
		statusCode = 0		
		while statusCode != 200:
			format = input("Enter key format:")
			statusCode = getKey(uid,format)