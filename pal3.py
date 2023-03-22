def is_palindrome(s):
    return s == s[::-1]

def split_palindromes(word):
    n = len(word)
    
    if n < 3 or not is_palindrome(word):
        print("Impossible")
        return
    
    for i in range(1, n-1):
        if is_palindrome(word[:i]):
            for j in range(i+1, n):
                if is_palindrome(word[i:j]):
                    if is_palindrome(word[j:]):
                        print(word[:i])
                        print(word[i:j])
                        print(word[j:])
                        return
    
    print("Impossible")

word = input()
split_palindromes(word)
 
def der(word):
    for i in range(1,len(word)-1):
        if is_palindrome(word[:i]):
            for j in range(i+1,len(word)):
                if is_palindrome(word[i:j]):
                    if is_palindrome(word[j:]):
                        print(word[:i])
                        print(word[i:j])
                        print(word[j:])
                        return
    
#der written by me
der(word)