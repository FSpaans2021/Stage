
def main():
    list_text, list_text2 = input_and_prepare_text()
    both_texts = compare_text(list_text, list_text2)
    final_new_list_both_texts = remove_unnecessary_words(both_texts)
    write_file(final_new_list_both_texts)


def input_and_prepare_text():
    text = input("Enter your text: ")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    list_text = []
    text = text.split(" ")
    for i in text:
        list_text.append(i)

    text2 = input("Enter your text: ")
    text2 = text2.replace(",", "")
    text2 = text2.replace(".", "")
    text2 = text2.lower()
    list_text2 = []
    text2 = text2.split(" ")
    for i in text2:
        list_text2.append(i)

    return list_text, list_text2

def compare_text(list_text, list_text2):
    both_texts = []

    for i in list_text:
        if i in list_text2:
            both_texts.append(i)

    return both_texts

def remove_unnecessary_words(both_texts):
    unnecessary_words = ["the", "a", "and", "from", "is", "there", "as", "this", "to", "of", "are", "on", "which", "in",
                         "well", "with"]

    new_list_both_texts = []
    for i in both_texts:
        if i not in unnecessary_words:
            new_list_both_texts.append(i)

    final_new_list_both_texts = list(dict.fromkeys(new_list_both_texts))

    return final_new_list_both_texts

def write_file(final_new_list_both_texts):
    file = open("output.txt", "w")
    for element in final_new_list_both_texts:
        file.write(element + "\n")
    file.close()



if __name__ == "__main__":
    main()