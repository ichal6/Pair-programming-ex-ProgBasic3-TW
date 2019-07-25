def palindrome(str):
    str = str.lower()
    riverse_str = str[::-1]
    str = str.split(' ')
    riverse_str = riverse_str.split(' ')
    str = "".join(str)
    riverse_str = "".join(riverse_str)
    if str == riverse_str:
        return True
    else:
        return False

def main():
    return

if __name__ == '__main__':
    main()
