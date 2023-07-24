from licensing.models import *
from licensing.methods import Key, Helpers
from easygui import enterbox

# message to be displayed
text = "Introduzca su clave de producto:"

# window title
title = "zeroTwo [johanmess]"

# creating a enter box
output = enterbox(text, title)

# creating a message
clave = str(output)


RSAPubKey = "<RSAKeyValue><Modulus>07BZbKLxSrKJIBWAyAgCsjFrS9ncKGnOxTZarF9FjwjxSQex/ZOjSke/b5sL7q7nU/McjdxC80Q1QWu2nXmMBzW+9KuXtHGFXXRVq3VrCt/OMiCet0b55pG9+HDArFHfv5mNp0lJ+gWbLu2IkpkGPUoiDnrpQ5ylrsO2I6akN8WOGhEYg0pAfPaGUJ4g69kPaHckw9t8A0rOdnpgYe/k7Q6F5X+svlrP00OspJ9eMDYzoaqe3iqmbx75ssqNVJuwzetYfynNve40SZbBqVsZ2PD5ISLmuP5L/42ENuQfeIfPiTofvZa61TH0KKvE6tkNoPoR3DjONkdqLDPhn/kuPQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI1NTIzODk5OCIsImJBUnBDR2ZqZlloMkhQaitCbDE2Lzh4d3JzSHVIWWk4U2xidHU2Sy8iXQ=="

result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=21037, \
                   key=clave,\
                   machine_code=Helpers.GetMachineCode(v=2))

if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
    quit()
else:
    from zeroTwo import coco
    coco()
    