from pytube import YouTube
import customtkinter

# the basic color theme of the app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def Download_Initiation(option):
    try:
        yt_link = YouTube(link_dialogue_box.get(), on_progress_callback = Download_Progress)


        if option == "Video":
            video = yt_link.streams.filter(file_extension= 'mp4').get_by_resolution('720p')
            video.download()
        elif option == "Audio":
            audio = yt_link.streams.get_audio_only()
            audio.download()
        else:
            return "Problem encountered!"
                
    except:
        '''final_label.configure(text="Download Error!")'''

def Download_Progress():
    pass


root = customtkinter.CTk()

root.title("YT Downloader")
root.geometry('1080*480')

link_dialogue_box = customtkinter.CTkEntry(root)

video_button = customtkinter.CTkButton(root, text= 'Video', command=lambda: Download_Initiation('Video'))
audio_button = customtkinter.CTkButton(root, text= 'Audio', command=lambda: Download_Initiation('Audio'))

link_dialogue_box.pack()
video_button.pack()
audio_button.pack()

root.mainloop()