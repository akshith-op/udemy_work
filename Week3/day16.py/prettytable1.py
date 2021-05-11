from prettytable import PrettyTable

table = PrettyTable()
table.add_column('pokemon_name',['Pikachu'," ",'Squirtle'," ",'Charmender'])
table.add_column('Type',['Lightning'," ",'Water'," ","Fire"])
table.align = 'l'
print(table)