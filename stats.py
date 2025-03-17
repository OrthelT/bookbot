



def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    chars = [x.lower() for x in text]
    unique_chars = []
    unique_chars = [c for c in chars if c not in unique_chars]
    chars_dict = dict.fromkeys(unique_chars)
    for key in chars_dict.keys():
        count = chars.count(key)
        chars_dict[key] = count
        count = 0
    results = create_report(chars_dict) 
    return results

def create_report(chars_dict):
    sorted_dict = dict(sorted(chars_dict.items(), key=lambda item: item[1], reverse=True))
    dict_list = []
    for k,v in sorted_dict.items():
        dict_list.append({k: v})

    return dict_list
