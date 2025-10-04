# 📘 Trade Engine

> 🇵🇱 **Polish version available here:** [README_PL.md](README_PL.md)

---

## 📈 Overview

**Trade Engine** is a web application built with **Django**, designed to simulate a simplified investment and trading system.  
It allows users (investors) to **buy and sell assets** such as stocks, currencies, and commodities, while administrators can **manage the market** — adding, removing, and updating asset prices.

The project follows the **Model-View-Template (MVT)** architecture with a strong focus on backend functionality — transaction logic, data relationships, and efficient data management.

---

## 🚀 Main Backend Features

### 🧩 Data Models
The project is based on five core models:

1. **AssetType** – defines the type of asset (e.g., stocks, commodities, currencies).  
2. **Asset** – represents a single tradable asset with a name, type, and current price.  
3. **Investor** – a user model inheriting from `AbstractUser`, extended with balance and owned assets.  
4. **Holding** – an intermediate model linking an investor with assets, storing the **quantity** of each owned asset.  
5. **Order** – represents a buy or sell transaction, including investor, asset, quantity, total value, and timestamp.

---

## ⚙️ Business Logic

- **Buying and Selling Assets** – investors can purchase or sell available assets.  
  The transaction value is dynamically calculated as `price × quantity`.  
- **Balance Management** – investor balance is automatically updated after every transaction.  
- **Holdings Tracking** – the `Holding` model ensures accurate tracking of each investor’s owned assets and quantities.  
  When all units of an asset are sold, the corresponding record in `Holding` is automatically removed.  
- **Market Administration** – administrators can create, update, or delete assets and asset types directly from the interface or Django Admin Panel.

---

## 🔐 Test Investor Account

To try out the application without registration, log in using the demo account:

### login: TestInvestor
### password: zaq1@wsx

You’ll gain access to full investor functionality — browsing assets, performing buy/sell actions, and managing your balance.

---

## 🖥️ User Interface

The frontend uses the **Material Kit for Django** theme, customized to match the project’s design.  
Through the interface, users can:

- Browse assets and their types  
- View the list of investors and account details  
- Perform operations like **Buy**, **Sell**, **Update**, and **Delete**  
- Edit their **balance** and **password**

Each model includes a dedicated `ListView` and `DetailView`, and all changes are stored automatically in the database.

---

## 🧠 Technologies

- **Python 3.13+**  
- **Django 5.x**  
- **SQLite** (default) or any Django-compatible database  
- **Bootstrap / Material Kit**  
- **HTML, CSS, JavaScript (Django Templates)**

---

## ⚙️ How to Run the Project

Follow the steps below to set up and run the application locally:

```bash
# 1. Clone the repository
git clone https://github.com/<your_repo>/trade_engine.git

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

Then open your browser and visit:

http://127.0.0.1:8000/

## 👨‍💻 Author & License

Bartosz Okrój

This project was developed for educational purposes.
It can be freely modified, expanded, and used for further development or learning.
---

