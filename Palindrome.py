def trivial_method(s):
    if(s==s[::-1]):
        return True
    else:
        return False


# peeweep
# nun
def iterative_method(s):
    i=0
    j=len(s)-1
    while i<j:
        if(s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True

def recursive_method(s):
    if (len(s)<=1):
        return True
    else:
        if(s[0]==s[-1]):
            return recursive_method(s[1:-1])
        else:
            return False



def main():
    s= input("Enter a word: ")

    print("detect using trivial way: \n")
    if(trivial_method(s)):
        print("It's Palindrome! \n")
    else:
        print("It's not Palindrome! \n")

    print("detect using iterative way: \n")
    if (iterative_method(s)):
        print("It's Palindrome! \n")
    else:
        print("It's not Palindrome! \n")

    print("detect using recursive way: \n")
    if (recursive_method(s)):
        print("It's Palindrome! \n")
    else:
        print("It's not Palindrome! \n")


if __name__ == '__main__':
    main()