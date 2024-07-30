data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('File read. There are ', len(data), 'reviews in total') 

#average word count for each review
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('The average word count is', sum_len/len(data), 'per review.')

#reviews each with fewer than 100 words
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are' ,len(new), 'reviews with fewer than 100 words.')

#reviews with the word "good"
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good), 'reviews with the word \"good\".')
print(good[0])
