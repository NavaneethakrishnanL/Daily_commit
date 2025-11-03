from moviepy.editor import VideoFileClip

# Load your video
clip = VideoFileClip("input.mp4")

# Reverse both video and audio
reversed_clip = clip.fx(vfx.time_mirror)

# Save the reversed video
reversed_clip.write_videofile("reversed_output.mp4", codec="libx264", audio_codec="aac")
