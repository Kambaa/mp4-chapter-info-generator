#READ FROM https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg

import re

#print(
#  "ADD CHAPTERS TO MP4\nYou will need ffmpeg for this. Download for windows here: https://www.gyan.dev/ffmpeg/builds/"
#)
#print("Run this command to extract ffmetadata from your original video first!")
#print("...")
#print("ffmpeg -i INPUT.mp4 -f ffmetadata FFMETADATAFILE.txt")
#print("...")
#print("...")
#print("After that add your chapters to Chapters.txt")
#print("Example content in Chapters.txt:")
#print("...")

#print(
#  "0:00:00 A question about last day\n0:12:10 Session 1\n1:10:39 10 Min Break\n1:19:22 Session 2\n2:03:49 10 Min Break\n2:12:26 Session #3\n2:49:29 END\n"
#)
#print("...")
#print("Do not forget to add a line with video end time")
#print("...")

chapters = list()

with open('Chapters.txt', 'r') as f:
  for line in f:
    x = re.match(r"(\d):(\d{2}):(\d{2}) (.*)", line)
    hrs = int(x.group(1))
    mins = int(x.group(2))
    secs = int(x.group(3))
    title = x.group(4)

    minutes = (hrs * 60) + mins
    seconds = secs + (minutes * 60)
    timestamp = (seconds * 1000)
    chap = {"title": title, "startTime": timestamp}
    chapters.append(chap)

text = ""

for i in range(len(chapters) - 1):
  chap = chapters[i]
  title = chap['title']
  start = chap['startTime']
  end = chapters[i + 1]['startTime'] - 1
  text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""

# with open("FFMETADATAFILE", "a") as myfile:
# myfile.write(text)

print("Open README.md For Details")
print(
  "Add These to the FFMETADATA.txt file(append it-do not remove or change original text)"
)
#print("...")
#print("...")
print(text)
#print("...")
#print("...")
#print(
#  "Run this command to add a new video file with chapters on it(named `OUTPUT.mp4`): "
#)
#print("...")
#print(
#  "ffmpeg -i INPUT.mp4 -i FFMETADATAFILE.txt -map_metadata 1 -codec copy OUTPUT.mp4"
#)
