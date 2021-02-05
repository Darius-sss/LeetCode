strs = ["flower", "flow", "flight"]

m = len(strs)
n = min(len(_) for _ in strs)
print(m, n)
ind, temp = 0, []
for i in range(0, 2):
    temp.clear()
    for j in range(m):
        temp.append(strs[j][i])
    if len(set(temp)) != 1:
        break
    else:
        ind = i
print(strs[0][:ind+1])



