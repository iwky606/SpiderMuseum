a = {
    "nihao": 1
}
print(a.get('nihao', None))
print(a.get("nnn", None))
a['nnn'] = 'nnn'
print('nnn' in a)
