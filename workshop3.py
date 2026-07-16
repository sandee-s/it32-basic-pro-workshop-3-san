bank = 0
shop = int(input("วันนี้ต้องไปเก็บกี่ร้าน :"))
for i in range(1,shop+1) :
    monney = int(input(f"ยอดเงินที่เก็บมาจากร้าน {i} :"))
    bank = monney + bank
print(f"จำนวนร้านที่ไปเก็บ {shop} ")
print(f"จำนวนเงินทั้งหมดที่ไปเก็บ {bank}")