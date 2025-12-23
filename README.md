# Eksperimen SML - Mikail Thoriq Kariemshah Banowo

Repository ini berisi eksperimen preprocessing data untuk memenuhi submission kelas **Sistem Machine Learning (SML)**.

## 📂 Struktur Folder

```
Eksperimen_SML_Mikail-Thoriq-Kariemshah-Banowo/
│
├── .github/workflows/        # Automasi GitHub Actions
│   └── preprocessing.yml
│
├── titanic_raw/              # Dataset mentah
│   └── titanic.csv
│
├── preprocessing/
│   ├── Eksperimen_Mikail Thoriq Kariemshah Banowo.ipynb  # Notebook Eksperimen Manual
│   ├── automate_Mikail Thoriq Kariemshah Banowo.py       # Script Otomatisasi
│   └── titanic_preprocessing/                            # Hasil Preprocessing
│       └── train_processed.csv
│
├── README.md
└── requirements.txt
```

## 📊 Dataset

Dataset yang digunakan adalah **Titanic Dataset**.

- **Lokasi Raw**: `titanic_raw/titanic.csv`
- **Lokasi Processed**: `preprocessing/titanic_preprocessing/train_processed.csv`

## 🎯 Tujuan Eksperimen

Melakukan eksplorasi data (EDA) dan preprocessing features untuk mempersiapkan data bagi model machine learning. Tahapan meliputi handling missing values, encoding kategorikal features, dan scaling variabels numerik.

## ⚙️ Preprocessing Steps

1. **Handling Missing Values**:
   - `Age`: Diisi dengan mean.
   - `Embarked`: Diisi dengan mode.
2. **Dropping Columns**:
   - `Cabin` (banyak missing values).
   - `Name`, `Ticket`, `PassengerId` (tidak relevan/high cardinality).
3. **Encoding**:
   - One-Hot Encoding untuk `Sex` dan `Embarked`.
4. **Scaling**:
   - StandardScaler untuk `Age` dan `Fare`.

## 🚀 Cara Menjalankan

### 1. Prasyarat

Pastikan `uv` sudah terinstall. Jika belum, install `uv` terlebih dahulu.
Kemudian buat virtual environment dan install dependencies:

```bash
uv venv
source .venv/bin/activate  # atau .venv\Scripts\activate di Windows
uv pip install -r requirements.txt
```

### 2. Menjalankan Notebook (Manual)

Buka file `preprocessing/Eksperimen_Mikail Thoriq Kariemshah Banowo.ipynb` menggunakan Jupyter Notebook atau VS Code.
Pastikan kernel yang digunakan adalah kernel dari virtual environment yang barusan dibuat (`.venv`).

### 3. Menjalankan Script Otomatis

Jalankan perintah berikut di terminal dari root folder project:

```bash
python "preprocessing/automate_Mikail Thoriq Kariemshah Banowo.py"
```

Script ini akan membaca file dari `titanic_raw/` dan menyimpan hasil preprocessing ke `preprocessing/titanic_preprocessing/`.

## 🤖 GitHub Actions

Repository ini dilengkapi dengan CI/CD sederhana menggunakan **GitHub Actions**.

- **Trigger**: Push ke repository.
- **Workflow**: Menginstall dependencies dan menjalankan script `automate_Mikail Thoriq Kariemshah Banowo.py` secara otomatis.
- **Artifact**: Hasil `train_processed.csv` dapat diunduh dari tab Actions di GitHub.
