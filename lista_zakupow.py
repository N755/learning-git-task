my_dict = {
    "Пекарня": ['Хліб', 'Пончик', 'Булки'],
    "Продуктовий": ['Морква', 'Селера', 'Рукола']
}

for k in my_dict:
  print(f"Я йду до {k.upper()} і купую там: ", ', '.join([w.upper() for w in my_dict[k]]))
print(f"Всього разом я купую: {sum(len(val) for val in my_dict.values())} продуктів")