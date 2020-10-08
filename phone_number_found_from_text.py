def isPhoneNumber(text):
	if len(text) != 11:
		return False
	for i in range(0,11):
		if not text[i].isdecimal():
			return False
	return True



msg = 'call me at  019'
for i in range(len(msg)):
	chunk = msg[i:i+11]
	if isPhoneNumber(chunk):
		print(f'phone number found {chunk}')


print('not found')



