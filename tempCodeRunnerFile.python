n = int(input().strip())
input()  # skip 'shuffled'
shuffled = [input().strip() for _ in range(n)]
input()  # skip 'original'
original = [input().strip() for _ in range(n)]

same = 0
for i in range(n):
    for j in range(n):
        k = 0
        while i + k < n and j + k < n and shuffled[i + k] == original[j + k]:
            k += 1
        if k > same:
            same = k

print(n - same)
