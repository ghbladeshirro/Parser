# 🚀 Парсер для pricing.parts

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green?logo=selenium)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange?logo=pandas)

Парсер на Python для сбора данных о запчастях с сайта [pricing.parts](https://pricing.parts) и экспорта в Excel.

- Пример для фриланса

---
## Процесс
![py_5ORjqeiVhw](https://github.com/user-attachments/assets/0709042d-e4c3-46a4-8ee0-c6be267388d9)
## Итог
![EXCEL_Dwh54EyzLN](https://github.com/user-attachments/assets/1d56f84b-bfdb-4678-8c21-a3dec681bb50)

---

## ✨ Описание
- **Парсинг** с использованием `undetected-chromedriver`
- **Многостраничный сбор данных**
- **Экспорт в Excel** с:
  - Названиями брендов
  - Номерами запчастей
  - Описаниями
  - Ценами (мин/макс в рублях)
- **Логирование прогресса** в консоль

---

### 🛠 Зависимости

- Браузер Chrome
- Python 3.8+

```bash
pip install undetected-chromedriver selenium pandas openpyxl
