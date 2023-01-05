# def main():
#     x = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
#     if answear(x):
#         print("Yes")
#     else:
#         print("No")
#
#
# def answear(n):
#     if n == ("42"):
#         return True
#     elif n == ("Forty-two"):
#         return True
#     elif n == ("forty two"):
#         return True
#
# main()

def is_answer_correct(answer):
    answer = answer.lower().replace(' ', '')
    return answer == '42' or answer == 'fortytwo'

answer = input('What is the answer to the Great Question of Life, the Universe, and Everything? ')
if is_answer_correct(answer):
    print('Yes')
else:
    print('No')