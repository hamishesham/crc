def xor(a, b): 

	result = [] 

	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 

	return ''.join(result) 
def mod2div(divident, divisor): 
	pick = len(divisor) 
	tmp = divident[0 : pick] 

	while pick < len(divident): 

		if tmp[0] == '1': 

			 
			tmp = xor(divisor, tmp) + divident[pick] 
		else: 
			tmp = xor('0'*pick, tmp) + divident[pick]  
		pick += 1

	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 

	checkword = tmp 
	return checkword 

def encodeData(data, key): 

	l_key = len(key) 

	# Appends n-1 zeroes at end of data 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 

	# Append remainder in the original data 
	codeword = data + remainder 
	return codeword	 
	
input_string = raw_input("Enter data you want to send->") 
#s.sendall(input_string) 
data =(''.join(format(ord(x), 'b') for x in input_string)) 
print (data) 
key = "1001"

ans = encodeData(data,key) 
file=open('data','a')
file.write(ans)
file.close()
print(ans)  
