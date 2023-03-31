def mispelled(word1,word2):
    len1,len2 = len(word1),len(word2)
    if len1==len2:
        return sum(1 for res1,res2 in zip(word1,word2) if res1 != res2) <= 1
    if len1-len2 == 1:
        return word1.startswith(word2) or word1.endswith(word2)
    if len1-len2 == -1:
        return word2.startswith(word1) or word2.endswith(word1)
    return False
