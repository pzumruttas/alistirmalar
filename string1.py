kelime=str(input("Stringi giriniz:"))
liste=list(kelime)

for i in range(len(liste)-1):
    print(liste[i],end=".")

print(liste[len(liste)-1])
