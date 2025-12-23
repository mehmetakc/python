
#!banka hesap uygulaması
def create_account(owner_name):
    return {"owner": owner_name,"balance":0}
   
def depozit(amount,account):
    if(amount>0):
        account["balance"]+=amount
        print(f"{amount} tl basarılı bır sekılde yuklenmısstır guncel  bakıyenız :{account["balance"]}tl")
    else:
        print("yatırılacak mıktar pozıtıf olmalıdır")
def withdraw(amount,account):
    if(amount>0):
        if(account["balance"]>=amount):
            account["balance"]-=amount
            print(f"{amount} tl basarılı bır sekılde  cekıldı guncel bakıye {account["balance"]} tl")
        else:
            print("hesabınızda yeterli bakıye bulunmamaktadır ")
    else:
        print("cekilecek mıktar pozıtıf olamıdır ")

def display_balance(account):
   print(f"{account["owner"]} hesanın guncel bakıyesi {account["balance"]} tl dir")

print("BANKAMIZIN HESAP UGULAMSINA HOSEGELDİNİZ")
owner=input("HESAP SABİNİN ADİ:")
account=create_account(owner)
while(True):
    print("\nSECENEKLER:")
    print("1-para yatir")
    print("2-para cek")
    print("3-bakiye görüntule")
    print("4-cıkıs")
    choice=int(input("seiminizi yapınız 1 ve 4 arasında "))
    if(choice==1):
     amount=float(input("lutfene yatırmak ıstedıgınız para tutarını gırınız:"))
     depozit(amount,account)
       
    elif(choice==2):
     amount=float(input("lutfene cekmek ıstedıgınız para tutarını gırınız:"))
     withdraw(amount,account) 
    elif(choice==3):
     display_balance(account)


    elif(choice==4):
        print("uygulamdan cıktınız iyi gunler dileriz ")
        break
    else:
        print("gecersiz secim ! lutfen 1 ve 4 arsında secim yapınız ")
