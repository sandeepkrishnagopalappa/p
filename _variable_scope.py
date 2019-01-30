# x = 'global x'


def test(z):
    global x    # Explicitly declaring x as global inside function
    # y = 'local y'
    # x = 'local x'
    # print(y)
    # print(x)
    print(z)


test('local z')

# print(x)
