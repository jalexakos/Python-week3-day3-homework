# Create a function that given a string remove the vowels in the string and return the string.
# Example Input: “Joel”
# Example Output: “Jl”

def remove_vowels(str1):
    s_list = []
    l_1 = []
    i = 0
    while i < len(str1):
        s_list.append(str1[i])
        i+=1
    for letter in s_list:
        if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u":
            l_1.append(letter)
    answer = "".join(l_1)
    print(answer)

remove_vowels("Joel")
remove_vowels("Josh")