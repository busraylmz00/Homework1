
# parola kontrol

forbidden_number = "0"
password = True

print ("Parolanız sadece rakamlardan oluşabilir ve içerisinde 0 olmamalıdır.")

while password :

    user_input = input("Lütfen parola giriniz:")

    try:
        if forbidden_number in user_input :
            raise TypeError
        user_input = int (user_input)

    except ValueError :
        print("Sadece rakam kullanılabilir")

    except TypeError :
        print("Parola 0 içeremez.")

    else :
        print("Tebrikler! Üyelik tamamlandı.")
        password = False
