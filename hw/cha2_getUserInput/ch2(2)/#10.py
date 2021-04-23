# Xu Song
# 1 Sep 2018
# Problem 10 on page 78

cn = int(input('How many cookies do you want to make?'))
s = float(1.5 / 48 * cn)
ns = round(s, 2)
b = float(1 / 48 * cn)
nb = round(b, 2)
f = float(2.75 / 48 * cn)
nf = round(f, 2)
print('To make ', cn, ' cookies,you need:\n', ns, 'cups of sugar\n', nb, 'cups of butter\n', nf, 'cups of flour')
