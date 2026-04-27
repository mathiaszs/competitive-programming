def main():
    N, D = map(int, input().split())

    nums = list(map(int, input().split()))

    ans, soma = 0, 0
    somas = [0]

    freq = {0: 1}

    for n in nums:
        soma += n
        somas.append(soma)

        if soma - D in freq:
            ans += freq[soma - D]

        freq[soma] = freq.get(D, 0) + 1

    # Preciso de uma implementação menor para essa parte O(n)
    '''for i in range(1, N):
        for j in range(N - 1, i - 1, -1):

            a = somas[i]
            b = somas[N] - somas[j]

            siu = a + b

            if siu > D:
                break
            if siu == D:
                ans += 1'''

    # TWO POINTER TECNIQUE???
    '''left, right = 1, N

    while left < right:
        a = somas[left]
        b = somas[N] - somas[right]

        sum = a + b

        if sum == D:
            ans += 1
            left += 1
            right -= 1
        elif sum < D:
            left += 1
        else:
            right -= 1''' # After one hour, GPT said that maybe its not the better aproach

    target = soma - D
    s = 0
    left = 0
    for right in range(N):
        s += nums[right]
        while s > target and left <= right:
            s -= nums[left]
            left += 1
        if s == target and left > 0 and right < N-1:
            ans += 1


    print(ans)

if __name__ == "__main__":
    main()
