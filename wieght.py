print('Enter unit you want convert: ')
unit = input('(L)bs or (K)g: ')
weight = int(input('weight '))


if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'Your are in {converted} kilos')
else:
    converted = weight // 0.45
    print(f'Your are in {converted} pounds')