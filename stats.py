
def get_num_words(text):
    num_words=0
    words=text.split()
    for i in range(len(words)):
        num_words+=1
    return num_words

def get_num_characters(text):
    words= text.lower()
    new_dict={}
    for word in words:
        if word not in new_dict:
            new_dict.update({word:0})
        new_dict[word]+=1
    return new_dict

def sort_on(items):
    return items['num']

def sort_dict(dict_characters):
    sorted_list=[]
    for char in dict_characters:
        if char.isalpha():
            sorted_list.append({"char": char,"num": dict_characters[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

