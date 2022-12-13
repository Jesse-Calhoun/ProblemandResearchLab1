#task 1 on Problem Solving 2
# word = input('Type a random word. ')
# reversed_word = ''
def reverse_word(word):
    #word = input('Type a random word. ')
    reversed_word = ''
    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]
    return reversed_word
#reverse_word()
#task 2
# def cap_each_first_letter():
#     response = input('Type a random sentence. ')
#     capped_response = response.title()  
#     print(capped_response)  
# cap_each_first_letter()
#task 3
def run_palindrome():
    response = input("Type a word you believe to be a Palindrome: ")
    is_palindrome = reverse_word(response)

    while is_palindrome != response:
        response = input('This is not a Palindrome. Try again ')
        is_palindrome = reverse_word(response)
        if is_palindrome == response:
            continue
    print('This is a Palindrome!')

run_palindrome()
