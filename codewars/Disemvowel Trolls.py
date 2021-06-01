def disemvowel(string_):
    vowels = ['a','e','i','o','u']
    for i in string_:
        if i in vowels or i.lower() in vowels:
            string_ = string_.replace(i,'')
    return string_
print(disemvowel('This website is for losers LOL!'))
print(3**0.5)