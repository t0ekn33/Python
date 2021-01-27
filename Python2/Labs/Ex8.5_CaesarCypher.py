"""
Exercise 8.5. A Caesar cypher is a weak form of encryption that involves “rotating” each letter by
a fixed number of places. To rotate a letter means to shift it through the alphabet, wrapping around
to the beginning if necessary, so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.
To rotate a word, rotate each letter by the same amount. For example, “cheer” rotated by 7 is “jolly”
and “melon” rotated by -10 is “cubed”. In the movie 2001: A Space Odyssey, the ship computer
is called HAL, which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer as parameters, and returns
a new string that contains the letters from the original string rotated by the given amount.
You might want to use the built-in function ord, which converts a character to a numeric code, and
chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
order, so for example:
>>> ord('c') - ord('a')
2
Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
letters are different.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar
cypher with rotation 13. If you are not easily offended, find and decode some of them. Solution:
http://thinkpython2.com/code/rotate.py 
"""

def rotate_word(word,num):
    """Convert word to ord and increased by num."""
    num_code = []
    new_word = []
    for letter in word:
        num = int(num)
        if num < 0:
            num_code.append(ord(letter) - abs(num))
            # print(num_code)
        else:
            num_code.append(ord(letter) + num)
            # print(num_code)
    for num in num_code:
        new_word.append(chr(num))
    
    for let in new_word:
        print(let, end = " ")
    
        #return(new_word,num)


word = input("Enter word to encrypt:")
num = input("Enter number to rotate:")
word = rotate_word(word,num)

# print(enc_word, num)
