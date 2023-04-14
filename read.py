data = []
count = 0

with open('reviews.txt', 'r') as f :
	for line in f:
		data.append(line)
		count += 1
		if count %1000 == 0:
			print(len(data))
print('檔案讀取完了', len(data), '筆資料')


sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度是', sum_len/len(data))

#清單篩選
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

#留言裡有提到good這個字串相關的
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('有', len(good), '筆留言提到good')
print(good[0])		 

#list comprehension(清單快寫法)
#good = [d for d in data if 'good' in d]
"""
等於
good = []
for d in data:
	if 'good' in d:
		good.append(d)
"""
#bad = ['bad' in d for d in data]
"""
等於
bad = []
for d in data:
	bad.append('bad' in d)
"""


