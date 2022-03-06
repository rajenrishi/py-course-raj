# Write a program to reverse the given list.

# IMPLEMENTATION 1
l = ['a', 'b', 'c', 'e', 'd']
out_l = []
cnt = len(l)
while cnt > 0:
    cnt = cnt - 1
    out_l.append(l[cnt])

print(out_l)

# IMPLEMENTATION 2
cnt = len(l)
for i in range(cnt):
    ele = l.pop()
    l.insert(i, ele)
print(l)