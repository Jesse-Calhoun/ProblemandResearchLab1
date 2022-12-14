new_string = ""
string = "aaabrraaaccccaaadddddaaabrra"
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count = count + 1
    else:
        new_string += str(count) + string[i]
        count = 1
new_string += str(count) + string[i+1]
print()
print(new_string)
print()
