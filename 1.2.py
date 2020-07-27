def filter_long_words(word_list,n):
    if len(word_list) > n:
        return True
    else:
        return False
word_list = ["Assam","Bihar","Chennai","Jamshedpur"]
n = int(input("Enter Minimum word Length"))
filtered_words = filter(lambda seq:filter_long_words(seq,n),word_list)
print(list(filtered_words))
    
    
