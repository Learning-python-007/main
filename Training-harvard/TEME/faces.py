#Making Faces
#Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!
#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to π (otherwise known as a slightly smiling face) and any :( converted to π (otherwise known as a slightly frowning face). All other text should be returned unchanged.
#Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. Youβre welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

#import  emoji
#name = input("emoticon ")
#print(emoji.emojize(name))

def main():
    faces = input("Say something: ")
    print(change_faces(faces))


def change_faces(sentence):
    sentence = sentence.replace(":)", "π")
    sentence = sentence.replace(":(", "π")
    return sentence

main()
