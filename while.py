print("welcome")
banyak_voucher = int(input("jumlah voucher:"))
banyak_data = int(input("banyak data: "))
list_belanja= [] #list
def belanjaan_terbanyak(): 
    termahal= max(list_belanja)
    return termahal  
def menu():
    print("pilih menu")
    print("1. belanjaan terbanyak")
    print("2. cek belanja ke-berapa")
    print("0. Exit")
    opsi= int(input())
    if opsi== 0:
        return
    elif opsi== 1:
        if banyak_data== 1:
            print(list_belanja)
        else: 
            print(belanjaan_terbanyak)
        menu()
    elif opsi== 2:
        nomer_urut_belanja = int(input("cek belanjaan ke berapa: ")) 
        print(list_belanja[nomer_urut_belanja-1]) #indexing of list
        menu()
    #print("daftar harga belanjaan bulan ini: ",list_belanja)
    else:
        print("pilihan menu tidak tersedia")
        menu()
while banyak_data > 0 :
    total_harga = float(input("masukkan total harga: ")) 
    if total_harga >= 30000 and banyak_voucher > 0 : 
        potongan_harga = 0.3
        harga_bayar = 1 - potongan_harga # baris pertama
        total_harga *= harga_bayar # baris kedua
        banyak_voucher -= 1
    pajak = 0.1 # pajak dalam persen ~ 10%
    """
    pajak_bayar = pajak * total_harga # baris ketiga 
    total_harga += pajak_bayar # baris ke-4
    """
    total_harga = int(total_harga * (1 + pajak))
    """
    if total_harga % 1 == 0 : 
        total_harga = int(total_harga)
    """
    list_belanja.append(total_harga)
    print(total_harga)
    banyak_data -= 1
print(list_belanja)
menu()
