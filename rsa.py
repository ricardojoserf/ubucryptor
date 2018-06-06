import Crypto
from Crypto.PublicKey import RSA


class RSACipher(object):

	def encrypt(self, message):
		f = open('public.pem', 'rb')
		publickey = RSA.importKey(f.read())
		encrypted = publickey.encrypt(message, 32)
		return encrypted

	def decrypt(self, enc_message):
		f = open('private.pem', 'rb')
		private = RSA.importKey(f.read())
		decrypted = private.decrypt(enc_message)
		return decrypted

'''
message ='aaaaaaaaaaaa'
enc = RSACipher().encrypt(message)
print enc
dec = RSACipher().decrypt(enc)
print dec
'''
