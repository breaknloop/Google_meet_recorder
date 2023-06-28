#its an undergoing project we are open to suggestions for improvement
#further it will be improved for taking notes and also creating transcripts

import tkinter
import pyautogui
from tkinter import ttk
from tkinter import messagebox
import time


def record_meeting(meeting_id, output_file):
    # Open Google Meet

    pyautogui.hotkey('Alt','Tab')
    time.sleep(1)
    pyautogui.click(x=1200, y=50)

    # Join the meeting
    pyautogui.typewrite(meeting_id)

    # Start recording the meeting
    pyautogui.hotkey(button1)

    # Wait for the meeting to end
    time.sleep(60*60)

    # Stop recording the meeting
    pyautogui.hotkey(button2)

    # Save the recording
    pyautogui.typewrite(output_file)

def dat_sync():
    meeting_id_1 = first_meetId_entry
    meeting_id_2 = second_meetId_entry

    # Get the output file names
    output_file_1 = first_file_entry
    output_file_2 = second_file_entry

    # Record the meetings
    record_meeting(meeting_id_1, output_file_1)
    record_meeting(meeting_id_2, output_file_2)

window = tkinter.Tk()
window.title("Google meet recorder")

frame = tkinter.Frame(window)
frame.pack(padx=240, pady=200)

# taking google meet id for meetings
meet_info_frame = tkinter.LabelFrame(frame, text="Google meet Links", padx=20, pady=20)
meet_info_frame.grid(row=0, column=0)
first_meetId_label = tkinter.Label(meet_info_frame, text="First ID/Link", padx=5, pady=20)
first_meetId_label.grid(row=0, column=0)
second_meetId_label = tkinter.Label(meet_info_frame, text="Second ID/Link", padx=5, pady=20)
second_meetId_label.grid(row=1, column=0)

first_meetId_entry = tkinter.Entry(meet_info_frame, width=50)
second_meetId_entry = tkinter.Entry(meet_info_frame, width=50)
first_meetId_entry.grid(row=0, column=1)
second_meetId_entry.grid(row=1, column=1)

# Get the output file names
output_info_frame = tkinter.LabelFrame(frame, text="File names", padx=20, pady=20)
output_info_frame.grid(row=2, column=0)
first_file_label = tkinter.Label(output_info_frame, text="First file name", pady=20)
first_file_label.grid(row=2, column=0)
second_file_label = tkinter.Label(output_info_frame, text="Second file name", pady=20)
second_file_label.grid(row=3, column=0)

first_file_entry = tkinter.Entry(output_info_frame, width=50)
second_file_entry = tkinter.Entry(output_info_frame, width=50)
first_file_entry.grid(row=2, column=1)
second_file_entry.grid(row=3, column=1)

button1 = tkinter.Button(frame, text="Start Recording", command=dat_sync)
button1.grid(row=3, column=0, sticky="news", padx=20, pady=20)

button2 = tkinter.Button(frame, text="Stop Recording", command=dat_sync)
button2.grid(row=4, column=0, sticky="news", padx=20, pady=20)






window.mainloop()
