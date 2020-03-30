
# parola kontrol

forbidden_number = 0
password = True
user_input = 0
print ("Parolanız sadece rakamlardan oluşabilir ve içerisinde 0 olmamalıdır.")

while password :

    try:
        user_input = int(input("Lütfen parola giriniz:"))
        print(user_input)

    except ValueError:

        print("Sadece rakam kullanılabilir")

    if user_input <= forbidden_number:

            print("Parola 0 içeremez.")

    else :
        print("Üyelik tamamlandı.")
        password = False
