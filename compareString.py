def compare_strings(str1, str2):
    if id(str1)==id(str2):
        return 0
    elif str1 > str2:
        return 1
    else:
        return -1

str1 = "212.21.12.13"
  
str2 = "212.23.13.13"
print(compare_strings(str1,str2))
