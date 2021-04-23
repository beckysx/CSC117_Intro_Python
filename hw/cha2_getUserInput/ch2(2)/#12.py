# Xu Song
# 1 Sep 2018
# Problem 12 Page 79

ps = (2000 * 40)  # paid for stock
pcb = (0.03 * ps)  # paid broker when bought
sa = (2000 * 43.75)  # sold stock
pba = (0.03 * sa)  # paid broker sold
lq = (sa - ps - pcb - pba)  # last question
print('Joe paid $', ps, 'for the stock.', '\nHe paid his broker $', pcb, 'when he bought the stock.',
      '\nJoe sold the stock for $', sa, '.\nHe paid his broker $', pba, 'when he sold the stock.')
print('At last, he remained $', lq, '.Joe made a profit!')
