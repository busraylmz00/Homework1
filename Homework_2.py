
my_number = 50
max_number = 100

user_forecast = int (input ("1-100 arasında bir sayı tuttum. Bu sayıyı bilebilir misin?"))
while user_forecast > max_number :
    print ("Lütfen 1-100 arasında sayı giriniz.")
    break
while user_forecast > my_number and user_forecast < max_number :
    print("Lütfen daha küçük sayı tahmin ediniz.\nTekrar deneyiniz...")
    break
while  user_forecast < my_number :
    print ("Lütfen daha büyük sayı tahmin ediniz.\nTekrar deneyiniz...")
    break
while user_forecast == my_number :
    print("Tebrikler! Doğru tahmin ettiniz.\nProgram kapatılıyor...")
    break









