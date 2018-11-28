#Mükemmel karma

kartSayisi = int(input("Kart sayısını giriniz: "))
deste = [x+1 for x in range(kartSayisi)]
ilk_deste = deste
sayac = 0

ilkYarım = int(kartSayisi/2)
ikinciYarım = kartSayisi+1
 
while True:
    sag_deste = deste[ilkYarım:ikinciYarım]
    sol_deste = deste[0:ilkYarım]

    deste = []
    for i in zip(sag_deste, sol_deste):
    #for i in zip(sol_deste, sag_deste):
        deste.append(i[0])
        deste.append(i[1])

    sayac = sayac + 1    

    if deste == ilk_deste:
        print(sayac)
        break
    
