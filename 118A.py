def convert_string(s):
    vowels = "AEIOUYaeiouy"
    result = ""
    
    for char in s:
        if char not in vowels:
            result += "." + char.lower()
 
    return result
 
s = input()

result = convert_string(s)
print(result)