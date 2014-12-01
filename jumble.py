import os

def power_list(l):
    if len(l) == 0:
        return [[]]
    prevList = power_list(l[1:])
    currentElem = l[0]
    ansList = prevList[:]
    for lst in prevList:
        ansList.append(lst +[currentElem])
    return ansList

def permute(s):
    if len(s) <= 1:
        return [s]
    char = s[0]
    permutations = permute(s[1:])
    results = []
    for perm in permutations:
        for i in range(len(perm) + 1):
            newPerm = perm[:i] + char + perm[i:]
            results.append(newPerm)
    return results

def jumble_answer(word, valid_words):
    ans = []
    pList = power_list(word)
    for lst in pList:
        currentWord = ''.join(lst)
        permutations = permute(currentWord)
        for permutation in permutations:
            if permutation in valid_words:
                if permutation not in ans:
                    ans.append(permutation)
    return ans

wordFilePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'corncob_lowercase.txt')

valid_words = set([])
fid = open(wordFilePath, 'rb')
for line in fid:
    valid_words.add(line.strip())

word = raw_input('Enter a word, or enter empty string to quit: ').strip()
while len(word) > 0:
    print 'Here are the valid jumble words: ',
    for s in jumble_answer(word, valid_words):
        print s,',',
    print
    word = raw_input('Enter a word, or enter empty string to quit: ').strip()
