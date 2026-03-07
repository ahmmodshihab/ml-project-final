# 🎓 Student Exam Performance Indicator

This is a **Machine Learning** web application built with **Flask** and deployed on **Render**. The application predicts a student's **Math Score** based on several demographic and academic factors using regression algorithms.

## 🚀 Live Demo
You can access the live application here: https://perfomance-indicator.onrender.com

## 🛠️ Tech Stack
* **Language:** Python 🐍
* **Web Framework:** Flask 🌐
* **Machine Learning:** Scikit-learn, Pandas, NumPy, CatBoost, XGBoost
* **Frontend:** HTML5, CSS3, Bootstrap 5 🎨
* **Deployment:** Render 🚀

## 📊 Features
* **Modern UI:** Clean and responsive interface inspired by professional dashboards.
* **Accurate Prediction:** Uses advanced regression models to predict scores.
* **Precision Control:** Displays results rounded to 2 decimal places for better readability.
* **Error Handling:** Custom exception handling for robust performance.

## 📋 How to Run Locally
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ahmmodshihab/ml-project-final.git
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python app.py
    ```
5.  Open `http://127.0.0.1:5000/` in your browser.

## 🗂️ Project Structure
* `app.py`: The main Flask application entry point.
* `src/`: Contains the ML pipeline, including data ingestion, transformation, and model training.
* `templates/`: HTML files for the Home and Prediction pages.
* `requirements.txt`: List of required libraries with specific versions for deployment stability.

---
Made with ❤️ by Shihab