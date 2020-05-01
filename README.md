# ubucryptor
File encryptor and decryptor in Linux with Python. Using the same file extensions than Wannacry

## Usage

#### Encrypt files:

```
python enc.py $directory
```

#### Decrypt files:

```
python dec.py $directory
```

## Or create executable files

```
cat enc.py crypto.py >> temp_enc.py && pyinstaller -F temp_enc.py && rm temp_enc.py

cat dec.py crypto.py >> temp_dec.py && pyinstaller -F temp_dec.py && rm temp_dec.py
```

## Example

![Screenshot](https://i.imgur.com/undefined.png)


## Requirements

Python 2.x:

```
sudo pip install pyinstaller
```

Python 3.x:

```
sudo pip3 install pyinstaller
```

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)