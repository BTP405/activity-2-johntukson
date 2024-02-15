file_path = '/workspaces/activity-2-johntukson/words.txt'                

def wordCount(t):
    word_dictionary = []
    
    with open(t, 'r') as file:
        
        line_number = 1
        
        for line in file:
            new_word = {'word': line.strip(), 'line': line_number}
            line_number += 1
            word_dictionary.append(new_word)
            
    return word_dictionary         
            
print(wordCount(file_path))