import os
try:
    from pytube import Playlist, YouTube
    from art import *
except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install art')
tprint("ytbl2mp3bot")
print("made in Vietnam, by Imsohuy")
print("---------------------------")

# create a function to download mp3 from playlist
def get_playlist(playlists):
    print(playlists)
    urls = []
    # iteratively get watch links from playlist
    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            try:
                urls.append(url)
                video = YouTube(url)
                #extract audio only
                audio = video.streams.filter(only_audio=True).first()

                #destion for download, replace where u want to save
                des = "C:/Users/asus/Desktop/music"

                #create title
                title = audio.title
                title = title.replace("(Lyric Video)", "")
                title = title.replace("(Official)", "")
                title = title.replace("(Official Video)", "")
                title = title.replace("(Official HD Video)", "")
                title = title.replace("(Official Music Video)", "")
                title = title.replace("[Official Music Video]", "")
                title = title.replace("[Official Music Video]", "")
                title = title.replace("OFFICIAL MUSIC VIDEO", "")

                # download the file
                out_audio = audio.download(output_path=des, filename=title + ".mp3")

                #result
                print(title + " downloaded!")
            except:
                print(title + " error! Skip!")

# main code
playlist = ["https://www.youtube.com/playlist?list=PLyPDCUrqti684QwRHgXka07WK2xKJUbbx"]
pl_urls = get_playlist(playlist)