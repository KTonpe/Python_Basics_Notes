def read_and_display_poem():
    with open('BYTRAINING\poem.txt','r') as f:
        poem = f.readlines()
    for lines in poem:
        print(lines,end ='')
        print('')

def read_and_check_letter_in_story():
    with open('BYTRAINING\story.txt','r') as file:
        lines = file.readlines()
    count = sum(line[0] != 'T' for line in lines)
    print(f'"T" comes : {count} times ')

def read_and_count_word_from_file():
    input_word = input('Enter a word : ').lower()
    with open(r'BYTRAINING\notes.txt','r') as file:
        lines = file.readlines()
    word_count =[]
    count = 0
    for line in lines:
        for word in line.split():
            if len(word) < 4:
                word_count.append(word)
        count += line.lower().count(input_word)
    print(f'There are {len(word_count)} words with less than 4 letters asn the words are {word_count}')       
    print(f'The word "{input_word}" comes "{count}" times in the notes')
def read_and_count_numebr_at_last_pos_():
    with open(r'BYTRAINING\notes2.txt','r') as file:
        lines = file.readlines()
    count = []
    for line in lines:
        sentence_to_words = line.split()
        for words in sentence_to_words:
            if words[-1].isdigit():
                count.append(words)
    print(f'There are "{len(count)}" word with digit at the end of the line : they are {count}')
if __name__ =='__main__':
    menu ={
        '1': read_and_display_poem,
        '2': read_and_check_letter_in_story,
        '3': read_and_count_word_from_file,
        '4': read_and_count_numebr_at_last_pos_,
        'e': exit
    }
    while True:
        print('''
                1. Read and display poem
                2. Read and check letter in story
                3. Read and count word from file
                4. Read and count number at last position
                e. Exit
              ''')
        choice = input("Enter your choice: ")
        menu[choice]() if choice in menu else print("Invalid choice")