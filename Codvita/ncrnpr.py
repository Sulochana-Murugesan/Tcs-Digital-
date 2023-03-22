MOD = int(1e9 + 7)

# function to calculate the number of combinations
def nCr(n, r):
    if r > n:
        return 0
    if r > n - r:
        r = n - r
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res

# function to calculate the number of permutations
def nPr(n, r):
    res = 1
    for i in range(r):
        res = res * n
    return res

low, high = map(int, input().split())
K = int(input())

# count the number of even and odd numbers in the range
even_count = (high - low + 1) // 2
odd_count = high - low + 1 - even_count

# count the number of valid permutations
ans = 0
for i in range(K // 2 + 1):
    j = K - i
    if i <= even_count and j <= even_count:
        ans += (nCr(even_count, i) * nPr(even_count, i) * 
                nCr(even_count, j) * nPr(even_count, j))
        ans %= MOD

if K % 2 == 0:
    ans -= nCr(even_count, K // 2) * nPr(even_count, K // 2) ** 2
else:
    ans -= (nCr(even_count, K // 2) * nPr(even_count, K // 2) * 
            odd_count)
ans %= MOD

print(ans)
