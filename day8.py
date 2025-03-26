import string
import random
letters_l = string.ascii_lowercase
letters =list(letters_l)


def encrypt(msg,shift):
    en_msg =[]
    for i in range(len(msg)):
        if msg[i] in letters:
            ind = letters.index(msg[i])
            n_ind = ind+shift
            if n_ind<len(letters):
                en_msg.append(letters[n_ind])
            else:
                n_ind = (n_ind%26)
                en_msg.append(letters[n_ind])
        else:
            en_msg.append(msg[i])
    return ''.join(en_msg)

def decrypt(msg,shift):
    de_msg =[]
    for i in range(len(msg)):
        if msg[i] in letters:
            ind = letters.index(msg[i])
            n_ind = ind-shift
            if 0<=n_ind<len(letters):
                de_msg.append(letters[n_ind])
            else:
                n_ind = ((-1*n_ind)%26)
                de_msg.append(letters[-1*n_ind])
        else:
            de_msg.append(msg[i])
    return ''.join(de_msg)

if __name__=='__main__':
    con = 'yes'
    while con=='yes':
        en_de = input('Type "encode" to encrypt and "decode" to decrypt: ')
        text= input('Type your message:\n')
        shift = input('Type the shift number:\n')
        if en_de.lower()=='encode':
            print('Encoded message:')
            print(encrypt(text.lower(),int(shift)))
        elif en_de.lower()=='decode':
            print('Decoded message:')
            print(decrypt(text.lower(),int(shift)))
        else:
            print('Give proper encode/decode input..')
            continue
        con = input('Do you want to continue? Type "yes" or "no": ').lower()





