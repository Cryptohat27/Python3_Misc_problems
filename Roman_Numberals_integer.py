"""
Roman Numberals to integer's"
"""

values = (('M',  1000),
         ('CM', 900),
         ('D',  500),
         ('CD', 400),
         ('C',  100),
         ('XC', 90),
         ('L',  50),
         ('XL', 40),
         ('X',  10),
         ('IX', 9),
         ('V',  5),
         ('IV', 4),
         ('I',  1))

def romantoint(year):
    result = 0
    l = []
    for i in range(len(year)):
        for letter, value in values:
            if year[i] == letter:
                l.append(value)
    l.append(0)
    for i in range(len(year)):
        if l[i] >= l[i+1]:
            result = result + l[i]
        else:
            result = result - l[i]
    return result
print(romantoint('XX'))
