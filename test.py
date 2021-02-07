def same_start_end(s):
    """最长前后缀相同的字符位数"""
    k = -1
    n = len(s)
    j = 0
    next_list = [0 for _ in range(n)]
    next_list[0] = -1                           #next数组初始值为-1
    while j < n-1:
        if k == -1 or s[k] == s[j]:
            k += 1
            j += 1
            next_list[j] = k                    #如果相等 则next[j+1] = k
        else:
            k = next_list[k]                    #如果不等，则将next[k]的值给k
    return next_list


def kmp(s, p):
    """kmp算法,s是字符串，p是模式字符串，返回值为匹配到的第一个字符串的第一个字符的索引，
    没匹配到返回-1"""
    i = 0  # 指向s
    j = 0  # 指向p
    next_list = same_start_end(p)
    ans = -1
    while i < len(s):
        if s[i] == p[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next_list[j]
        if j == len(p):
            ans = i - len(p)
            break
    return ans

print(kmp("mississippi", "issip"))