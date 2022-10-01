def define_alphabet(c, alphabets):
    for alphabet in alphabets:
        if c in alphabet:
            return alphabet, alphabet.index(c)
    return None,None


def get_alphabet():
    en = [chr(c) for c in range(ord('a'),ord('z')+1)]
    EN = [c.upper() for c in en]
    ru = [chr(c) for c in range(ord('а'),ord('я')+1)]
    RU = [c.upper() for c in ru]
    return en, EN, ru, RU

def atbash_encode(string, alphabets):
    res = ''
    for c in string:
        alphabet, pos = define_alphabet(c, alphabets)
        res += c if alphabet is None else alphabet[len(alphabet)-pos-1]
    return res


def atbash_decode(string, alphabets):
    return atbash_encode(string, alphabets)

def caesar_encode(string, alphabets, key):
    res = ''
    for c in string:
        alphabet, pos = define_alphabet(c, alphabets)
        res += c if alphabet is None else alphabet[(pos+key) % len(alphabet)]
    return res

def caesar_decode(string, alphabets, key):
    return caesar_encode(string, alphabets, -key)



def main():
    alphabets = get_alphabet()

    string1 = 'Veni, vidi, vici!'
    caesar_enc = caesar_encode(string1, alphabets, 3)
    caesar_dec = caesar_decode(caesar_enc, alphabets, 3)

    string2 = 'Сохраняйте спокойствие'
    atbash_enc = atbash_encode(string2,alphabets)
    atbash_dec= atbash_decode(atbash_enc,alphabets)

    print('caesar encode:', caesar_enc)
    print('caesar decode:', caesar_dec)

    print('atbash encode:', atbash_enc)
    print('atbash decode:', atbash_dec)



if __name__ == '__main__':
    main()



