s = list(str(input()))
for x in s:
    i = s.index(x)
    if i % 2 :
        s[i],s[i-1] = s[i-1], s[i]
print(''.join(s))