# ragne 範圍
# python內驗空能: 清單產生器

import random # 載入隨機數

range(3) # [0, 1, 2] 包含開始值，但不包含結束值
range(2, 5) # [2, 3, 4]
range(2, 10, 3) # [2, 5, 8] 每次增加三

for i in range(10):
	print('hi') # hi X 10

for i in range(3):
	r = random.randint(1, 200) # 1到200隨機找三個數字，存到r
	print(r)