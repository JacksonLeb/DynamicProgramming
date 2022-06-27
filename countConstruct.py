def countConstruct(target, wordBank, memo={}):
    if(target in memo):
        return memo[target]
    if(target == ''):
        return 1

    totalCount = 0
    for word in wordBank:
        if(target.startswith(word)):
            suffix = target[len(word):]
            memo[suffix] = countConstruct(suffix, wordBank, memo)
            totalCount += memo[suffix]

    return totalCount


print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "baor"]))
print(countConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
      ["e", "ee", "eee", "eeeee", "eeeeee", "eeeeeeee"]))
