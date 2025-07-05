
#ॐ
from tkinter import *
import os
from tkinter import StringVar, Listbox, Tk, Label, Button, Scrollbar, END, BOTH, VERTICAL, X
from tkinter import filedialog
import pygame.mixer as mixer
import os

def create_music_player_gui():
    mixer.init()

    def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
        song_name.set(songs_list.get(ACTIVE))
        mixer.music.load(songs_list.get(ACTIVE))
        mixer.music.play()
        status.set("Song PLAYING")

    def stop_song(status: StringVar):
        mixer.music.stop()
        status.set("Song STOPPED")

    def load(listbox):
        os.chdir(filedialog.askdirectory(title='Open a songs directory'))
        tracks = os.listdir()
        for track in tracks:
            listbox.insert(END, track)

    def pause_song(status: StringVar):
        mixer.music.pause()
        status.set("Song PAUSED")

    def resume_song(status: StringVar):
        mixer.music.unpause()
        status.set("Song RESUMED")

    root = Tk()
    root.geometry('700x220')
    root.title('CVR Music Player')
    root.resizable(0, 0)

    song_frame = LabelFrame(root, text='Current Song', bg='DarkBlue',fg='white', width=400, height=80)
    song_frame.place(x=0, y=0)

    button_frame = LabelFrame(root, text='Control Buttons',fg='white', bg='Maroon', width=400, height=120)
    button_frame.place(y=80)

    listbox_frame = LabelFrame(root, text='Playlist', bg='Lightgrey')
    listbox_frame.place(x=400, y=0, height=200, width=300)

    current_song = StringVar(root, value='<Not selected>')
    song_status = StringVar(root, value='<Not Available>')

    playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Lightgrey')
    scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
    scroll_bar.pack(side=RIGHT, fill=BOTH)
    playlist.config(yscrollcommand=scroll_bar.set)
    scroll_bar.config(command=playlist.yview)
    playlist.pack(fill=BOTH, padx=5, pady=5)

    Label(song_frame, text='CURRENTLY PLAYING:', bg='Lightgrey', font=('Times', 10, 'bold')).place(x=5, y=20)
    song_lbl = Label(song_frame, textvariable=current_song, bg='LightGrey', font=("Times", 12), width=25)
    song_lbl.place(x=150, y=20)

    pause_btn = Button(button_frame, text='Pause', bg='Lightgrey', font=("Georgia", 13), width=7, command=lambda: pause_song(song_status))
    pause_btn.place(x=15, y=10)

    stop_btn = Button(button_frame, text='Stop', bg='Lightgrey', font=("Georgia", 13), width=7, command=lambda: stop_song(song_status))
    stop_btn.place(x=105, y=10)

    play_btn = Button(button_frame, text='Play', bg='Lightgrey', font=("Georgia", 13), width=7, command=lambda: play_song(current_song, playlist, song_status))
    play_btn.place(x=195, y=10)

    resume_btn = Button(button_frame, text='Resume', bg='Lightgrey', font=("Georgia", 13), width=7, command=lambda: resume_song(song_status))
    resume_btn.place(x=285, y=10)

    load_btn = Button(button_frame, text='Load Directory', bg='Lightgrey', font=("Georgia", 13), width=35, command=lambda: load(playlist))
    load_btn.place(x=10, y=55)

    Label(root, textvariable=song_status, bg='Lightgrey', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

    root.mainloop()

#----------------
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="PLEASE ENTER DETAILS BELOW").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="USERNAME")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="PASSWORD *")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Sign up", width=10, height=1,command = register_user).pack()
 
 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="PLEASE ENTER DETAILS BELOW TO LOGIN").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="USERNAME").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="PASSWORD *").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found() 
def login_sucess():
    global login_success_screen
    create_music_player_gui()
 
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
  
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
  
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
  
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="navyblue",fg="white", width="300", height="2", font=("Calibri", 20)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
