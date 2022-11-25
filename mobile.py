from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from urllib.request import Request, urlopen
import json
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString
import keyboard as Keyboard
import time
import sys

# class Enviroment():
# 	__last_chip__ = ""
# 	__loop__ = True

def nfc_reader(self, debug=True ,output=True, keyboard_output=False, set_timeout=120, set_cooldown = 3):
	"""
	Returns UID of NFC Chip/Card\n
	Set ouput to False if no output is required default is True \n
	debug -> def = True          | Output for errors etc. will be enabled \n
	output -> def = True         | Output for success/feedback etc. will be enabled \n
	keyboard_output -> def False | Types output like typing it \n
	set_timeout -> def 120/2min  | Sets timeout in seconds. Timeout for scan card. \n
	"""
	self.ti_result.text = "111"
	card_not_found = True
	while card_not_found:
		try:
			if output:
				#print("Waiting for Card..")
				self.ti_result.text = "Waiting for Card.."
			getuid=[0xFF, 0xCA, 0x00, 0x00, 0x00]
			act = AnyCardType()
			cr = CardRequest( timeout=set_timeout, cardType=act )
			cs = cr.waitforcard()
			cs.connection.connect()
			data, sw1, sw2 = cs.connection.transmit(getuid)
			data = toHexString(data)
			data = data.replace(" ", "")
			if data != "" and data != None and data != Enviroment.__last_chip__:
				card_not_found = False
				Enviroment.__last_chip__ = data
				if output:
					print(f"Success in reading chip..\nUID: {data}")
					self.ti_result.text = data
				if keyboard_output:
					if debug:
						#print("Output send to keyboard")
						self.ti_result.text = "Output send to keyboard"
					Keyboard.write(f"{data}")
				else:
					return data
				time.sleep(set_cooldown)
			cs=None
		except CardRequestTimeoutException:
			if debug:
				#print("Connection timed out... New request starting")
				self.ti_result.text = "Connection timed out... New request starting"
		except Exception as x:
			if debug:
				#print(f"Error: {x}")
				self.ti_result.text = x
					
class pageLayout(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ti_result = TextInput(hint_text="which button is click", multiline=False, font_size=14, size_hint=(1,0.3)) 
		self.add_widget(self.ti_result)
		nfc_reader(self, debug=True ,output=True, keyboard_output=False, set_timeout=120, set_cooldown = 3)

# def loop(debug=True ,output=True, keyboard_output=False, set_timeout=120, set_cooldown = 3):
#     """
#     Returns UID of NFC Chip/Card\n
#     Set ouput to False if no output is required default is True \n
#     Will be looped until Enviroment.__loop__ is False \n
#     debug -> def = True          | Output for errors etc. will be enabled \n
#     output -> def = True         | Output for success/feedback etc. will be enabled \n
#     keyboard_output -> def False | Types output like typing it \n
#     set_timeout -> def 120/2min  | Sets timeout in seconds. Timeout for scan card. \n
#     """
    
#     while Enviroment.__loop__:
#         nfc_reader(debug=debug ,output=output, keyboard_output=keyboard_output, set_timeout=set_timeout, set_cooldown = set_cooldown)

class MainApp(App):
	def build(self):
		return pageLayout()

if __name__ == "__main__":
	MainApp().run()