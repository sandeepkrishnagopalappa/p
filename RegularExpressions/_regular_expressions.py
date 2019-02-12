import re

# Searching and Matching Text

# . - Matches any character except new line
# \d - Digit [0-9]
# \D - Not a Digit [^0-9]
# \w - Word Character [a-zA-Z0-9_]
# \W - Not a word character
# \s - White Space (space, tab, new line)
# \S - Not White Space


# Anchors
# ^ - Start of the String   (^ inside square brackets is inversion or NOT)
# $ - End of the String
# \b -  Word Boundry
# \B - Not a word Boundry

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
http://facebook.com

123*456*1234
123.456.1234

600-098-9864
1800-123-1245
900-098-9864

(080)-123-0987
Mr. Steve
Mr Jobs
Ms Steve
Mrs. Steve
Mr. S

Hello_world! Welcome to Python Training !wow!

Hello !world How are you d$oing

10.1.2.1
199.199.199.199
1.1.1.1
12.122.1.222
127-0-0-0
'''


def search_pattern(_search_pattern, _search_string):
    _pattern = re.compile(_search_pattern)
    _matches = _pattern.findall(_search_string)
    return _matches


# email_pattern = '[\w.-]+@[\w.]+'
# phone_pattern = '\d{3}[-*.]\d{3}[-.*]\d{4}'
# phone_pattern_toll_free = '1800[-*.]\d{3}[-.*]\d{4}'
# phone_pattern_not_800_900 = '[^89]00[-*.]\d{3}[-.*]\d{4}'
# url_pattern = 'https?://[\w.]+'
# person_pattern = '(Mr|Mrs|Ms)\.?\s[\w]+'
# Hours_24_time_format = '[0-2][0-4]:[0-5]\d:[0-5]\d'
# id_address_format = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
url_pattern_2 = 'https?://(www)?([\w.]+)(com|edu|gov)'

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
# matches = search_pattern('colou?r', 'color')  # Matches colour or color
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
# with open('apache.log') as file:
#     text = file.read()


# Below regular expression matches only integers
# '' - Should Not Match
# ' 5' - Should Not Match
# '4000' - Should Match
# '-999' - Should Match
# '+999' - Should Not Match
# '00' - Should Match
# '0.0' - Should Not Match
match_integer = '^[-]?([1-9]\d*|0)$'
# matches = search_pattern(match_integer, '')
# matches = search_pattern(match_integer, ' 5')
# matches = search_pattern(match_integer, '5000')
# matches = search_pattern(match_integer, '-999')
# matches = search_pattern(match_integer, '+999')
# matches = search_pattern(match_integer, '00')
# matches = search_pattern(match_integer, '0.0')

# Below regular expression matches fractions
# '' - Should Not Match
# '5000' - Should Not Match
# '-999/1'  - Should Match
# '+999/1' - Should Match
# '00/1' - Should Match
# '/5'  - Should Not Match
# '5/0' - Shoud Not Match
# '5/010' - Should Match
# '5/105' - Should Match
# '5 / 1' - Should Not Match

# match_fraction = '^\S[^\s\D+]\d{1, 3}/\d{1, 3}'

# ===================================================
# Regular expression - VOWELS
match_vowels = '[aeiou]'
words = ['hello', 'exit', 'entry', 'auspicious']
for word in words:
    print(word, '--> ', end='')
    matches = search_pattern(match_vowels, word)
    for match in matches:
        print(match, end=',')
    print()
# ===================================================
# Regular Expression - File extensions
# ===================================================
match_file_extension = '\.[a-zA-Z]+$'
files = ['archive.zip', 'image.jpeg', 'index.xhtml', 'archive.tar.gz']
for file in files:
    print(file, '-->', end='')
    matches = search_pattern(match_file_extension, file)
    for match in matches:
        print(match)
# ===================================================
# Regular Expression- File Abbrevation
# ===================================================
match_abbreviation = r'(\b[A-Za-z]|\B[A-Z])'
file_formats = ['Graphics Interchange Format',
                'Advanced Audio Coding',
                'cascading style sheets',
                'HyperText Markup Language',
                'Joint Photographic Experts Group',
                'content management system',
                'Tagged Image File Format',
                'Windows Media Audio',
                'Comma Seperated Values',
                'JavaScript Object Notation'
                ]
for name in file_formats:
    print(name, ' -->', end='')
    matches = search_pattern(match_abbreviation, name)
    for match in matches:
        print(''.join(match).upper(), end='')
    print()
# ===================================================
# Regular Expression - YYYY-MM-DD date format
# ===================================================
_dates = ['2019-01-02', '2019-13-02', '2019-12-26', '26-08-2019', '20-19-20', '2019-12-31', '2019-12-32']
match_date_format = r'(\d{4})-([0-1][0-2])-([0-2][0-9]|3[01])'

for date in _dates:
    matches = search_pattern(match_date_format, date)
    for match in matches:
        print(match)
# ===================================================

# Regular Expression -
_links = ['https://www.python.org', 'https://www.google.com', 'https://www.fecebook.com']
match_links = r'\.[a-z]+\.'

for link in _links:
    matches = search_pattern(match_links, link)
    for match in matches:
        print(match[1:-1])

