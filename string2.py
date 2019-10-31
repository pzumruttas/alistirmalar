girilen=input("Stringi giriniz:")

aranan_harf=input("Aranan harf:")
a=0
for i in range(len(girilen)):
    if girilen[i]==aranan_harf:
        a+=1

print(a)
          
