import re

# . -Matches any character except new line
# \d - Digit (0-9)
# \D - Not a Digit (0-9)
# \w - Word Character (a-z, A-Z, 0-9, _)
# \W - Not a word character
# \s - White Space (space, tab, newLine)
# \S - Not White Space (space, tab, newLine)

# Characters that needs to be Escaped
# . ^ $ * + ? { } [ ] \ | ( )

# Quantifiers
# * - 0 or More
# + - 1 or More
# ? - 0 or ONE
# {3} - EXACT NUMBER
# {3,4} - Range Of Numbers (Minimum, Maximum)
# {3, } - 3 or More

text = '''
Apple Inc.
654-123-4570
1, Infinite Loop, Cupertino, CA, USA
Steve.Jobs@company.com and you can email me to my mail id
https://www.apple.com

Microsoft.
567-897-0987
Redmond, Washington, USA
Bill.Gates@company.com
http://microsoft.com

Google Inc.
009-013-1084
Mountain View, CA, USA
Sundar.Pichai@company.com
http://www.google.com
https://www.gst.gov 

https://www.harvard.edu

123*456*1234
123.456.1234

600-098-9864
800-123-1245
900-098-9864

(080)-123-0987
Mr. Steve
Mr Jobs
Ms Steve
Mrs. Steve
Mr. S 

'''
# email_pattern = '[\w.-]+@[\w.]+'
# phone_pattern = '\d{3}[-*.]\d{3}[-.*]\d{4}'
# phone_pattern_800 = '[6-9]00[-*.]\d{3}[-.*]\d{4}'
# url_pattern = 'https?://[\w.]+'
# person_pattern = '(Mr|Mrs|Ms)\.?\s[\w]+'

# url_pattern_2 = 'https?://(www)?([\w.]+)(com|edu|gov)'

# with open('mailid.txt') as file:
#     str_text = file.read()


def search_pattern(str_pattern, str_string):
    # _matches = re.findall(str_pattern, str_string)
    _pattern = re.compile(str_pattern)
    _matches = _pattern.findall(str_string)
    return _matches


# matches = search_pattern('[0123456789]', '$100 and $200')
# matches = search_pattern('[0-9]', '$100 and $200')
# matches = search_pattern('[a-z]', '$100 and $200')
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
t1 = '1.1 Hello there i turned 35 years 10 months back and i am now 35.10'
t2 = '12/0'
sentence = 'I am flying out of SFO today evening and landing in LAX international'

# Matches Integers
# matches = search_pattern('^\S[\d]+', t2)

# Matches Fractions
matches = search_pattern('^\S\d*/\d+', t2)

# matches = search_pattern('\.\w+', 'archive.txt, san.kid, index.xhtml')

# matches = search_pattern('[A-Z]{3}', sentence)
print(matches)
