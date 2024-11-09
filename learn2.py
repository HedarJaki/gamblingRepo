banyak_data = int(input("banyak data: "))
banyak_voucher = 2
for i in range(banyak_data):
    total_harga = float(input("masukkan total harga: ")) 
    if total_harga >= 30000 and banyak_voucher > 0 : 
        potongan_harga = 0.3
        harga_bayar = 1 - potongan_harga # baris pertama
        total_harga *= harga_bayar # baris kedua
        banyak_voucher -= 1
    pajak = 0.1 # pajak dalam persen ~ 10%
    #pajak_bayar = pajak * total_harga # baris ketiga 
    #total_harga += pajak_bayar # baris ke-4
    total_harga = total_harga * (1 + pajak) 
    if total_harga % 1 == 0 : 
        total_harga = int(total_harga)
    print("total tagihan pembayaran adalah sebesar:", total_harga )