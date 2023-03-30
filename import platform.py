
import re
# def text_match(text):
#         patterns = '^a(b*)$'
#         if re.search(patterns,  text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')
# print(text_match("ac"))
# print(text_match("abc"))
# print(text_match("a"))
# print(text_match("ab"))
# print(text_match("abb"))

def text_match(text):
        patterns = '^[a-z]+_[0-9]+_[@gmail.com]'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab123@gmail."))
