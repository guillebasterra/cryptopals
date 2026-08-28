#write a function that takes two equal-length buffers and produces their XOR combination


#iirc XOR means that both inputs are different

#conver the decimal numbers into binary and compare each corresponding bit


def fixed_XOR(s1:str,s2:str) -> bytes:
    bytes1 = hex_to_bytes(s1)
    bytes2 = hex_to_bytes(s2)
    res = []
    for a,b in zip(bytes1,bytes2):
        res.append(a^b)
    return bytes(res)

def hex_to_bytes(hex_string:str)->bytes:
    return bytes.fromhex(hex_string)


input1 = "1c0111001f010100061a024b53535009181c"
input2 = "686974207468652062756c6c277320657965"
out = bytes.fromhex("746865206b696420646f6e277420706c6179")


print(fixed_XOR(input1,input2))

print(fixed_XOR(input1,input2) == out )

b = fixed_XOR(input1, input2)
print(b)          # b"the kid don't play"   ← repr, characters
print(list(b))    # [116, 104, 101, 32, ...] ← the actual ints
print(b[5])       # 100                       ← indexing gives int
print(b.hex())    # '746865206b6964...'       ← ints as hex pairs
