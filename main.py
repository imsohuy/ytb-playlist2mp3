import time
import os

try:
    from pytube import Playlist, YouTube
    from art import *
except ModuleNotFoundError:
    os.system('pip install pytube')
    os.system('pip install art')


# create a function to download mp3 from playlist
def get_playlist(playlists, des):
    urls = []
    count = 0
    # iteratively get watch links from playlist

    for playlist in playlists:
        try:
            playlist_urls = Playlist(playlist)
            for url in playlist_urls:
                try:
                    start_time = time.time()
                    urls.append(url)
                    video = YouTube(url)
                    # extract audio only
                    audio = video.streams.filter(only_audio=True).first()

                    # create title
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
                    # result
                    eta = end_time - start_time
                    print("[" + title + " downloaded {eta:" + time.strftime("%S", time.gmtime(eta)) + "s} ]")
                    count += 1
                except:
                    print(title + " error! Skip!")
        except:
            print("Playlist", playlist, "cannot download!")
    print("Total download file: " + str(count))


# terminal menu
def menu():
    # input playlist here for download
    playlists = []

    # input folder path for store file
    save_path = "D:/download/audio/music"
    while True:
        print("Q - to quit input")
        print("P - to input playlist")
        print("L - to input save location")
        print("I - to print infomation")
        option = input("Enter option: ")
        if (option.lower() == 'q'): break
        if (option.lower() == 'i'):
            print("Current playlist to download", playlists)
            print("Save location", save_path)
            print("===========================\n")
        if (option.lower() == 'l'):
            save_path = input("Enter path for download: ")
            print("Save location", save_path)
            print("===========================\n")
        if (option.lower() == 'p'):
            input_pl = input("Enter playlist for download: ")
            playlists.append(input_pl)
            print("Current playlist to download", playlists)
            print("===========================\n")

    pl_urls = get_playlist(playlists, save_path)


# main code
tprint("ytbl2mp3bot")
print("Made in Vietnam, by Imsohuy\n")
print("======YtbPlayList2Mp3======")
menu()
