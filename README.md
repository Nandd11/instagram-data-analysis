# Instagram Data Parsing & Analysis (Pure Python)

A Python project that parses Instagram-style raw text data, cleans it, converts it into structured JSON, and performs analysis to extract insights like:

- Most followed profile
- Profile with maximum posts
- Profile following the most users
- Category distribution

This repository contains **both**:
- ✅ A runnable script version (`main.py`)
- ✅ A Jupyter notebook (`notebooks/instagram_data_parsing_analysis.ipynb`)

---

## 🚀 Features
- Parse unstructured raw text records
- Clean & normalize fields
- Store structured data as JSON
- Run analytics (top accounts, category counts)
- Export cleaned CSV

---

## 📂 Project Structure
```txt
instagram-data-analysis/
│── main.py
│── src/
│   ├── parser.py
│   ├── analysis.py
│   └── utils.py
│── notebooks/
│   └── instagram_data_parsing_analysis.ipynb
│── data/
│   ├── initialdata.txt
│   ├── finaldata.csv
│   └── data.json
│── README.md
│── requirements.txt
│── .gitignore
│── LICENSE
```

---

## ⚙️ Installation
```bash
git clone https://github.com/Nandd11/instagram-data-analysis.git
cd instagram-data-analysis
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Run (Script Mode)
```bash
python main.py
```

It will:
1) Parse `data/initialdata.txt`
2) Create `data/data.json`
3) Create `data/finaldata.csv`
4) Print analytics summary

---

## 🧪 Example Output
```txt
Total profiles: 150
Top by followers: user_abc (1,200,000)
Top by posts: user_xyz (12,430)
Top by following: user_pqr (7,210)

Category distribution:
Blogger: 42
Fitness: 31
Business: 21
...
```

---

## 👤 Author
**Nand Patel**  
GitHub: https://github.com/Nandd11
