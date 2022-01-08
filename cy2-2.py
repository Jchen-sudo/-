def check(s: bytes):
	padding = s[-s[-1]:]
	for i in padding:
		if i != len(padding):
			return False
	return True
  
print(check(b'ICE ICE BABY\x04\x04\x04\x04'))
print(check(b'ICE ICE BABY\x05\x05\x05\x05'))
print(check(b'ICE ICE BABY\x01\x02\x03\x04'))
print(check(b'ICE ICE BABY'))