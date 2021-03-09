import string as str

a = 42
b = 3.14
"""
s = '%d:%f' %(a,b)
#s = '{1}:{0}'.format(a, b)
#s = f'{a}:{b}'


print(s)

print(len(s.ascii_letters))
print(s.ascii_lowercase)
print(s.ascii_uppercase)
print(s.digits)
print(s.hexdigits)

a = '2cd'
b = 'abcdabcdab'
c = '23425'

print(a in b)
print(b.count(a))
print(b.find(a))
print(a.isalnum())
print(b.isalpha())
print(c.isdigit())
print(c.isidentifier())
print(b.islower())
print(b.isupper())


lul = ';'.join(['a','b', 'c', 'd'])
print(lul)
print(lul.split(';', 2))
print(lul.rsplit(';', 2))
a = '==a==='
print(a.strip('='))

print([i*i for i in range(10) if (i>5)])
"""

number = '+7(985)990-70-45'
digits = '0123456789'
russian_numbers = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
stroka = ''




stroka = [stroka + russian_numbers[digits.find(c)] for c in number if (c.isdigit())]
stroka = ' '.join(stroka)

print(stroka)




def transliteration(line):
    result = ''
    for i in line:
        result = result + translit[russian_letters.find(i)]
    return result

def FIO_Form(FIO):
    result = FIO[0]
    for word in FIO[1:]:
        result = result + word[0]
    return result


russian_letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя "
translit = ['a','b','v','g','d','e','zh','z','i','y','k','l','m','n',
            'o','p','r','s','t','u','f','kh','ts','ch','sh','shch','"','y',"'",
            'eh','yu','ya', ' ', '-']

w = open ('e-mails.txt', 'w')

f = open('data.txt', 'r')
for line in f:
    line = line.lower()
    line = transliteration(line)
    FIO = line.split(' ')
    w.write(FIO_Form(FIO) + '@bmstu.ru\n')

f.close()
w.close()
"""

s = "jwkgiuwbgiwigno"
for i in s:
    print(i + ',')
    
"""
