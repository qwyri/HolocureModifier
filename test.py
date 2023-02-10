from re import sub

x = input("")
y = int(input(""))

print(sub(f'\"{x}\": ',f'\"{x}\": {y}.0',f'\"{x}\": ,'))