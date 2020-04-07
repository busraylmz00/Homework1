# Kullanıcı adı kontrol

user_name = True
forbidden_name = "admin"
print ("Kullanıcı adı rakam içeremez ya da içerisinde \"admin\" kelimesi olamaz.")

while user_name :
    user_input = input("Lütfen kullanıcı adı giriniz:")

    try:
        if forbidden_name == user_input.replace("Admin","admin"):
            raise ValueError

        for number in range(0, 10):
            if str(number) in user_input:
                raise TypeError

    except ValueError :
        print("Kullanıcı adı \"admin\" olamaz.")

    except TypeError :
        print("Kullanıcı adı rakam içeremez")

    else :
        print("Tebrikler! Kullanıcı adınız kaydedildi.")
        user_name = False





