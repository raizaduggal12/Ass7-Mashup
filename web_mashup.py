from flask import Flask, request, render_template_string
import os
import zipfile
import smtplib
from email.message import EmailMessage
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

app = Flask(__name__)

# ---------- IMPROVED HTML UI ----------
HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
<title>Mashup Web Service</title>

<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
}

.container {
    width: 480px;
    margin: 80px auto;
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.2);
    text-align: center;
}

table {
    margin: auto;
}

td {
    padding: 10px;
    text-align: left;
}

input {
    width: 220px;
    padding: 6px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: orange;
    border: none;
    padding: 8px 18px;
    font-size: 14px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: darkorange;
}

.msg {
    margin-top: 15px;
    font-weight: bold;
    color: green;
}

.error {
    color: red;
}
</style>
</head>

<body>

<div class="container">
    <h2>Mashup Web Service</h2>

    <form method="POST">
        <table>
            <tr>
                <td>Singer Name</td>
                <td><input name="singer" required></td>
            </tr>

            <tr>
                <td># of videos</td>
                <td><input name="videos" type="number" required></td>
            </tr>

            <tr>
                <td>Duration (sec)</td>
                <td><input name="duration" type="number" required></td>
            </tr>

            <tr>
                <td>Email ID</td>
                <td><input name="email" type="email" required></td>
            </tr>

            <tr>
                <td></td>
                <td><button type="submit">Submit</button></td>
            </tr>
        </table>
    </form>

    {% if msg %}
        <p class="msg">{{msg}}</p>
    {% endif %}
</div>

</body>
</html>
"""

# ---------- CREATE MASHUP ----------
def create_mashup(num_videos, duration, output_file="mashup.mp3"):
    video_folder = "downloads"
    video_files = os.listdir(video_folder)[:num_videos]

    audio_clips = []

    for i, video in enumerate(video_files):
        video_path = os.path.join(video_folder, video)
        audio_path = f"audio/audio{i}.mp3"

        AudioFileClip(video_path).write_audiofile(audio_path, verbose=False, logger=None)

        sound = AudioSegment.from_mp3(audio_path)
        clip = sound[: duration * 1000]

        clip_path = f"clips/clip{i}.mp3"
        clip.export(clip_path, format="mp3")

        audio_clips.append(AudioSegment.from_mp3(clip_path))

    final_audio = AudioSegment.empty()
    for clip in audio_clips:
        final_audio += clip

    final_audio.export(output_file, format="mp3")
    return output_file


# ---------- ZIP FILE ----------
def zip_file(file_path):
    zip_name = "mashup.zip"
    with zipfile.ZipFile(zip_name, "w") as z:
        z.write(file_path)
    return zip_name


# ---------- SEND EMAIL ----------
def send_email(receiver, zip_path):
    sender = "raizaduggal1@gmail.com"
    password = "ibxxbrncfwwffkey"   # Gmail App Password

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup File"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content("Attached is your mashup zip file.")

    with open(zip_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="zip", filename="mashup.zip")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)


# ---------- ROUTE ----------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            singer = request.form["singer"]
            num_videos = int(request.form["videos"])
            duration = int(request.form["duration"])
            email = request.form["email"]

            if num_videos <= 10 or duration <= 20:
                return render_template_string(HTML_FORM, msg="Invalid inputs! Must be >10 videos and >20 sec.")

            mashup = create_mashup(num_videos, duration)
            zip_path = zip_file(mashup)
            send_email(email, zip_path)

            return render_template_string(HTML_FORM, msg="Mashup sent to email successfully!")

        except Exception as e:
            return render_template_string(HTML_FORM, msg=f"Error: {str(e)}")

    return render_template_string(HTML_FORM, msg="")


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

