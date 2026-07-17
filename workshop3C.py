bank = 0
number = 0
count = 1
monney = int(input("วันนี้ต้องไปเก็บเงินทั้งหมดเท่าไหร่ :"))
while True :
    monney_store = (input(f"ยอดเงินที่เก็บมาจากร้าน {count} :"))
    if monney_store == "police" :
        print("ตำรวจมาแล้ว")
        break
    else:
        bank += int(monney_store)
        number += 1.
        count += 1
print(f"จำนวนร้านที่ไปเก็บ {number} ")
print(f"จำนวนเงินทั้งหมดที่ไปเก็บ {bank}")