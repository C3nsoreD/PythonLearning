a = b'h\x65llo'
print(list(a))


## Str and Bytes

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str  # Instance of str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str  # Instance of bytes
    return value


## TEST 
print(repr(to_str(b'hello')))
print(repr(to_str('hello')))

# compare bytes to strings 
assert b'foo' > b'fo'  # Returns true
# assert b'hello' > 'hello'  # returns an error

## writing to file 
# writing and reading binary data requires the appropriate mode i.e. wb, rb
with open('file.bin', 'w') as f:  # fix me: w -> wb
    f.write(b'\xf1\xf2\xf3\xf4\xf5')  # returns error, why?

with open('file.bin', 'r') as f:
    data = f.read()

assert data == b'\xf1\xf2\xf3\xf4\xf5'  # compare binary