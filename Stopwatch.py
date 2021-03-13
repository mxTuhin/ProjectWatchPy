# Python program to illustrate a stop watch 
# using Tkinter 
# importing the required libraries
import tkinter as Tkinter
from datetime import datetime
from tkinter import *
import json

counter = 64800
running = False
timer=0


def counter_label(timerText, label):
    def count():
        if running:
            global counter
            label['text'] = "Counting.."

            # To manage the intial delay.
            if counter == 64800:
                label['text'] = "Counting.."  # Or label.config(text=display)
                display="00:00:00"
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            timerText['text'] = display  # Or label.config(text=display)
            global timer
            timer+=1

            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count)
            counter += 1

    # Triggering the start of the counter.
    count()


# start function of the stopwatch
def Start(timerText, label):
    global running
    running = True
    counter_label(timerText, label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# Stop function of the stopwatch
def Stop(label):
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    label['text'] = 'Start !'
    running = False


# Reset function of the stopwatch
def Reset(label):
    global counter
    counter = 64800

    # If rest is pressed after pressing stop.
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Start !'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text'] = 'Starting...'

def submit():
    Stop(label)
    dictValue={}
    dictValue = {
        "Working_Module": [],
        "Time": []
    }
    x={}
    dictValue["Working_Module"].append(workedOn.get())
    dictValue["Time"].append(timer-1)
    with open('data.json') as f:
        x = json.loads(f.read())
        x["Working_Module"].append(workedOn.get())
        x["Time"].append(timer - 1)
        # x=json.loads(f.read())
        # print(x["Working_Module"])
    with open('data.json', 'w') as f:
        f.write(json.dumps(x, ensure_ascii=False))
    workedOn.delete(0, END)
    workedOn.insert(0, "Default: UI Modification")

root = Tkinter.Tk()
root.configure(bg='black')
root.title("StopWatch")

# Fixing the window size. 
root.minsize(width=350, height=250)
label = Tkinter.Label(root, bg="black", text="Start !", fg="white", font="Verdana 16 bold")
label.pack()
timerText = Tkinter.Label(root, bg="black", text="00:00:00", fg="white", font="Verdana 40 bold")
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', bg="black", fg="white", width=6, command=lambda: Start(timerText, label))
stop = Tkinter.Button(f, text='Stop', bg="black", fg="white", width=6, state='disabled', command=lambda:Stop(label))
reset = Tkinter.Button(f, text='Reset', bg="black", fg="white", width=6, state='disabled', command=lambda: Reset(label))

f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
timerText.pack()
workedOn=Entry(root, bg="black", fg="white", font="Verdana 12 bold")
workedOn.insert(0, 'Default: UI Modification')
workedOn.pack()
submitButton = Tkinter.Button(text='Submit', bg="black", fg="white", width=10, height=2, command=submit)
submitButton.pack(pady=10)
def on_click(event):
    workedOn.configure(state=NORMAL)
    workedOn.delete(0, END)

    # make the callback only work once
    workedOn.unbind('<Button-1>', on_click_id)

on_click_id = workedOn.bind('<Button-1>', on_click)

root.mainloop()

