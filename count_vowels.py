text="algorithm"
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in text:
    if char.isalpha():
        vowel_count+=1
    else:
        consonant_count +=1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
