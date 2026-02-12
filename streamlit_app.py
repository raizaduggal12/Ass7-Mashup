import streamlit as st
import os
import zipfile
import smtplib
from email.message import EmailMessage
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

st.title("🎵 Mashup Web Service")

# ---------- INPUT FORM ----------
singer = st.text_input("Singer Name")
num_videos = st.number_input("# of videos", min_value=1, step=1)
duration = st.number_input("Duration (sec)", min_value=1, step=1)
email = st.text_input("Email ID")

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


# ---------- ZIP ----------
def zip_file(file_path):
    zip_name = "mashup.zip"
    with zipfile.ZipFile(zip_name, "w") as z:
        z.write(file_path)
    return zip_name


# ---------- EMAIL ----------
def send_email(receiver, zip_path):
    sender = "raizaduggal1@gmail.com"
    password = "ibxxbrncfwwffkey"

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


# ---------- BUTTON ----------
if st.button("Generate Mashup"):

    if num_videos <= 10 or duration <= 20:
        st.error("Inputs must be >10 videos and >20 sec")
    else:
        with st.spinner("Creating mashup and sending email..."):
            mashup = create_mashup(int(num_videos), int(duration))
            zip_path = zip_file(mashup)
            send_email(email, zip_path)

        st.success("✅ Mashup sent to your email!")
