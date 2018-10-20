def vowel(String):
	vowelString=[]
	vowels=['a','e','o','u']
	duplicates = len(String) - len(set(String))
	for i in String:
		if i in vowels and i not in vowelString:
			vowelString.append(i)
		
	return vowelString, duplicates
print(vowel('damdam'))