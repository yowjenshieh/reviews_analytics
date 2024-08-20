data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(f"File read. There are {len(data)} reviews in total") 
print(data[0])

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


#wordcount
wc = {} #word_count
for d in data:
	words = d.split() #split default = whitespace
	for word in words:
		if word in wc:
			wc[word] += 1 #add the existing value by 1
		else:
			wc[word] = 1 #add a new key
for word in wc:
	if wc[word] > 1000000:
	 	print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input("Type the word you want to find: ")
	if word == 'q':
		break
	if word in wc:
		print(f"The wordcount for {word} is {wc[word]}")
	else:
		print(f"Word not found")
print("Thank you and goodbye")









