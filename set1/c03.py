input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

input_b = bytes.fromhex(input)

#naive - xor against every character and find the message


def fixed_XOR(s1:str,s2:str) -> bytes:
    bytes1 = hex_to_bytes(s1)
    bytes2 = hex_to_bytes(s2)
    res = []
    for a,b in zip(bytes1,bytes2):
        res.append(a^b)
    return bytes(res)

def hex_to_bytes(hex_string:str)->bytes:
    return bytes.fromhex(hex_string)

def looped_XOR()-> dict:
    decrypted_and_score = {}
    for ch in range(256):
        res = []
        score = 0
        for val in input_b:
            new_char = val^ch
            res.append(new_char)
            if ((new_char == 32) 
                or (new_char in range(65,91)) 
                or (new_char in range(97,123))):
                score += 1
        decrypted_and_score[ch] = (score, bytes(res))
    return decrypted_and_score

decrypted_and_score = looped_XOR()
high_score = float('-inf')
max_message = b''
for score,mes in decrypted_and_score.values():
    if score > high_score:
        high_score = score
        max_message = mes
print(max_message)
print(input_b)
