import sys

def count_keyword_occurrences(keyword, text):
    return text.count(keyword)

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    text = sys.argv[2]
    count = count_keyword_occurrences(keyword, text)
    
    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()