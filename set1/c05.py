#implementing repeating-key XOR

input_s = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"

def repeating_key_XOR(key_string : str, input_string : str) -> str:
    key_string_b = key_string.encode()
    input_string_b = input_string.encode()
    key_length = len(key_string_b)
    res = []
    for i,let in enumerate(input_string_b):
        key_index = i % key_length
        res.append(key_string_b[key_index] ^ let)
    return str(bytes(res).hex())

print(repeating_key_XOR("ICE", input_s))




