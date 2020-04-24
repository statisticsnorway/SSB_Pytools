
import pandas as pd
import pyffx
from getpass import getpass

Enc_key = getpass('Enter Encryption key').encode()

def Encryption_numeric_ID(df, col, length, Enc_key=Enc_key):
    wrong_format = 0
    empty = 0
    key = Enc_key
    alphabet = '1234567890'
    e = pyffx.String(key, alphabet=alphabet,length=length)
    encryptet_col = []
    print(f'Encrypting: {col}')
    for i in df[col]:
        if len(str(i)) == 1:
            empty += 1
            encryptet_col.append(i)
        elif len(str(i))==length:
            x = e.encrypt(str(i))
            encryptet_col.append(x)
        else:
            wrong_length = len(str(i))
            error_alphabet = 'qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM1234567890_'
            error_e =pyffx.String(key, alphabet=error_alphabet,length=wrong_length)
            x = error_e.encrypt(str(i))
            encryptet_col.append(x)
            wrong_format += 1
    print(f'Number of values in {col} with the wrong format: {wrong_format}')
    print(f'Numert of entries without values in {col} : {empty}')
    return encryptet_col


def Decryption_numeric_ID(df, col, length, Enc_key=Enc_key):
    wrong_format = 0
    empty = 0
    key = Enc_key
    alphabet = '1234567890'
    e = pyffx.String(key, alphabet=alphabet,length=length)
    encryptet_col = []
    print(f'Encrypting: {col}')
    for i in df[col]:
        if len(str(i))==length:
            x = e.decrypt(str(i))
            encryptet_col.append(x)
        else:
            wrong_length = len(str(i))
            error_alphabet = 'qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM1234567890_'
            error_e =pyffx.String(key, alphabet=error_alphabet,length=wrong_length)
            x = error_e.decrypt(str(i))
            encryptet_col.append(x)
            wrong_format += 1
    print(f'Number of values in {col} with the wrong format: {wrong_format}')
    print(f'Numert of entries without values in {col} : {empty}')
    return encryptet_col

def Encryption_string(df, col, Enc_key=Enc_key):
    empty = 0
    key = Enc_key
    alphabet = 'qwertyuiopåasdfghjkløæzxcvbnmÅPOIUYTREWQÆØLKJHGFDSAMNBVCXZ -'
    encrypted_col = []
    for i in df[col]:
        if len(str(i)) == 1:
            empty += 1
            encryptet_col.append(i)
        else:
            words = str.split(i)
            Enc_sentance = []
            for word in words:
                e = pyffx.String(key, alphabet=alphabet, length=len(word))
                x = e.encrypt(word)
                Enc_sentance.append(x)
            encrypted_col.append(Enc_sentance)
    return encrypted_col


def Decryption_string(df, col, Enc_key=Enc_key):
    empty = 0
    key = Enc_key
    alphabet = 'qwertyuiopåasdfghjkløæzxcvbnmÅPOIUYTREWQÆØLKJHGFDSAMNBVCXZ -'
    encrypted_col = []
    for i in df[col]:
        decrypted_sentance = []
        for word in i:
            e = pyffx.String(key, alphabet=alphabet, length=len(word))
            x = e.decrypt(word)
            decrypted_sentance.append(x)
            
        sentance = ' '.join(word for word in decrypted_sentance)
        
        encrypted_col.append(sentance)
    return encrypted_col

def Encryption_num_adr(df, col, Enc_key=Enc_key, length=None):
    empty = 0
    key = Enc_key
    alphabet = 'qwertyuiopåasdfghjkløæzxcvbnmÅPOIUYTREWQÆØLKJHGFDSAMNBVCXZ0123456789'
    encrypted_col = []
    municipality = []
    for i in df[col]:
        municipality.append(i[:4])
        if set(i)=={'0'}:
            empty += 1
            encrypted_col.append(i)
        elif (length != None) & (len(i)!= length):
            i = i.ljust(length, '0')
            e = pyffx.String(key, alphabet=alphabet, length=len(i))
            x = e.encrypt(i)
            encrypted_col.append(x)
        else:
            e = pyffx.String(key, alphabet=alphabet, length=len(i))
            x = e.encrypt(i)
            encrypted_col.append(x)
    return encrypted_col, municipality

def Decryption_num_adr(df, col, Enc_key=Enc_key):
    empty = 0
    key = Enc_key
    alphabet = 'qwertyuiopåasdfghjkløæzxcvbnmÅPOIUYTREWQÆØLKJHGFDSAMNBVCXZ0123456789'
    encrypted_col = []
    municipality = []
    for i in df[col]:
        if set(i)=={'0'}:
            empty += 1
            encrypted_col.append(i)
        else:
            e = pyffx.String(key, alphabet=alphabet, length=len(i))
            x = e.decrypt(i)
            encrypted_col.append(x)
    return encrypted_col