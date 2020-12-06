import re

# ============ Characters ===================
# . - Matches any character except new line
# \. - Mathes a dot.
# \\ - Matches backslash
# \* - Matches astrick

# ============ Character set ===================
# [abcd] - any character which matches either 'a' or 'b' or 'c' or 'd'
# [^abcd] - any character but not 'a' or 'b' or 'c' or 'd'
# [a-z] - any character between 'a' through 'z'

# =========== Special Sequences ================
# \w - Word character. Same as [a-zA-Z0-9_]. Matches alphanumeric and underscore.
# \W - Non-Word Character. Same as [^a-zA-Z0-9_]. Matches anything but word characters.
# \d - Matches a digit. Same as [0-9]
# \D - Matches a Non-Digit. Same as [^0-9]
# \s - Matches only whitespace.
# \S - Matches only Non-Whitespace.

# ========== Anchors ======================
# ^ - Start of String
# $ - End of String
# \b - Word boudary
# \B - Not a word Boundry
# [] - Matches characters in square brackets
# [^ ] - Matches characters Not in square brackets

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

# =========== Grouping ====================
# ("A"| "B" | "C") - Either "A" or "B" or "C"


def search_pattern(_search_pattern, _search_string):
    _matches = re.findall(_search_pattern, _search_string)
    return _matches


greeting = "Hello world welcome to regular expressions in python"
matches = re.findall("python", greeting)


# ===================================================
# Regular expression - VOWELS
match_vowels = r'[aeiou]'
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
match_file_extension = r'\.[a-zA-Z]+$'
files = ['archive.zip', 'image.jpeg', 'index.xhtml', 'archive.tar.gz', 'python.py']
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
# Regular Expression - Website names
_links = ['https://www.python.org',
          'https://www.google.com',
          'https://www.facebook.com',
          'https://www.youtube.com',
          'http://www.amazon.com.us'
          ]
match_links = r'\.[a-z]+\.'

for link in _links:
    matches = search_pattern(match_links, link)
    for match in matches:
        print(match[1:-1])
# ===================================================
# Regular Expression - Phone Number pattern
# ===================================================
phone_numbers = ['123-345-0987', '456-9832-098', '800-987-4756', '080-1029384725', '123-345-12', '900-938-0987']
match_phone_numbers = r'\d{3}[-.]\d{3}[-.]\d{4}'

for phone_number in phone_numbers:
    matches = search_pattern(match_phone_numbers, phone_number)
    for match in matches:
        print(match)
# ===================================================
# Regular Expression - IP Addresses
# ===================================================
id_address_format = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ips = ['10.1.2.3', '127.0.0.0', '199.99.9.9', '199.9.9999.9', '127-0-0-0']

for ip in ips:
    matches = search_pattern(id_address_format, ip)
    for match in matches:
        print(match)
# ===================================================
# Regular Expression - Email format
# ===================================================
email_pattern = r'[\w.-]+@[\w]+\.com'
emails = ['test.user@company.com',
          'test.user2@company.com',
          'test_user@company.com',
          'testing@company.com',
          'test-T.user@company.com',
          'testing@company',
          'testingcompany.com'
          ]

for email in emails:
    matches = search_pattern(email_pattern, email)
    for match in matches:
        print(match)
# ===================================================
# Regular Expression - URL Pattern
# ===================================================
url_pattern = r'https?://[\w.]+'
urls = ['http://youtube.com',
        'https://google.com',
        'http://amazon.in',
        'https://mail.yahoo.com',
        'ftp://test.com'
        'https://facebook.com/'
        ]

for url in urls:
    matches = search_pattern(url_pattern, url)
    for match in matches:
        print(match)
# ===================================================
