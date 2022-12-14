#task 1 on Problem Solving 2
# word = input('Type a random word. ')
# reversed_word = ''
# def reverse_word(word):
#     #word = input('Type a random word. ')(<---needed for it's own function unless another function is gathering userinput)
#     reversed_word = ''
#     for index in range(len(word) -1, -1, -1):
#         reversed_word += word[index]
#     return reversed_word
    #print(reversed_word)  <---commented this out so I could return a value rather than print to be used in task 3
#reverse_word()
#task 2 
def cap_each_first_letter():
    response = input("Type A Sentence To Be Formatted The Same As This Request: ")
    split_words = response.split(" ")
    formatted_response = ""
    word = 0
    for word in split_words:
        i = 0
        split_letters = list(word)
        split_letters[i] = split_letters[i].upper()
        seperator = ''
        joined_word = seperator.join(split_letters)
        formatted_response += joined_word + ' '
    print()
    print(formatted_response)
    print()
    
    #print(split_word)
        
        #formatted_response = formatted_response + split_response[word+1].capitalize()
        #i += 1
    #print(split_response)
        # formatted_response = response.split(" ")[0].capitalize() + response.split(" ")[1].capitalize()
        # print(formatted_response)
    # result = response.split(' ')
    # print(result)

cap_each_first_letter()    
# def cap_each_first_letter():
#     response = input('Type a random sentence. ')
#     capped_response = response.title()  
#     print(capped_response)  
# cap_each_first_letter()
#task 3
# def run_palindrome():
#     response = input("Type a word you believe to be a Palindrome: ")
#     is_palindrome = reverse_word(response)

#     while is_palindrome != response:
#         response = input('This is not a Palindrome. Try again ')
#         is_palindrome = reverse_word(response)
#         if is_palindrome == response:
#             continue
#     print('This is a Palindrome!')

# run_palindrome()
