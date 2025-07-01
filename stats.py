def count_words(text):
    words = text.split()
    return len(words)
# unique words in a text file  
 
def count_characters(text):
    
    chardict = {}
    
    text = text.lower()                 
    for i in text:
        if i in chardict:
            chardict[i] += 1                
        else:
            chardict.update({i: 1})
    return chardict           

def sort_characters(chardict):
    finallist = []
    for key, value in chardict.items():
        if key.isalpha():
            chardict[key] = value
            finallist.append((key, value))
        else:
            continue        
    finallist.sort(key=lambda x: x[1], reverse=True)
    return finallist

