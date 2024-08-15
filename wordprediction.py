import re


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())


    return valid_words



if __name__ == '__main__':
    english_words = load_words()
    sorted_eng_words = sorted(english_words)
    #print (sorted_eng_words)
    print('egg' in english_words)


strvar = r''
strvar = strvar+"app"
strvar = strvar+"l"
#strvar = strvar+"e"
#print(type(strvar))
pattern = re.compile(strvar)
matching_words = [word for word in sorted_eng_words if pattern.match(word)]
print(matching_words)
