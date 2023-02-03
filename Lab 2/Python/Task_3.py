
my_str = "Swagat Panda"
code = []
binary_rep =[]
# Coding the string in binary
for i in my_str:
    code.append(ord(i))
    binary_rep.append(bin(ord(i)).replace("0b", ""))

binary_str = [''.join(i) for i in [binary_rep]]

decode = [chr(j) for j in code]
dec_str = [''.join(i) for i in [decode]]

print(code)
print(binary_rep)
print(binary_str[0])
print(dec_str[0])

