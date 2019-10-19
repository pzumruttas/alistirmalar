girdi=str(input("Stringi giriniz:"))

if girdi[::1]==girdi[::-1]:
    print("Bu bir palindromdur!")
else:
    print("Bu bir palindrom değildir!")
