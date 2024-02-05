from pytube import YouTube
import customtkinter

# the basic color theme of the app
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# function defining download procedures
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


# function for Download Progress Bar
def Download_Progress():
    pass

# GUI for the app
root = customtkinter.CTk()

root.title("YT Downloader 1.0.1")
root.minsize(550,220)
root.maxsize(550,220)

yt_label = customtkinter.CTkLabel(root, text= "YouTube U/A Downloader", font= ("Comic Sans", 20))

link_dialogue_box = customtkinter.CTkEntry(root, width= 500, placeholder_text="Enter URL")

video_button = customtkinter.CTkButton(root, text= 'Video', command=lambda: Download_Initiation('Video'))
audio_button = customtkinter.CTkButton(root, text= 'Audio', command=lambda: Download_Initiation('Audio'))

yt_label.grid(row= 0, column= 0, columnspan=3, pady= 20)
link_dialogue_box.grid(row= 1, column= 0, columnspan= 3,padx=30, pady=20)
video_button.grid(row= 2, column = 0, padx= 10, pady= 20)
audio_button.grid(row= 2, column = 2, padx= 10, pady= 20)

root.mainloop()