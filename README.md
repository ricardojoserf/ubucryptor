# ubucryptor
Trying to replicate (~) Wannacry encrypting in Ubuntu


## Usage

Encrypt files:

*python enc.py $directory*

*./enc_exe $directory*


Decrypt files:

*python dec.py $directory*

*./dec_exe $directory*



## Requirements

sudo pip install pyinstaller



## Creating the executable

cat enc.py crypto.py >> test.py

pyinstaller -F test.py



## Example of usage

![Screenshot](images/ubucryptor.png)
