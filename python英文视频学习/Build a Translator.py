'''
def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translate = translate + "g"
        else:
            translate = translate +letter
    return translate

print(translate(input("ENter a phrase:")))
'''

'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":      # 没有返回大写字母
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:")))
'''
m

# 翻译相应的单词


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase:")))