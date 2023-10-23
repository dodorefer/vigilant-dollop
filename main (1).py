from math import log10, tan
m = [2, 5, 10, 22, 3, 88, 11, 5, 17, 10, 3, 5]

print("#1)", max(m))
print("#2)", min(m))
m_lg = [log10(i) for i in m]
m_lg = [m_lg.pop(m_lg.index(max(m_lg)))] + m_lg
print("#3)", m_lg)
res = 0
res_m = []
for i in m:
    if i % 11 == 0:
        res += 1
        res_m.append(i)
print("#4)", ['Нет таких', max(res_m)][res!=0])
res = []
for i in range(1, len(m)-1):
    if m[i-1] - m[i+1] >= 72:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#5)", res)
res = []
for i in range(1, len(m)-1):
    if m[i-1] / m[i+1] % 2 == 0:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#6)", res)
res = []
for i in range(1, len(m)-1):
    if abs(m[i-1] - m[i+1]) % 2 == 0:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#7)", res)
res = []
for i in range(1, len(m)):
    if sum(m[:i]) == 12:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#8)", res)
res = []
for i in range(len(m)):
    if m[i] % 10 == 0:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#9)", res)
res = []
for i in range(1, len(m)-1):
    if m[i-1] - m[i+1] % 2 == 0 and m[i-1] - m[i+1] % 3 == 0:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#10)", res)
res = []
for i in range(1, len(m)-1):
    t = [j**2 for j in m[i:]]
    if (sum(t)/len(t))**0.5 < 10:
        res.append(m[i])
if res:
    res = max(res)
else:
    res = "Нет таких"
print("#11)", res)
m_lg = [tan(i) for i in m]
m_lg = [m_lg.pop(m_lg.index(max(m_lg)))] + m_lg
print("#12)", m_lg)