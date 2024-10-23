text = 'Clarusway'
text[3]
text[4:7]
text[6:]
text[0:6]
text[:6]

text = 'Clarusway'
text[1:8]
text[1:8:2]
text[1::3]
text[::2]
text[5:1]
text[5:1:-1]
text[5:1:-2]
text[::-1]

print("python candir"[2:10:2])

text = 'kayak'
print(text == text[::-1])

yeni_text = 'abcdef'

print(yeni_text == yeni_text[::-1])

print(yeni_text[::-1])

city = 'Phoenix'
print(city[1:])
print(city[:6])
print(city[::2])
print(city[1::2])
print(city[-3:])
print(city[::-1])

text= 'Clarusway'
text[-1]
text[8] == text[-1]

animal = "hippopotamus"

print(animal[1:])
print(animal[:6])
print(animal[::2])
print(animal[1:7:2])
print(animal[-3:])
print(animal[::-1])

text = 'Clarusway'
print(text[:4] + text[-3:])
print(text[:5] + 'k' + text[-3:])
print(text[:5] + 'k' + text[6:])

print(len(text))

print(text, 'kelimesinin uzunlugu' ,len(text))

a = 5 
a = a + 1
print(a)

name = 'Yasin'
print("Merhaba , %s" % name)

name = 'ali'
age = 43.5
meslek = 'Content Creator'
print('Merhaba, ismin {}, yasin {} meslegin ise {}'.format(name,age,meslek))
print('Merhaba, ismin {a}, yasin {b} meslegin ise {c}'.format(b =age, c=meslek, a=name))

print(f"merhaba benim adim {name} yasim {age} meslegim {meslek}")

name = "MARIAM"
print(f'My name is {name.capitalize()}')
print(f'saga hizalama {name:>20}')
print(f'saga hizalama {name:<20}')
print(f'saga hizalama {name:*^20}')

name = 'Susan'
age = 'young'
gender = 'lady'
school = 'CLRWY IT university'

output = (
    f"{name} is a {age}"
    f"{gender} and she is a student"
    f"at the {school}"
)
print(output)