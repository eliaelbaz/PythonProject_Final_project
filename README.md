📌 ML API Project

פרויקט זה מממש שרת API באמצעות FastAPI לניהול משתמשים, טוקנים ואימון מודלים פשוטים של Machine Learning. בנוסף, קיים לוח בקרה גרפי (Streamlit) לניהול ויזואלי של משתמשים ומודלים.

📂 מבנה הפרויקט
main.py                 # קובץ ראשי – מרים את השרת
database.py             # חיבור למסד נתונים (SQLite)
user_model.py           # מודלים לוגיים של משתמשים
user_service.py         # לוגיקה עסקית של משתמשים
user_router.py          # ניתוב בקשות API של משתמשים
ml_model.py             # מודלים של Machine Learning
ml_service.py           # לוגיקה עסקית לאימון/חיזוי
ml_router.py            # ניתוב בקשות API של ML
streamlit_dashboard.py  # לוח בקרה גרפי (Streamlit)
requirements.txt        # ספריות נדרשות
server.log              # לוגים של פעולות
ml_server.db            # מסד נתונים SQLite
uploads/                # תיקייה להעלאת CSV
models_store/           # שמירת מודלים שאומנו

⚙️ התקנה
pip install -r requirements.txt

🚀 הפעלת ה־API
uvicorn main:app --reload


כתובת ראשית: http://127.0.0.1:8000/

תיעוד (Swagger): http://127.0.0.1:8000/docs

📊 הפעלת לוח הבקרה
streamlit run streamlit_dashboard.py


כתובת: http://localhost:8501

✅ מה הפרויקט יודע לעשות

יצירת משתמשים והוספת טוקנים.

מחיקת משתמשים ובדיקת יתרת טוקנים.

העלאת קובצי CSV ואימון מודלים.

הצגת מודלים שאומנו.

ביצוע חיזוי (Prediction) עם נתוני JSON.

לוח בקרה גרפי לניהול משתמשים ומודלים.
