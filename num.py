import re

sentence = "this is alpha 5039 to 568"

# use regular expressions to extract all numbers in the sentence
numbers = re.findall('\d+', sentence)

print("The numbers in the sentence are:")
l=[]
for number in numbers:
    if "9" in number:
        continue
    else:
        l.append(number)
    
print(l)
