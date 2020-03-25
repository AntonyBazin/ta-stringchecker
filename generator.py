from strgen import StringGenerator
import random as rn
from re import sub


def generate_string(amount):
    for _count in range(amount):
        result = StringGenerator(r'<-[!\l]{1}[\l0-9]{0:15}').render()
        for i in range(rn.choice(range(5))):
            variable = StringGenerator(r'[!\l]{1}[\l0-9]{0:15}').render()
            operator = StringGenerator(r'[\&\|^]').render()
            result += (operator + variable)
        result += '#'
        yield result


def damage_string(s, key=0):
    if not key:
        return s[1:]
    elif key is 1:
        return sub(r'-', '0', s)
    elif key is 2:
        return sub(r'[&|^]', '0', s)
    elif key is 3:
        return s.replace('#', '0', 1)


if __name__ == '__main__':
    errors = 0
    with open('data.txt', 'w') as dt:
        for c in generate_string(1000000):
            if rn.choice([True, False]):
                c = damage_string(c, rn.choice(range(4)))
                errors += 1
            dt.write(c + '\n')
    print(errors)
