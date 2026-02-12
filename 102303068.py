import sys
import os
from moviepy.editor import AudioFileClip
from pydub import AudioSegment

# ---------- CHECK ARGUMENTS ----------
if len(sys.argv) != 5:
    print("Usage: python <file.py> <SingerName> <NoOfVideos> <DurationSec> <OutputFile>")
    sys.exit()

singer = sys.argv[1]
num_videos = int(sys.argv[2])
duration = int(sys.argv[3])
output_file = sys.argv[4]

if num_videos <= 10 or duration <= 20:
    print("Error: Number of videos must be >10 and duration >20 sec")
    sys.exit()

# ---------- CREATE FOLDERS ----------
os.makedirs("audio", exist_ok=True)
os.makedirs("clips", exist_ok=True)

# ---------- READ DOWNLOADED VIDEOS ----------
video_folder = "downloads"
video_files = os.listdir(video_folder)[:num_videos]

audio_clips = []

print("Processing downloaded videos...")

for i, video in enumerate(video_files):
    try:
        video_path = os.path.join(video_folder, video)
        audio_path = f"audio/audio{i}.mp3"

        # Convert video → audio
        AudioFileClip(video_path).write_audiofile(audio_path, verbose=False, logger=None)

        # Cut first Y seconds
        sound = AudioSegment.from_mp3(audio_path)
        clip = sound[: duration * 1000]

        clip_path = f"clips/clip{i}.mp3"
        clip.export(clip_path, format="mp3")

        audio_clips.append(AudioSegment.from_mp3(clip_path))

    except Exception as e:
        print("Error processing:", video, e)

# ---------- MERGE ALL CLIPS ----------
print("Merging clips...")
final_audio = AudioSegment.empty()

for clip in audio_clips:
    final_audio += clip

final_audio.export(output_file, format="mp3")

print("Mashup created successfully:", output_file)
