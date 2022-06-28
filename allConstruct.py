def allConstruct(target, wordBank):
    if(target == ""):
        return [[]]

    result = []

    for word in wordBank:
        if(target.startswith(word)):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank)
