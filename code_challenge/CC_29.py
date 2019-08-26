import string

print("type the input: ")

a = input(">")
b=list(a)
c = list(dict.fromkeys(b))
d = len([int(s) for s in c if s.isdigit()])

invalidChars = set(string.punctuation.replace("_", ""))

if any(char in invalidChars for char in a):
    print(a, "=>","Error")

elif d > 0:
    print(a, "=>","Error")
    
else:
    i=1
    e=[]
    for x in c:
        e.append(i)
        i=i+1
        
    dictionary = dict(zip(e, c))
    reverse_subs = { v:k for k,v in dictionary.items()}

    converted_list=[reverse_subs.get(item,item)  for item in b]
    
    s = [str(y) for y in converted_list]  
    number = int("".join(s))
    
    print("".join(b), "->", number)