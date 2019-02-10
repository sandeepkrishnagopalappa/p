import re

# Searching and Matching Text

# . - Matches any character except new line
# \d - Digit [0-9]
# \D - Not a Digit [^0-9]
# \w - Word Character [a-zA-Z0-9_]
# \W - Not a word character
# \s - White Space
# \S - Not White Space


# Anchors
# ^ - Start of the String   (^ inside square brackets is inversion or NOT)
# $ - End of the String
# \b -  Word Boundry

# Meta Characters that needs to be Escaped (But need not be escaped when inside square brackets)
# . ^ $ * + ? { } [ ] \ | ( )

# Quantifiers
# * - Match expression 0 or more times
# + - Match expression 1 or more times
# ? - Match expression 0 or 1 times
# {3} - Matches expression exactly 3 times
# {3,4} - Matches expression 3 to 4 times
# {3, } - Match expression 3 or more times
# {, 3} - Match expression 0 to 3 times

text = '''
Apple Inc.
654-123-4570
1, Infinite Loop, Cupertino, CA, USA
https://www.apple.com

Microsoft.
567-897-0987
Redmond, Washington, USA
http://microsoft.com

Google Inc.
009-013-1084
Mountain View, CA, USA
http://www.google.com
https://www.gst.gov
https://www.harvard.edu

123*456*1234
123.456.1234

600-098-9864
8900-123-1245
900-098-9864

(080)-123-0987
Mr. Steve
Mr Jobs
Ms Steve
Mrs. Steve
Mr. S 

'''


def search_pattern(str_pattern, str_string):
    _pattern = re.compile(str_pattern)
    _matches = _pattern.findall(str_string)
    return _matches

# email_pattern = '[\w.-]+@[\w.]+'
# phone_pattern = '\d{3}[-*.]\d{3}[-.*]\d{4}'
# phone_pattern_800 = '[89]00[-*.]\d{3}[-.*]\d{4}'
# phone_pattern_not_800_900 = '[^89]00[-*.]\d{3}[-.*]\d{4}'
# url_pattern = 'https?://[\w.]+'
# person_pattern = '(Mr|Mrs|Ms)\.?\s[\w]+'
# Hours_24_time_format = '[0-2][0-4]:[0-5]\d:[0-5]\d'
# id_address_format = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# url_pattern_2 = 'https?://(www)?([\w.]+)(com|edu|gov)'

# with open('mailid.txt') as file:
#     str_text = file.read()
# matches = search_pattern('[0123456789]', '$100 and $200')
# matches = search_pattern('[0-9]', '$100 and $200')
# matches = search_pattern('[a-z]', '$100 and $200')
# matches = search_pattern('^a', 'apple')     # Mathches if the string start with letter 'a'
# matches = search_pattern('e$', 'apple')     # Matches if the string ends with letter 'e'
# matches = search_pattern('[A-Za-z0-9]', '$100 and $200')    # Combine both lower case and upper case and numbers
# matches = search_pattern('[^0-9]', '$100 and $200')  # Matches all characters except numbers between 0-9
# matches = search_pattern('[^A-Za-z]', '$100 and $200')  # Matches all characters except numbers between A-Z and a-z
# matches = search_pattern('^an.*a$', 'anna')  # Matches if the sequence starts with 'a' and ends with 'a'
# matches = search_pattern('^an*a$', 'anna')
# matches = search_pattern('^an*a$', 'aa')      # Match
# matches = search_pattern('^a.{1,}a$', 'ana')   # Match
# matches = search_pattern('colou?r', 'what a nice color')   # Match

# Matches Vowels
# matches = search_pattern('[AEIOUaeiou]', 'exit')
# t1 = '1.1 Hello there i turned 35 years 10 months back and i am now 35.10'
# t2 = '12/0'
# sentence = 'I am flying out of SFO today evening and landing in LAX international'

# Matches Integers
# matches = search_pattern('^\S[\d]+', t2)


# Matches Fractions
# matches = search_pattern('[^\W_]+', 'Hello_world _sandeep 123 wow $100 _Hello @text')

# matches = search_pattern('\.\w+', 'archive.txt, san.kid, index.xhtml')
# with open('reg.txt') as file:
#     text = file.read()
matches = search_pattern(phone_pattern_not_800_900, text)
print(matches)
