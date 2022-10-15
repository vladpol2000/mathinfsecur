def encrypt_gamma(text, gamma):
    alphabet = [chr(c) for c in range(ord('а'), ord('я') + 1)]
    key = (gamma*(len(text)//len(gamma)+1))[:len(text)]
    ind_text = []
    ind_key = []
    res_index = []
    res = ''
    for c in text:
        for l in alphabet:
            if c == l:
                ind_text.append(alphabet.index(l))
    for k in key:
        for z in alphabet:
            if k == z:
                ind_key.append(alphabet.index(z))
    for i in range(len(text)):
        res_index.append((ind_text[i] + ind_key[i]) % 33 + 1)
    for v in res_index:
        res += alphabet[v].upper()
    return res

def decrypt_gamma(text, gamma):
    alphabet = [chr(c) for c in range(ord('а'), ord('я') + 1)]
    key = (gamma*(len(text)//len(gamma)+1))[:len(text)]
    ind_text = []
    ind_key = []
    res_index = []
    res = ''
    for c in text:
        for l in alphabet:
            if c == l:
                ind_text.append(alphabet.index(l))
    for k in key:
        for z in alphabet:
            if k == z:
                ind_key.append(alphabet.index(z))
    for i in range(len(text)):
        res_index.append(ind_text[i]  - (ind_key[i] % 33) - 1)
    for v in res_index:
        res += alphabet[v].upper()
    return res

print(encrypt_gamma('приказ', 'гамма'))
print(decrypt_gamma('усхчбл', 'гамма'))