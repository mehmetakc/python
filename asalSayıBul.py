#!girlen sayıya kadar kac asal sayı var hangileri olduğunu bullan kod :

 #! ders 50   girilen sayıya kadar olan asal sayıları bulıp ekrana yazdiran kod

input_numbers=int(input("lutfen bir sayi giriniz"))
prime_numbers=[]
if(input_numbers<0):
  print("negatif bir sayi girdiniz lutfen bir pozitif sayı giriniz")
elif(input_numbers>0 and input_numbers<2):
 print("en kucuk asal sayı 2 dir ")
else:
    prime_numbers.append(2)#! iki asal sayı oldugu icin ekledik hepsinde var diye
    for i in range(3,input_numbers+1,2):#! 3 den basla girilen sayı -1 e kadar bakar dostum +1 ekledık 2 ser 2ser alark articak dostum cift sayılara bakmaya gerek yok 
         for j in range(3,int(i**0.5)+1):#! karekokune kadar bakıyoruz fazla gıtmeye gerek yoktur dostum
             if(i %j==0):
              break
         else:
              prime_numbers.append(i)#! bolunmuyorsa asal sayı dedık ve listeye ekledik hocam bizde
    print(f"{prime_numbers}")
    