# Bank Account Management

Bu loyiha Python’da **Inkapsulyatsiya** va **Polimorfizm** tushunchalarini amalda ko‘rsatish uchun yaratilgan. Loyihada turli xil bank hisob turlari (SavingsAccount va CheckingAccount) bilan ishlash ko‘rsatiladi.

---

## Xususiyatlar

- **BankAccount** klassi:
  - Balansni maxfiy (`__balance`) o‘zgaruvchi sifatida saqlaydi.
  - `deposit(amount)` – balansga mablag‘ qo‘shadi.
  - `withdraw(amount)` – mablag‘ni yechib oladi.
  - `get_balance()` – balansni qaytaradi.

- **SavingsAccount**:
  - `withdraw` metodi orqali pul yechilganda foiz (bonus) hisoblab beradi.

- **CheckingAccount**:
  - `withdraw` metodi orqali overdraft (manfiy balans) imkoniyati mavjud.
  - Overdraft limiti bilan balansdan ko‘p yechib olish mumkin.

---

## Polimorfizm

Barcha hisob turlari bir ro‘yxatga joylashtiriladi va polimorfik tarzda `withdraw` metodi chaqiriladi. Shunday qilib, turiga qarab tegishli metod avtomatik ishlaydi.

---

## Misol

```python
# Hisoblarni yaratish
acc1 = SavingsAccount(1000)
acc2 = CheckingAccount(500)

# Barchasini ro'yxatga joylashtirish
accounts = [acc1, acc2]

# Polimorfik tarzda withdraw
for account in accounts:
    account.withdraw(200)
    print(f"Balance now: {account.get_balance()}\n")
