def decimalToBinary(n):
    return bin(n).replace("0b", "")
def countup(n):
    if n >= 0:
        countup(n-1)
        print("-----------Sayı Değeri----------------")
        print(n)
        print("----------Binary Değeri-----------------")
        print(decimalToBinary(n))
        print("-----------Binary Değeri İçin MSB Değeri----------------")
        mbsValue=decimalToBinary(n)
        print(mbsValue[0])
n=int(input("Bir sayı giriniz::"))  
countup(n)
