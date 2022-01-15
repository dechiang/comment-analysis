# review comments program

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # 如果count 的餘數和 1000 是 0
			print(len(data))
print('the file has been uploaded succussfully, it has total: ', len(data), 'comments')


sum_len = 0
for d in data:
	sum_len += len(d) # sum = sum + len(d)
print('the average length of each comment: ', sum_len / len(data)) 
# total length / total comments

less = []
for t in data:
	if len(t) < 100:
		less.append(t)
print("total comments less than 100 words: ", len(less))
print(less[0])


good = []
for x in data:
	if 'good' in x:
		good.append(x)
print(len(good))
print(good[0])
