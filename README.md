# 🛍️ Zara Web Automation Tests (Playwright + Pytest)

This project contains end-to-end UI automation tests for the **Zara** website, written in **Python** using **Playwright** and **Pytest**.

The goal of the project is to validate core e-commerce user flows such as:
- searching for products
- adding/removing items from the shopping bag
- changing store region

The project follows the **Page Object Model (POM)** pattern to keep tests clean, reusable, and maintainable.

---

## 🧰 Tech Stack

- **Python 3.9+**
- **Playwright (Python)**
- **Pytest**
- **python-dotenv**
- **Git**

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone (https://github.com/gal-ben-david/automation_project.git)
cd automation_project
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Install Playwright browsers
```bash
playwright install
```
---

## 🌍 Environment Variables

Create a .env file based on .env.example.

Example:

BASE_URL=https://www.zara.com/il/en/
HEADLESS=false
BROWSER=chromium
TIMEOUT=15000
LOCALE=en-US

---

##  ▶️ Running Tests

Run all tests

```bash
pytest
```



