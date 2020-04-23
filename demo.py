import requests
import json
class RunMain:
	def __init__(self,url,method,data=None):
		self.res = self.run_main(url,method,data)

	def send_get(url,data):
		res = requests.get(url=url,data=data).json()
		return json.dumps(res,indent=2,sort_keys=True)

	def send_post(url,data):
		res = requests.post(url=url,data=data).json()
		return json.dumps(res,indent=2,sort_keys=True)

	def run_main(self,url,method,data=None):
		res=None
		url='http://127.0.0.1:8000/login'
		data = {
			'username':'222',
			'password':'111'
		}		if method == 'GET':
			res=self.send_get(url,data);
		else:
			res=self.send_post(url,data);
		return res
if __name__=='__main__':
	url='http://127.0.0.1:8000/login'
	data = {
		'username':'222',
		'password':'111'
	}
	run = RunMain(url,'GET',data)	
	#print run_main(url,'POST',data)