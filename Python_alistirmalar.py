### Python Alistirmalari###
# Görev 1: Verilen değerlerin veri yapılarını inceleyiniz.(Type() metodunu kullanınız.)

x = 8
y = 3.2
z =  8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1,2,3,4]
d = {"Name":"jake","Age":27,"Adress":"Downtown"}
t = ("Machine Learning", "Data Science")
s = {"python","Machine Learning", "Data Science"}

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
type(text)

text= text.replace(","," ").replace("."," ")
text = text.upper().split()
print(text)

# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D","A","T","A","S","C","İ","E","N","C","E"]

#Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)

#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız

print(lst[0],lst[10])

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

print(lst[0:4])

# Adım 4: Sekizinci indeksteki elemanı siliniz.

del lst[8]
print(lst)
# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("S")
print(lst)

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8,"N")
print(lst)

#Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız

dict = {"Christian":["America",18],
        "Daisy":["England",12],
        "Antonio":["Spain",22],
        "Dante":["Italy",25]}
#Adım 1: Key değerlerine erişiniz.

keys = dict.keys()
print(keys)

# Adım 2: Value'lara erişiniz.

values = dict.values()
print(values)

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict.update({"Daisy":["England",13]})

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz

dict.update({"Ahmet":["Turkey",24] })
dict

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict["Antonio"]

#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
#return eden fonksiyon yazınız.

l= [2,13,18,93,22]

odd_numbers = []
even_numbers = []

def func (l):
   for i in l:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    return even_numbers,odd_numbers

odd_numbers,even_numbers = func(l)


print("Çift sayılar: ", even_numbers)
print("Tek sayılar: ", odd_numbers)

#Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
#bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
#tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i, ogrenci in enumerate(ogrenciler):
    if i < 3:
        print(f"Mühendislik Fakültesi {i+1}. öğrencisi: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {i-2}. öğrencisi: {ogrenci}")

#Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
#almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu= ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan =[30,75,150,25]

for ders, krd, kont in zip(ders_kodu, kredi, kontenjan):
    print(f" {krd} kredisi olan {ders} kodlu dersin kontenjanı {kont} kişidir.")


#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
#eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1= set(["data","python"])
kume2= set(["data","function","qcut","lamda","python","miuul"])

kume1.issuperset(kume2) #1. küme 2. kümeyi kapsıyor mu ?

kume1.intersection(kume2) # ortak elemanları kesişimleri...

kume2.difference(kume1) # küme 2 nin küme 1 den faklı olan elemanları...