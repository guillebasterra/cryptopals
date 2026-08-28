## might be hex -> binary -> base64
import base64
def hex_to_bytes(s: str) -> bytes:
    return bytes.fromhex(s)

def bytes_to_b64(b: bytes) -> bytes:
    return base64.b64encode(b)

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

exp_output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

hex_bytes = hex_to_bytes(hex_string)
b64_bytes = bytes_to_b64(hex_bytes)

print(b64_bytes)
print(b64_bytes.decode()==exp_output)


       


