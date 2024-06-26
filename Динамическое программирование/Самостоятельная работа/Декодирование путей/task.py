def num_decodings(s: str) -> int:
    ...
    if not s:
        return 0

    # alphabet = [chr(i) for i in range(65, 91)]
    # letter_dict = {alphabet[i-1]: str(i) for i in range(1, 27)}
    # s_new = []
    # for i in range(len(s)):
    #     s_new.append(letter_dict.get(s[i]))
    # return ' '.join(s_new)

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6'):
            dp[i] += dp[i - 2]

    return dp[n]

print(num_decodings('11106'))