#Kullanıcıdan alınan girdinin tersten okunuşuyla düzden okunuşunun aynı olup olmadığına bakar
girdi=input("Stringi giriniz:")

if girdi[::1]==girdi[::-1]:
    print("Bu bir palindromdur!")
else:
    print("Bu bir palindrom değildir!")
