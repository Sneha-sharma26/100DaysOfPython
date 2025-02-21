# Write a py program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end. Now, append three random characters at the starting and the end.
# else:
#    simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#    remove the 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Program should ask whether you want to code or decode


# ## ------------ MY CODE ------------ ##
import random
import string

def reverse_msg(word) :                   # function to reverse string
    return word[-1: -len(word)-1 : -1]

def add_random_chars(word) :              # fn to add random characters into string ending and starting
    input_str = ''.join(word)
    random_chars = ''.join(random.choices(string.ascii_letters, k = 3))
    return random_chars + input_str + random_chars

def remove_random_chars(word) :           # fn to remove random characters from the string at the beginning & the ending
    return word[3:-3]

user_input = input("Enter your message : ") 
words = user_input.split(" ")
# Asking user whether they want to code or decode
user_choice = int(input("Enter your choice : 1. Code  2. Decode \n"))

# Encoding of message
if user_choice == 1 : 
    nwords = []
    for word in words:
        if len(word) < 3 :                                                # case when len < 3
            encoded_msg = reverse_msg(word)                               # reversing the message
            nwords.append(encoded_msg)
        else :
            first_char = word[0: 1: 1]     # store the 1st char for further use
            word = list(word)        # changing the datatype to list for the ease of performing operations
            word.pop(0)                    # removing the 1st letter from msg
            word.append(first_char)        # appending the 1st letter at the end
            encoded_msg = add_random_chars(word)
            nwords.append(encoded_msg)
    print(f"Your message is encoded successfully!\nEncoded Message is: {" ".join(nwords)}")
# Decoding of message      
elif user_choice == 2 :
    nwords = []
    for word in words: 
        if len(word) < 3 :
            decoded_msg = reverse_msg(word)             # if length of input encoded message < 3, then reversing the message
            nwords.append(decoded_msg)
        else :
            decoded_msg = remove_random_chars(word)     # removing the random characters
            last_char = decoded_msg[-1:-2:-1]                 # store the last char to use it further
            decoded_msg = list(decoded_msg)                   # changing the datatype to list for the east of performing operations
            decoded_msg.pop(-1)                               # removing the last character
            decoded_msg.insert(0,last_char)                   # adding the last character to the beginning of the message
            output_str = ''.join(decoded_msg)                 # changing the datatype to string using join function
            nwords.append(output_str)
    print(f"Your message is decoded successfully!\nDecoded Message is: {" ".join(nwords)}")
    
# if user enters a wrong choice       
else :
    print("Enter a valid choice! ") 



## -------------- CWH's CODE ------------ ##
# st = input("Enter message: ")
# words = st.split(" ")
# coding = input("1 for Coding and 0 for Decoding: ")
# coding = True if (coding=="1") else False       # coding = False is the condition for Decoding
# if(coding) :
#     nwords = []
#     for word in words :
#         if(len(word) >= 3):
#             r1 = "dsf"    # random characters
#             r2 = "jkr"
#             stnew = r1 + word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
    
# else:
#     nwords = []
#     for word in words :
#         if(len(word) >= 3):
#             stnew = word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))