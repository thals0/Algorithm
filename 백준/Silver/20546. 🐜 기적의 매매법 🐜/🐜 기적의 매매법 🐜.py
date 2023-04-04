money = int(input())
stocks = list(map(int, input().split()))

def bnp():
  left_money = money
  cnt = 0
  for stock in stocks:
    cnt += left_money // stock
    left_money = left_money % stock
    if left_money == 0:
      break
  return left_money, cnt

def timing():
  left_moeny = money
  cnt = 0
  for i in range(len(stocks)-4):
    if stocks[i] < stocks[i+1] < stocks[i+2] < stocks[i+3]:
      left_moeny += cnt * stocks[i+3]
      cnt = 0
    if stocks[i] > stocks[i+1] > stocks[i+2] > stocks[i+3]:
      cnt += left_moeny // stocks[i+3]
      left_moeny = left_moeny % stocks[i+3]
  return left_moeny, cnt

bnp_money, bnp_stock = bnp()
total_bnp_money = bnp_money + bnp_stock * stocks[-1]
timing_money, timing_stock = timing()
total_timing_money = timing_money + timing_stock * stocks[-1]

if total_bnp_money < total_timing_money:
  print('TIMING')
elif total_bnp_money > total_timing_money:
  print('BNP')
else:
  print('SAMESAME')