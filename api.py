from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from urllib.request import Request, urlopen
import json
import time
import requests
from kivy.network.urlrequest import UrlRequest
from functools import partial	
import urllib
from urllib.parse import urlparse


class pageLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ti_result = TextInput( multiline=False, font_size=14, size_hint=(0.2,0.2)) 
		self.btn_touchme = Button(text="Touch Me", font_size=16, size_hint=(1,0.4))
		self.btn_touchme.bind(on_press=self.callback) 
		# add_widgets on page
		self.add_widget(self.ti_result)
		self.add_widget(self.btn_touchme)		
	

	def callback(self, instance):
		#url_api = "http://172.18.14.23:4000/apitagsys/userDetails/2"
		url_api =  "http://172.18.14.23:4000/apitagsys/userLogin/morteza/Test@8521"
		#params = json.dumps({'@user_id': '1'})
		#params = urllib.urlencode({ "user_id" : "1" } )
		#header = {'Accept': 'application/json', 'Content-Type': 'application/json'	}
		header = {'Content-type': 'multipart/form-data','Accept': 'application/json'}
		req = UrlRequest(
					url_api,
					method = "GET",
					#req_body = params,	
					req_headers = header, 
					on_success=self.on_success_user_api,
					on_failure=self.on_failure_user_api,
					on_error=self.on_error_user_api,
				)

	def on_success_user_api(self, req, result):
		print('on_success_user_api')
		print(result)

	def on_failure_user_api(self,req, result):
		print('on_failure_user_api')
		print(result)

	def on_error_user_api(self,req, result):
		print('on_error_user_api')
		print(result)

		# req = UrlRequest(url, on_success, on_redirect, on_failure, on_error,
		# 				on_progress, req_body, req_headers, chunk_size,
		# 				timeout, method, decode, debug, file_path, ca_file,
		# 				verify)



	def OLDcallback(self, instance):
		pass
		# way 3
		# url = "http://172.18.14.23:3000/myapp/apiStudentDetails/8"
		"""
		url = "http://172.18.14.23:4000/apitagsys/apiUserDetails/2/"
		result = requests.get(url).json() 
		print(result) 
		"""
		
		# way 2
		"""
		url = "http://172.18.14.23:3000/myapp/apiStudentDetails/3"
		url = "http://172.18.14.23:4000/apitagsys/userDetails/2"
		headerValue = {'Accept': 'application/json', 'Content-Type': 'application/json'	}
		response = requests.get(url, headers=headerValue)
		result = json.loads(response.text) 
		self.ti_result.text = result['username']
		print(result) 
		"""
		
		# way 1
		"""
		req = Request("http://172.18.14.23:3000/myapp/apiStudentDetails/3")
		req.add_header('x-api-key', "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImpx")
		content = urlopen(req).read()
		result = json.loads(content)
		self.ti_result.text = result['family']
		print(result)
		"""

class MainApp(App):
	def build(self):
		return pageLayout()

if __name__ == "__main__":
	MainApp().run()
