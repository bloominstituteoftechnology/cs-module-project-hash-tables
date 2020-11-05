def letter_count(s):
	counts = {}​

	for c in s:
		if c not in counts:
			counts[c] = 0​

		counts[c] += 1
		"""
		if c in counts:
			counts[c] += 1
		else:
			counts[c] = 1
		"""​

	return counts
​

print(letter_count("aabbcaacb"))