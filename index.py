def decode_text(text, code):
    reverse_code_map = {v: k for k, v in code.items()}
    
    decoded_text = ""
    buffer = ""
    
    for bit in text:
        buffer += bit
        if buffer in reverse_code_map:
            decoded_text += reverse_code_map[buffer]
            buffer = ""
    
    return decoded_text

code1 = {
    '_' : '00',
    'A' : '11',
    'B' : '0100',
    'C' : '10111',
    'E' : '10000',
    'G' : '10001',
    'H' : '01011',
    'L' : '10110',
    'M' : '01010',
    'N' : '10101',
    'R' : '1001',
    'S' : '011',
    'T' : '10100'

}

text1 = "110100100111010111101010001100011111010110100110010111101101110011100100011101101110000"



decoded_text = decode_text(text1, code1)
print(decoded_text)
