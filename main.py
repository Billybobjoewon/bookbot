def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    # print(count)
    letters = {"a": 0, "b": 0, "c": 0, "d": 0,
     "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
      "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, 
      "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, 
      "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
       "y": 0, "z": 0}
    lower_file = file_contents.lower()
    for char in lower_file:
        if char in letters:
            letters[char] += 1
    #print(letters)
    #directed to use function for sort key, functions have yet to be taught
    def sort_on(dict):
        return dict["num"]
    sort_letters = []
    for i in letters:
        temp = {"let": i, "num": letters[i]}
        sort_letters.append(temp)
    sort_letters.sort(reverse=True, key=sort_on)
    #print(sort_letters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document\n")
    for dict in sort_letters:
        character = dict["let"]
        number = dict["num"]
        print(f"The {character} character was found {number} times")
    print("--- End report ---")
main()