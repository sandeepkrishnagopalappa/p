# Producing Structured Output

fname = 'Steve'
lname = 'Jobs'

print(f'Hello {fname} {lname} welcome to Python!')

portfolios = [
    {'name': 'IBM', 'shares': 100, 'price': 32.212},
    {'name': 'AAPL', 'shares': 60, 'price': 340.323},
    {'name': 'MSFT', 'shares': 140, 'price': 150.545},
    {'name': 'FB', 'shares': 80, 'price': 90.345},
    {'name': 'ACME', 'shares': 35, 'price': 37.908}
]

print(f'{"name":>8} {"shares":>8} {"price":>8}')    # Write headers

for portfolio in portfolios:
    name = portfolio.get('name')
    shares = portfolio.get('shares')
    price = portfolio.get('price')
    print(f'{name:>8} {shares:>8} {price:>8.2f}')