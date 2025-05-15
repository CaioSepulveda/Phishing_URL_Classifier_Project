# Phishing URL Classifier 



> **One‑stop showcase** of a  ML pipeline with data preprocessing, model training, packaging with Docker and reproducible instructions.

---

## 📂 Project Structure

```
├── data/
│   └── raw/
│       └── phishing.csv           # original dataset (Kaggle)
├── models/
│   └── phishing_clf.pkl          # trained model
├── notebooks/
│   ├── EDA_preprocessing_And_Training # exploration and feature engineering + Model Training
│   
├── predict.py                    # CLI script for single‑URL prediction
├── requirements.txt              # python packages
├── Dockerfile                    # containerization recipe
└── README.md                     # you are here
```

---

## 🗂️ Dataset

* **Source:** Kaggle – *Phishing Websites Dataset*
* **Target variable:** `Result` (1 = phishing, 0 = legitimate).
* **Basic features engineered** (`url_length`, `has_at`, etc.) plus optional BERT embeddings.

---

## ⚙️ Setup (local)

```bash
# clone repo and enter folder
$ git clone https://github.com/<your-user>/axur-ai-intern-mini-projects.git
$ cd axur-ai-intern-mini-projects

# create virtualenv (Windows cmd shown)
> python -m venv venv
> venv\Scripts\activate

# install dependencies
(venv) > pip install -r requirements.txt

# run notebook for exploration / training
(venv) > python -m notebook
```

---

## 🐳 Quick start with Docker

```bash
# build image (once)
$ docker build -t phishing-clf .

# single‑URL inference
$ docker run phishing-clf "http://example.com"
```

The container prints **`Phishing`** or **`Legitimate`**.

---

## 🔎 Key Results

| Model               | ROC‑AUC | F1‑score |
| ------------------- | ------- | -------- |
| Logistic Regression | 0.91    | 0.88     |
|                     |         |          |

---

## 🚀 How to Re‑train and Update the Image

1. Open `notebooks/2_model_training.ipynb`, tweak hyper‑parameters, run all cells.
2. A new `phishing_clf.pkl` is saved under `models/`.
3. Rebuild image:

```bash
docker build -t phishing-clf .
```

---

---

## 📝 License

MIT — free to use, share, and modify.
