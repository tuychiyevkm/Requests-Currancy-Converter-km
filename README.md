# 💱 Mini Project: Currency Converter (`CBU` API asosida)

## 🎯 Maqsad:

* `requests` kutubxonasi bilan valyuta kurslarini olish
* Foydalanuvchi kiritgan qiymatni `USD`, `EUR`, `UZS` orasida konvertatsiya qilish
* Natijani chiroyli formatda konsolga chiqarish

---

## 🔗 API manzili (CBU Uz):

```
https://cbu.uz/uz/arkhiv-kursov-valyut/json/
```

Bu API JSON ko‘rinishida quyidagi kabi ma’lumot qaytaradi:

```json
[
  {
    "Ccy": "USD",
    "CcyNm_UZ": "AQSH dollari",
    "Rate": "12750.33",
    "Date": "25.07.2025"
  },
  ...
]
```

---

## 🧩 Project structure: `converter.py`

### 🔹 Step 1: Kurslarni olish

* API'dan so‘rov yuboriladi
* USD va EUR uchun `Rate` qiymatlari ajratiladi
* `float` ga aylantiriladi

### 🔹 Step 2: Foydalanuvchi interfeysi (input)

* Foydalanuvchidan:

  * **miqdor** (son)
  * **valyuta turi** (`USD`, `UZS`, `EUR`)
  * **aylantiriladigan valyuta** (`USD`, `UZS`, `EUR`) so‘raladi

### 🔹 Step 3: Hisoblash

* Masalan:

  * `100 USD → UZS` → `100 * USD_Rate`
  * `127500 UZS → USD` → `127500 / USD_Rate`

### 🔹 Step 4: Natijani chiqarish

* `100 USD = 1,275,000 UZS` ko‘rinishida chiroyli chiqarilsin

---

## ✅ Vazifa topshirig‘i

### 📋 **Talablar:**

1. API’dan so‘rov yuboring.
2. USD va EUR kurslarini ajrating.
3. Foydalanuvchidan input oling: miqdor, valyuta, konvertatsiya yo‘nalishi.
4. Hisoblab, natijani ekranga chiqaring.
5. Har safar ishga tushganda eng so‘nggi kurslar ishlatilishi kerak.

---

## 💡 Misol ishlash:

```bash
$ python converter.py
Enter amount: 100
From currency (USD, UZS, EUR): USD
To currency (USD, UZS, EUR): UZS

✅ 100 USD = 1,275,000.00 UZS (25.07.2025)
```
currency_converter
│               
├── services/
│   └── exchange.py         
│
├── utils/
│   └── converter.py        
│
├── interface/
│   └── cli.py              
├── main.py  
└── __init__.py             
