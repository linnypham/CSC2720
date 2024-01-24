array = ["eat","tea","tan","ate","nat","bat"]

anagram_dict = {}

for w in array:
    count = [0]*26
    for c in w:
        count[ord(c)-ord("a")]+=1
    if tuple(count) not in anagram_dict:
        anagram_dict[tuple(count)] = []
    anagram_dict[tuple(count)].append(w)

result = list(anagram_dict.values())
print(result)
