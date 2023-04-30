import hashlib
def get_hash(data="python"):
    encode_str = data.encode()
    s_256 = hashlib.sha3_256(encode_str)
    return s_256.hexdigest()

get_hash('test')
