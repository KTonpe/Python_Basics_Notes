# regular expressions

import re
def check_find_iter():
    pattern = re.compile("ab")
    matcher = pattern.finditer("abaababa")
    print(matcher)
    for match in matcher:
        print(match.span())
        print(match.group())

def check_match_function():
    p ='abc'
    m = re.match(p,'dergfabc')
    if m  != None:
        print(m.group())
        print(m.span())
    else:
        print('not found')

def check_fullmatch():
    p ='abc'
    q= 'dergfabc'
    m = re.fullmatch(p,'dergfabc')
    print(m,type(m))
    if m  != None:
        print(f"{p} Full matched with 'dergfabc'")
    else:
        print('Not macthed')
    n = re.fullmatch(q,'dergfabc')
    print(n,type(n))
    if n != None:
        print(f"{q} Full matched with 'dergfabc'")
    else:
        print('Not macthed')

def check_slash_d_module_mobile_match():
    pattern = r"^[7-9]\d{9}" 
    conatct_number = input("Enter mobile number: ")
    matcher = re.fullmatch(pattern,conatct_number)
    if matcher!= None:
        print("Matched")
    else:
        print('Not macthed')

def replace_using_sub():
    t =re.subn("\D","#",'ab123cde4')
    print(t[0],t[1])

if __name__ == '__main__':
    menu ={
        '1': check_find_iter,
        '2': check_match_function,
        '3': check_fullmatch,
        '4': check_slash_d_module_mobile_match,
        '5': replace_using_sub,
    }
    while True:
        print("""
                   1. finditer
                   2. match
                   3. full match
                   4. slash d module Mobile Matched
                   5. replace using sub
                   e. exit
              """)
        choice = input("Enter your choice: ")
        menu[choice]() if choice in menu else print("Invalid choice")