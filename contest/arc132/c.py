
# 500,5
# n,d = map(int,input().split())
# a = list(map(lambda x: int(x)-1,input().split()))
# mod = 998244353
# # 使ってない数
# lst = [0] * n
# # なんでも入れられるとこ
# lst_minus = [0] * n
# dp = [[0] * (n+1) for _ in range(n+1)]

# """
# ai = pi
# pi - i <= d
# """

# for i in range(n):
#     if a[i] != -2:
#         if abs(a[i] - i) > d:
#             print(0)
#             exit()
#         lst[a[i]] = 1
#     else:
#         lst_minus[i] = 1


# # i番目がjだだった時の合計数
# if lst_minus[0]:
#     cnt = 0
#     for j in range(min(d+1,n)):
#         if lst[j]:
#             continue
#         dp[0][j] = 1
#         cnt += 1
#     if cnt == 0:
#         print('a')
#         print(0)
#         exit()
#     dp[0][n] = cnt

# for i in range(1,n):
#     sum_ = 0
#     if lst_minus[i]:
#         for j in range(max(i-d,0),min(i+d+1,n)):
#             # 使ってたら
#             if lst[j]:
#                 continue
#             cnt = 0
#             for minus in range(1,d+1):
#                 if not 0 <= i-minus <n:
#                     continue
#                 cnt += dp[i-minus][j]
#             dp[i][j] = (dp[i-1][n] - cnt) % mod
#             sum_ += dp[i][j]
#         if sum_ == 0:
#             print('i')
#             print(0)
#             exit()
#         dp[i][n] = sum_
#     else:
#         dp[i][n] = dp[i-1][n]
# print(dp[n-1][n])
# 残りの数の中で何通り使用できるか計算する
# low = n
# high = 0
# ans = 0
# duplicate = 0
# prev = []
# # i番目のやつを決定する
# for i in lst_minus:
#     now_ = []
#     now_duplicate = 0
#     for is_use in range(max(i-d,0),min(i+d+1,n)):
#         if lst[is_use] == 0:
#             now_.append(is_use)
#         if len(now_) == 0:
#             print(0)
#             exit()
#     for p in prev:
#         if p in now_:
#             now_duplicate += 1
#     duplicate *= now_duplicate
#     ans += len(now_)
#     prev = now_
    


n,d = map(int,input().split())
a = list(map(int,input().split()))
mod = 998244353

# i番目を決める時、p_i, i-d ~ i+d
# dp[i][rest]
dp = [[0] * (1 << 2*n) for _ in range(n)]
dp[0][(1<<d) -1] = 1
for i in range(n):
    for bitmask in range(1 << (2*n)):
        val = dp[i][bitmask]
        new_bitmask = bitmask << 1
        if val == 0:continue
        if bitmask % 2 == 0:
            new_val = i - d + 1
            if a[i] == new_val or a[i] == 1:
                continue
            dp[i+1][bitmask // 2] += val
            dp[i+1][bitmask // 2] %= mod
        else:
            for j in range(2*d):
                if (new_bitmask >> j) %2 == 1:continue
                new_val = i+j-d+2
                if new_val > n:
                    continue
                if new_val == a[i] or a[i] == -1:
                    dp[i+1][new_bitmask | (1<<j)] += val
                    dp[i+1][new_bitmask | (1<<j)] %= mod

print(dp[n][1 << d]-1)


                
            
            