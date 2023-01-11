import time
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
def get_playlist(playlists,des):
    print(playlists)
    urls = []
    count = 0
    # iteratively get watch links from playlist
    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            try:
                start_time = time.time()
                urls.append(url)
                video = YouTube(url)
                #extract audio only
                audio = video.streams.filter(only_audio=True).first()

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

                end_time = time.time()
                #result
                eta = end_time - start_time
                print("[" + title + " downloaded {eta:" + time.strftime("%S", time.gmtime(eta))+"s} ]")
                count += 1
            except:
                print(title + " error! Skip!")

    print("Total download file: " + str(count))

# main code
# input playlist here for download
playlist = ["https://www.youtube.com/playlist?list=PLyPDCUrqti684QwRHgXka07WK2xKJUbbx"]

# input folder path for store file
save_path = "C:/Users/asus/Desktop/music"

pl_urls = get_playlist(playlist, save_path)