"""
name:  Elizabeth Johnson

"""
memoization = {}

def isPalindrome(string):
    return string == string[::-1]

def countPalindromes(s):
    if len(s) == 0:
        return 0  # No palindromes in an empty string

    # results of smaller
    cnt = [0] * (len(s) + 1)
    cnt[0] = 1  # Base case: empty string is a palindrome

    for i in range(1, len(s) + 1):
        for j in range(i):
            if s[j:i] not in memoization:
                memoization[s[j:i]] = isPalindrome(s[j:i])

            if memoization[s[j:i]]: # if its a palimdrome
                cnt[i] += cnt[j]

    return cnt[len(s)]


def main():
    n = int(input())
    words = [input() for _ in range(n)]
    num = 0
    for word in words:
        num = countPalindromes(word)
        print(num)
    pass

if __name__ == "__main__":
    main()
