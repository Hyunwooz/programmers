list_person = [
    {'name': 'Taro', 'height': 170, 'weight': 60},
    {'name': 'Jiro', 'height': 180, 'weight': 80},
    {'name': 'Hanako', 'height': 160, 'weight': 50}
]

ret = next((index for (index, item) in enumerate(
    list_person) if item['name'] == 'Taro'), None)

print(ret)
