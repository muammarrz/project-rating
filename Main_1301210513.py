file = open("teks_tubes.txt",'r')   #membuka file teks
baca_file = file.readlines()      #membaca file dengan built-in function dengan fungsi readlines
file.close()                        #menutup file agar tidak terjadi error

from fileinput import filename      #mengimpor file

#membuat fungsi untuk membaca data
def baca_data(filename):
    file_text = open(filename, "r")
    
    listk = []       #membuat list kosong
    teks = file_text.readline().replace("\n","").split()    #menjadikan teks sebagai list
    while teks:
        dictk = {"Unit": teks[0]}
        k = 1
        for i in teks[1:]:
            dictk["Spek " + str(k)] = i
            k += 1
        listk.append(dictk)
        teks = file_text.readline().replace("\n","").split() # Jadi list

    file_text.close()
    return listk
nama_file = "teks_tubes.txt"
print(baca_data(nama_file))

rating_mobil = ['tipe','Spesifikasi 1','Spesifikasi 2','Spesifikasi 3','Spesifikasi 4','Spesifikasi 5']
rating = []

for elemen in baca_file:
    list_data = elemen.replace('\n', '').split(' ')
    ratingdict = {}
    for i in range(len(list_data)):
        ratingdict[rating_mobil[i]] = list_data[i]
    rating.append(ratingdict)

#fungsi untuk mencari nilai terbaik
def terbaik(spek):
    for i in range(len(rating)):
        a = (int(rating[i].get(spek)))
        if (a == 8):
            print(rating[i].get('tipe'))
        
#fungsi untuk mencari rata-rata rating di atas 7
def report():
    for i in range(len(rating)):
        jumlah = 0
        for j in range(len(rating)):
            k = (int(rating[i].get(rating_mobil[j+1])))
            jumlah = jumlah + k
            rata_rata = jumlah/(len(rating))
            if (rata_rata > 7) :
                print(rating[i].get('tipe'))

#main program
#memanggil fungsi terbaik
print('rating tertinggi pada spesifikasi 1:')
terbaik('Spesifikasi 1')
print('\n')

print('rating tertinggi pada spesifikasi 2:')
terbaik('Spesifikasi 2')
print('\n')

print('rating tertinggi pada spesifikasi 3:')
terbaik('Spesifikasi 3')
print('\n')

print('rating tertinggi pada spesifikasi 4:')
terbaik('Spesifikasi 4')
print('\n')

print('rating tertinggi pada spesifikasi 5:')
terbaik('Spesifikasi 5')
print('\n')

#memanggil fungsi report
print('kendaraan dengan rata-rata rating diatas 7:')
report()
