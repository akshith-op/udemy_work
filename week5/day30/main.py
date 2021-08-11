try:
    with open('data123.txt') as file:
        q = file.read()
        print(q)

except:
    with open('data123.txt', 'w') as file:
        file.write('Game of Thrones is the greatest series in the world')
else:
    print('Akshith')
finally:
    raise SyntaxError   
print('akshith')