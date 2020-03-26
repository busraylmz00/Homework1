
print ("Aşağıdaki işlemlerden birini seçinizi.\n1- Toplama \n2- Çıkarma")

Toplama = 1
Çıkarma = 2

output = "İlk sayı: {}, ikinci sayı: {}"
İşlem = int (input("Lütfen işlem seçiniz."))

if İşlem == 1 :
    birinci_input = int(input("Lütfen ilk sayıyı giriniz."))
    ikinci_input = int(input("Lütfen ikinci sayıyı giriniz."))
    print(output.format(birinci_input, ikinci_input), "için toplama işleminin sonucu", (birinci_input + ikinci_input))
elif İşlem == 2 :
    birinci_input = int(input("Lütfen ilk sayıyı giriniz."))
    ikinci_input = int(input("Lütfen ikinci sayıyı giriniz."))

    print(output.format(birinci_input, ikinci_input), "için çıkarma işleminin sonucu", (birinci_input - ikinci_input))
else:
    print ("Yanlış seçim yaptınız.")


