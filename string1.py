kelime=str(input("Stringi giriniz:"))

for i in range(len(kelime)-1):
    print(kelime[i],end=".")

print(kelime[len(kelime)-1])
