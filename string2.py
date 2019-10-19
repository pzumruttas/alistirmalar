girilen_string=str(input("Stringi giriniz:"))

aranan_harf=str(input("Aranan harf:"))
a=0
for i in range(len(girilen_string)):
    if girilen_string[i]==aranan_harf:
        a+=1

print(a)
          
