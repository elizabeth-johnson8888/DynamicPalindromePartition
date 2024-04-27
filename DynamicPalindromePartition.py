"""
name:  Elizabeth Johnson

"""
memoization = {}
# checks if the string is a palindrome by checking it against its reverse side
def isPalindrome(string):
    return string == string[::-1]

def countPalindromes(s):
    if len(s) == 0:
        return 0  # no palindromes in an empty string

    # results of smaller
    cnt = [0] * (len(s) + 1)
    cnt[0] = 1  # base case is empty string is a palindrome

    for i in range(1, len(s) + 1):
        for j in range(i):
            if s[j:i] not in memoization:
                memoization[s[j:i]] = isPalindrome(s[j:i])

            if memoization[s[j:i]]: # if its a palimdrome
                cnt[i] += cnt[j]

    return cnt[len(s)]


def main():
    # get input
    n = int(input())
    words = [input() for _ in range(n)]

    # for each word, count the number of palindrome partitions and print the sum
    num = 0
    for word in words:
        num = countPalindromes(word)
        print(num)
    pass

if __name__ == "__main__":
    main()
