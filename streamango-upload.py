import requests, json, sys
try:
	import magic
except ModuleNotFoundError:
	print("Python magic is not installed. Use: \"sudo apt-get install python3-magic\" to install.")
	exit()

if len(sys.argv) != 2:
	print("Example usage: python3 streamango-upload.py file.mp4")
	exit()

headers = {'x-requested-with': 'XMLHttpRequest'}
uploadLink = requests.get('https://streamango.com/getUpload', headers=headers).text

mime = magic.Magic(mime=True)
files = {'f': (sys.argv[1], open(sys.argv[1],'rb'), mime.from_file(sys.argv[1]))}
print("Uploading..")
uploadResp = requests.post(uploadLink, files=files).text
result = json.loads(uploadResp)
try:
	if result['status'] == 200:
		print("Filename: {}\nSize: {} bytes\nSHA1: {}\nContent type: {}\n\nID: {}\nVideo URL: {}\n".format(result['result']['name'],result['result']['size'],result['result']['sha1'],result['result']['content_type'],result['result']['id'],result['result']['url']))
except:
	print("Some error occured!")
	print(result)
