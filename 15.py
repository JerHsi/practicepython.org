S = input("Enter a string:")

S_list = S.split(" ")

#print(S_list)
reverse_list = S_list[::-1]
r_str = ""
for i in range(len(reverse_list)):
  r_str += reverse_list[i] + " "
print(r_str)
