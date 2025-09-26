def strength(passwords):
    ans = []
    for p in passwords:
        test1=0
        test2=0
        test3=0
        if p == "" or p.isalpha() or len(p) < 8:
            ans.append("weak")
        elif len(p)>= 12:
            for i in p:
                if i.isalpha():
                    test1 = 1
                if i.isdigit():
                    test2 = 1
                if not i.isalnum():
                    test3 =1
            if (test1 == 1 and test2 == 1 and test3 == 1):
                ans.append("strong")
        # and not p.isalnum() and p.upper() and p.lower():
           
        else:
            ans.append("ok")
    return ans

print(strength(["abc", "School2025", "L3arn!ngAI2025"]))

print(strength(["12345", "abcdefg"])) 

print(strength(["helloworld", "PythonRocks"])) 

print(strength(["abc12345", "Password1", "Hello2025"])) 

print(strength([""])) 

print(strength(["onlyletters", "Mix123", "GoodOne2023!", "Ultra$trongP@ssw0rd2025"])) 
