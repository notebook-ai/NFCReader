from smartcard.Exceptions import NoCardException
from smartcard.System import readers
from smartcard.util import toHexString
import sys

# detect nfc reader (1)
found = False
reader = ''
for reader in readers():
    if reader:
        found = True
        break
if found == True:
    #print(type(reader))
    print(reader)
else:
    print("Not found nfc reader")
