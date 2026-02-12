# 🎵 Mashup Web Service Assignment

## 🔗 Deployed Web App
👉 https://mashup-h5qk.onrender.com/

This project generates a **music mashup** from multiple videos and sends the final audio file to the user via **email**.

---

#  Project Structure

This assignment contains **two parts**:

## 🟢 Part 1 — CLI Python Program

A **command-line Python script** named:

```
102303068.py
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

# 📷 Screenshots

## 🖥️ Web App Interface
![Web App](images/app.png)

## 📤 Email with Mashup
![Email Output](images/email.png)

## 💻 CLI Execution
![CLI Output](images/cli.png)


---

# 📁 Project Structure

```
Mashup-Assignment/
│
├── audio/                 # Temporary extracted audio files
├── clips/                 # Trimmed audio clips
├── downloads/             # Downloaded source videos│
├── 102303068.py           # Part 1: CLI mashup generator
├── web_mashup.py          # Part 2: Flask web application│
├── mashup.mp3             # Generated mashup output
├── mashup.zip             # Zipped mashup for email sendingfor Part1│
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version for Render
├── render.yaml            # Render deployment config (optional)│
├── README.md              # Project documentation
└── LICENSE                # License file
```


#  Conclusion

This project demonstrates:

- Python audio processing  
- CLI + Web integration  
- Email automation  
- Cloud deployment  

It provides a **complete end-to-end mashup generation system**.

---


# 👩‍💻 Author

**Name:** Raiza Duggal  

---


