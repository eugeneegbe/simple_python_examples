# write a python script to check if a string is a palindrom

def check_palindrome(string):
    size = len(string)
    j = size - 1
    i = 0
    result = True
    while i <= size / 2:
        print(string[i], string[j])

        if string[i] is not string[j]:
            result = False
        i += 1
        j -= 1

    return result


string = 'saippuakivikauppias'
print(check_palindrome(string))


# A palindrome is a word spelled the same way in the reverse
# For example "level"
# iterate over the arrray and stop when in the middle and str[i] == str[j]
# output check to be true
# else it is false
# Given the above example the output is True
# Note: This solution has a complexity of O(n) as it has to go through n number of elements