def xor(a, b): 
   
    # initialize result 
    result = [] 
   
    # Traverse all bits, if bits are 
    # same, then XOR is 0, else 1 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result.append('0') 
        else: 
            result.append('1') 
   
    return ''.join(result) 
   
   
# Performs Modulo-2 division 
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
   
# Function used at the receiver side to decode  
# data received by sender 
def decodeData(data, key): 
   
    l_key = len(key) 
   
    # Appends n-1 zeroes at end of data 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
   
    return remainder 
  
file = open("data", "r") 
data = file.read() 
print(data) 

  
key = "1001"
ans1 = decodeData(data, key) 
print("Remainder after decoding is->"+ans1) 
      
    # If remainder is all zeros then no error occured 
temp = "0" * (len(key) - 1) 
if ans1 == temp: 
        print (data)
 