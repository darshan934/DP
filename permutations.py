def permutations(str):
    if len(str) <= 1:
        return [str]
    else:
        perms = []
        for ch in permutations(str[:-1]):
            for i in xrange(len(ch)+1):
                perms.append(ch[:i] + str[-1] + ch[i:])
        return perms