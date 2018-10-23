# small town population is 1000
# every year it grows by 2% and 50 people move in
# how many years until it's 1200 people

p0 = 1000
percent = .02
aug = 50
p = 0
year = 1
#def nb_year(p0, percent, aug, p):
while p < 1200:
    p = p0 + p0 * percent + aug
    p0 = p
    if p >= 1200:
        break
    else:
        print(p)
        year = year + 1
print("The pupulation took ",year,"'s to get over 1200")
