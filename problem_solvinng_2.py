#task 1 on Problem Solving 2
# word = input('Type a random word. ')
# reversed_word = ''
def reverse_word():
    word = input('Type a random word. ')
    reversed_word = ''
    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]
    print(reversed_word)
reverse_word()
#task 2
def cap_each_first_letter():
    response = input('Type a random sentence. ')
    capped_response = response.title()  
    print(capped_response)  
cap_each_first_letter()
