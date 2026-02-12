# 🎵 Mashup Web Service Assignment

## 🔗 Deployed Web App
👉 https://mashup-h5qk.onrender.com/

This project generates a **music mashup** from multiple videos and sends the final audio file to the user via **email**.

---

# 📌 Project Structure

This assignment contains **two parts**:

## 🟢 Part 1 — CLI Python Program

A **command-line Python script** named:

```
<ROLLNO>.py
```

### Functionality
- Accepts:
  - Singer name  
  - Number of videos  
  - Duration of each clip  
  - Email ID  
- Downloads videos  
- Extracts audio using **MoviePy**
- Trims clips using **Pydub**
- Combines clips into a **single mashup**
- Sends mashup via **email**

### Technologies Used
- Python  
- MoviePy  
- Pydub  
- SMTP Email  

---

## 🌐 Part 2 — Web Application

A **Flask web app** (`web_mashup.py`) that provides a **user interface** for the same mashup process.

### Features
- Web form input:
  - Singer name  
  - Number of videos  
  - Duration  
  - Email  
- Backend processing:
  - Audio extraction  
  - Mashup creation  
  - ZIP generation  
  - Email delivery  

### Deployment
The web app is deployed on **Render**:

👉 https://mashup-h5qk.onrender.com/

---

# 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Audio Processing:** MoviePy, Pydub
- **Email Service:** SMTP (Gmail App Password)
- **Deployment:** Render Cloud
- **Version Control:** GitHub

---

# ▶️ How to Run Locally

## 1️⃣ Clone repository

```bash
git clone https://github.com/raizaduggal12/Mashup-Assignment.git
cd Mashup-Assignment
```

## 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Run CLI version

```bash
python <ROLLNO>.py
```

## 4️⃣ Run Web App

```bash
python web_mashup.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# ☁️ Deployment Details (Render)

### Build Command
```
pip install -r requirements.txt
```

### Start Command
```
gunicorn web_mashup:app
```

⚠️ Heavy audio processing is **disabled on cloud** to avoid timeout/memory limits.  
✔ Full mashup functionality works **locally**.

---

# 📷 Screenshots

## 🖥️ Web App Interface
*(Add screenshot here)*

## 📤 Email with Mashup
*(Add screenshot here)*

## 💻 CLI Execution
*(Add screenshot here)*

---

# 👩‍💻 Author

**Name:** Raiza Duggal  
**Course:** B.Tech Computer Science  
**Assignment:** Mashup Generation using Python & Flask  

---

# ✅ Conclusion

This project demonstrates:

- Python audio processing  
- CLI + Web integration  
- Email automation  
- Cloud deployment  

It provides a **complete end-to-end mashup generation system**.

---

# 📸 Important for Submission

You must **add 3 screenshots** in the repository:

1. **Web app page**
2. **Email received with mashup.zip**
3. **CLI running in terminal**

After uploading screenshots, replace:

```
*(Add screenshot here)*
```

with:

```md
![Web App](screenshots/web.png)
![Email](screenshots/email.png)
![CLI](screenshots/cli.png)
```
