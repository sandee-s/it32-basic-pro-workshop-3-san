bank = 0
number = 0
count = 1
monney = int(input("วันนี้ต้องไปเก็บเงินทั้งหมดเท่าไหร่ :"))
while bank < monney :
    monney_store = int(input(f"ยอดเงินที่เก็บมาจากร้าน {count} :"))
    bank += monney_store
    number += 1.
    count += 1
    if bank >= monney :
        break
print(f"จำนวนร้านที่ไปเก็บ {number} ")
print(f"จำนวนเงินทั้งหมดที่ไปเก็บ {bank}")
