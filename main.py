def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    print(count)

main()