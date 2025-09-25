def strength(passwords):
    ans = []
    for p in passwords:
        if p == "" or p.isalpha() or len(p) < 8:
            ans.append("weak")
        elif len(p) >= 12:
            ans.append("strong")
        else:
            ans.append("ok")
    return ans

print(strength(["abc", "School2025", "L3arn!ngAI2025"]))

print(strength(["12345", "abcdefg"])) 

print(strength(["helloworld", "PythonRocks"])) 

print(strength(["abc12345", "Password1", "Hello2025"])) 

print(strength([""])) 
