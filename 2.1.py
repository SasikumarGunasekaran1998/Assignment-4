def func(word_list):
    return len(word_list)
if __name__ == "__main__":
    word_list = ["abbs","acdvv","valg","ineuron"]
    x = map(func,word_list)
    print(list(x))
        
