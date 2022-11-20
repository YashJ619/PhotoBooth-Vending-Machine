# importing vlc module
import vlc
# creating vlc media player object
media = vlc.MediaPlayer("d.mp4")
#os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
# start playing video
media.play()
