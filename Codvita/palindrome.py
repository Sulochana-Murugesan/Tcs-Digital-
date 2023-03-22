
def ispalindro(word):
    if word==word[::-1]:
        return True
    else:
        return False

def pal(word):
    n=len(word)
    for i in range (1,n-1):
       if ispalindro (word[:i]):
           for j in range(i+1,n-1):
             if ispalindro(word[i:j]):
                if ispalindro(word[j:]):
                    print(word[:i])
                    print(word[i:j])
                    print(word[j:])
                    return

word=input()
pal(word)                
               
