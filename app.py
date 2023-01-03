from pytube import YouTube

link = input("enter the link:")

yt = youtube(link)

ys = yt.streams.get_highest_resolution()

print("downloading!....")
ys.download()
print("downloaded")
