## grab input file
## parse each line and decode each line to bytes
## run the XOR check for each line
## the one that we have decrypted should have the highest score
## print it


def decrypt_XOR(encrypted_string:bytes):
    decrypted_and_score = {}
    for ch in range(256):
        res = []
        score = 0
        for val in encrypted_string:
            new_char = val^ch
            res.append(new_char)
            if ((new_char == 32) 
                or (new_char in range(65,91)) 
                or (new_char in range(97,123))):
                score += 1
        decrypted_and_score[ch] = (score, bytes(res))
    high_score = float('-inf')
    max_message = b''
    for score,mes in decrypted_and_score.values():
        if score > high_score:
            high_score = score
            max_message = mes
    return (high_score,max_message)

messages_and_scores = []

with open('c04input.txt', 'r',encoding='utf-8') as file:
    for line in file:
        clean_line = line.strip()

        if not clean_line:
            continue
        clean_line_b = bytes.fromhex(clean_line)
        messages_and_scores.append(decrypt_XOR(bytes(clean_line_b)))

print(max(messages_and_scores))
        




