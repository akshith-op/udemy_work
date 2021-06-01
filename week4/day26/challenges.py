numbers = [1,1,2,3,5,8,13,21,34,25]

#challenge - 1
sqr_numbers = [idx **2 for idx in numbers]
print(sqr_numbers)

#challenge - 2

even_numbers = [xdi for xdi in numbers if xdi % 2 == 0]
print(even_numbers)