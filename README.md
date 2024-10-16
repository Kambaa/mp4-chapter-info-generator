# Add Chapters To Mp4 Files.

Read and used code from https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg
replit-code: https://replit.com/@d47im5e/MP4-chapter-information-generator

## Prerequisites:

- You will need to get ffmpeg for running commands written below on your machine. Get for windows [here](https://www.gyan.dev/ffmpeg/builds/ ), [direct download here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)
- For ease of use, i recommend extracting the ffmpeg zip to a directory and adding /bin folder to your enviroment variables. [Read and do as this tutorial says.](https://phoenixnap.com/kb/ffmpeg-windows)

## Usage
 
- Write your chapter times and labels to Chapters.txt like this(last line should be end time of your video):

```
0:00:00 Start
0:12:10 Chapter 1
1:10:39 Chapter 2
1:19:22 Chapter 3
2:03:49 Chapter 4
2:12:26 Chapter 5
2:49:29 END
```

- Do not forget to end with _**video end time**_

- Run main.py and copy generated codes written in console. For example:  
  
```
[CHAPTER]
TIMEBASE=1/1000
START=0
END=729999
title=Start

[CHAPTER]
TIMEBASE=1/1000
START=730000
END=4238999
title=Chapter 1

[CHAPTER]
TIMEBASE=1/1000
START=4239000
END=4761999
title=Chapter 2

[CHAPTER]
TIMEBASE=1/1000
START=4762000
END=7428999
title=Chapter 3

[CHAPTER]
TIMEBASE=1/1000
START=7429000
END=7945999
title=Chapter 4

[CHAPTER]
TIMEBASE=1/1000
START=7946000
END=10168999
title=Chapter 5
```
- Run the command below. This will generate FFMETADATAFILE.txt file with your original video's metadata.

`ffmpeg -i YOURVIDEO.mp4 -f ffmetadata FFMETADATAFILE.txt`

- Open FFMETADATA.txt file and add these generated codes at the bottom (append them - meaning add new line at end of the file and paste them), do not change original text
- Run this command to generate a new video with chapters on it(named `OUTPUT.mp4`):

`ffmpeg -i INPUT.mp4 -i FFMETADATAFILE.txt -map_metadata 1 -codec copy OUTPUT.mp4`

- Check your glorious work and have a nice watching session. 
