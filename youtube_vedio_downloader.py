from pytube import YouTube

link = input("Enter the link of the video you want to download:  ")
yt = YouTube(link)
videos = yt.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
n = int(input("Enter the number of the video you want to download: "))
videos[n].download()

print("Video downloaded successfully")


 