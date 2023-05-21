


# using while function.

'''
while True:
	
	name = input('請輸入你的名字：  ')

	if name == 'q':
		print ('you can leave now')
		break
	else:
		print ('you cannot leave')

python3 password_test.py
'''


'''
true_password 放左 loop 外運算會較簡潔
思考，chance 減少，應在哪個行動後發生
chance 減少，應在輸入錯誤後發生，不是在每次輸入後發生。這確保輸入正確後，不會減少chance。

每次輸入password後，最先要驗證的，應該是password是否正確
之後才到其他行動

chance 每次減少，最先驗證的，應該是chance 是否已到0，到0要有相應行動。
未到0， 就給回應，再行loop。

每個if 的最後，留一個else，比較清晰齊整

'''

'''
true_password = 'alan'

chance = 2

print('你有 ', chance, ' 次輸入密碼機會')

while chance >= 0:

	password = input('請輸入密碼：  ')
	

	if true_password == password:
		print('密碼正確')
		break

	else:
		chance = chance - 1
		if chance == 0:
			print('還是錯誤了，goodbye~~~~~')
			#理論上，要跳到處理重覆錯誤 password 的 flow
			break
		else:
			print('不正確，請重試')
			print('你尚有 ', chance, ' 次機會')
'''

import random
import time

'''
down = 1
up = 100
'''

'''

down = int(input('請輸入下限  '))
up = int(input('請輸入上限  '))
count = 1

r = random.randint(down, up)

guess_down = down
guess_up = up


print('\n系統隨機產生了一個', down, '至', up, '的數字，估中有獎\n')


while True:
	time.sleep(1)
	
	print('\n依家範圍係 ', guess_down, '至', guess_up, '\n')
	time.sleep(0.5)

	if guess_down == guess_up:
		print('無扮野喇，得返一個冧巴，冧巴溫啊你，快啲中左佢算啦\n')
	elif guess_up - guess_down < 15:
		print('得幾個數字，中硬啊你\n')

	time.sleep(0.5)
	print('係第 ', count, ' 次估！\n\n')
	time.sleep(0.5)

	guess = int(input('請輸入你估的數字。  '))
	print('\n\n')
	time.sleep(0.5)

	if guess == guess_down or guess_up:
		print('玩野？這個數字猜過了\n ')
	if guess < down:
		print('估咁細！落地獄啊你！  ', guess_down, '至', guess_up, ' 啊豬頭，再估過\n ')
	elif guess > up:
		print('估到出宇宙丫笨！ ', guess_down, '至', guess_up, ' 啊豬頭，再估過\n ')

	elif guess < guess_down:
		print('無腦架？仲估細啲？再估過\n ')
	elif guess > guess_up:
		print('無腦架？仲估大啲？再估過\n ')
	

	elif guess == r:
		print('估中了！！ 利害！！')
		break
	elif guess > r:
		print('太大了，再估\n')
		count = count + 1
		guess_up = guess - 1
	elif guess < r:
		print('太細了，再估\n')
		count = count + 1
		guess_down = guess + 1
	else:
		print('輸入數字啦')

'''


'''
list 清單，data structure
index
.append
'''

'''
a = ['item 1', 'item 2']
print(a)
print(a[0])
a.append('item 3')
print(a)
print(len(a))

print('item 3' in a)
'''

'''
cars = ['Toyota', 'Honda']

for x in cars:
	print(x)

students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']

for x in students:
	print('Hi', x)

print(len(students))


car = 'Audi'

for x in car:
	print(x)
	print(len(car))

print('A' in car)
'''

'''
data = []

with open('food.txt', 'r') as f:
	for line in f:
		line = line.strip()
		data.append(line)


print(data)
'''

'''

data = []

with open('test.txt', 'r') as x:
	for name in x:
		name = name.strip()
		data.append(name)

print(data)

'''

'''
data = []
count = 0

with open('reviews.txt', 'r') as x:
	for comment in x:
		data.append(comment)
		count = count + 1
		if count % 1000 == 0:
			print(len(data))

'''

#print('檔案讀取完，總共有', len(data), '筆資料')

#print(len(data))

#print(data)
'''print(data[0])
print('-------------')
print(data[99])'''


'''
data = []
comment_count = 0
comment_100 = 0
comment_100_2 = []
comment_good = []
comment_good_2 = []
comment_bad = []


with open('reviews.txt', 'r') as x:
	for comment in x:
#		comment = comment.strip()
		comment_count = comment_count + len(comment)
		data.append(comment)
		if 'good' in comment:
			comment_good.append(comment)
		if len(comment) < 100:
			comment_100 = comment_100 + 1
			comment_100_2.append(comment)

with open('reviews.txt', 'r') as x:
	comment_good_2 = [comment.strip() for comment in x if 'it is good' in comment]

with open('reviews.txt', 'r') as x:
	comment_bad = ['bad' in comment for comment in x]
# or
comment_bad = []
for comment in x:
	comment_bad.append('bad' in comment)



print('檔案讀取完，總共有', len(data), '筆資料')
print('留言的平均長度是：', comment_count / len(data))
print('留言少於100字的數量是：', comment_100)
print('留言少於100字的數量是：', len(comment_100_2))
print('留言包含「good」的數量是：', len(comment_good))
print('留言包含「it is good」的數量是：', len(comment_good_2))


print(comment_good_2[0])
# print(comment_100_2[1])
'''

cart = []

while True:
	product = input('請輸入產品名稱： ')
	if product == 'q':
		break
	price = input('產品的價格： ')
	# p = []
	# p.append(product)
	# p.append(price)
	p = [product, price]
	cart.append(p)

print(cart)

product[0][0]

print('你的購物車有以下產品')
for cart_list in cart:
	print(cart_list)
	


'''
python3 product.py

#更新版本用
git add product.py
git commit -m "product first commit"
git push origin main
'''