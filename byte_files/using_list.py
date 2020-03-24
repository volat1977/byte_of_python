shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен сделать', len(shoplist), 'покупок')

print('Покупки', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно  купить  риса')
shoplist.append("рис")
print('Теперь мой список покупок  товаров таков:', shoplist)

print("Отсортирую я  свой список")
shoplist.append('рис')

print("Отсортируя  я свой список")
shoplist.sort()
print("отсортированный  список выглядит так", shoplist)

print('Первой что мне  нужно  купить, это',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой  список покупок', shoplist)

