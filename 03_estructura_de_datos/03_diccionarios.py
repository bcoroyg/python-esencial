# Declarar un diccionario con Notacion Literal
rae = {}
rae['pizza'] = 'La comida mas deliciosa del mundo.'
print(rae)

rae['pasta'] = 'La comida mas sobrosa de italia.'

print(rae)

print(rae['pizza'])
print(rae['pasta'])

# Error ⇒ KeyError: 'helado'
# print(rae['helado'])

print(rae.get('helado', None))

a = rae.get('helado', None)
print(a)

a = rae.get('pizza', None)
print(a)

print('keys() ⇒',rae.keys())
print('values() ⇒',rae.values())
print('items() ⇒',rae.items())

print('for keys()')
for key in rae.keys():
    print(key)

print('for values()')
for value in rae.values():
    print(value)

print('for items()')
for key, value in rae.items():
    print(key, value)
