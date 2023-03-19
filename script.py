from tkinter import *
import time 
import threading 
from tkinter import messagebox

class Window():
    def __init__(self, title, width, height):
        ###################################################
        ####### setting initial variables #################
        ###################################################
        self.pause = False 
        ###################################################

        self.root = Tk() 
        self.root.geometry(f"{height}x{width}")
        self.root.title = "Timer rittwick" 
        self.title = title
        self.height = height 
        self.width = width 

        self.timer_frame = Frame(self.root, borderwidth=1, bg="grey", relief=SUNKEN)
        self.timer_frame.pack(side=TOP, anchor="nw")
        self.hour_input = Frame(self.timer_frame, borderwidth=1, bg="pink", relief=SUNKEN)
        self.hour_input.pack(side=LEFT)
        self.hour_value = IntVar() 
        self.hour_entry = Entry(self.hour_input, textvariable=self.hour_value)
        self.hour_entry.pack()


        self.display_frame = Frame(self.root, borderwidth=1, relief=SUNKEN)
        self.display_label = Label(self.display_frame, text="Time remaining")
        self.output_text = StringVar() 
        self.output_label = Label(self.display_frame, textvariable=self.output_text)
        self.display_label.pack() 
        self.output_label.pack()

        self.minute_value = IntVar()
        self.minute_input = Frame(self.timer_frame, borderwidth=1, relief=SUNKEN)
        self.minute_input.pack(side=RIGHT)
        self.minute_entry = Entry(self.minute_input, textvariable=self.minute_value)
        self.minute_entry.pack()

        self.btn_frame = Frame(self.root, borderwidth=1, relief=SUNKEN)
        self.start_btn = Button(self.btn_frame, text="Start now", command=self.start_countdown)
        self.start_btn.pack(side=LEFT, padx=23)

        self.quit_btn = Button(self.btn_frame, text="Close", command=self.close_timer)
        self.quit_btn.pack()
        
        self.pause_btn = Button(self.btn_frame, text="Pause now", command=self.pause_countdown)
        self.resume_btn = Button(self.btn_frame, text="Resume now", command=self.resume_countdown)
        self.btn_frame.pack(side=BOTTOM)
            
        self.root.attributes('-topmost',True)
        self.root.overrideredirect(True)
        self.root.bind('<B1-Motion>',self.move)
        self.root.mainloop() 

    def start_countdown(self):
        try:
            self.time_remaining = self.hour_value.get()*3600 + self.minute_value.get()*60
            # self.time_remaining = 5
            self.pause = False 
            thread = threading.Thread(target=self.countdown)
            thread.start() 
            self.timer_frame.forget()
            self.start_btn.forget() 
            self.display_frame.pack(side=TOP)
            self.pause_btn.pack(padx=23)
        except:
            messagebox.showerror("Enter time properly", "Enter time properly")


    def pause_countdown(self):
        self.resume_btn.pack(side=LEFT)
        self.pause_btn.forget()
        self.pause = True 

    def resume_countdown(self):
        self.pause = False 
        self.resume_btn.forget()
        self.pause_btn.pack(padx=23)
        thread = threading.Thread(target=self.countdown)
        thread.start() 

    def time_over(self):
        self.pause = False 
        self.display_frame.forget()
        self.timer_frame.pack(side=TOP, anchor="nw")
        self.start_btn.pack()
        self.pause_btn.forget()
        self.resume_btn.forget() 

    def move(self, event):
        x, y = self.root.winfo_pointerxy()
        self.root.geometry("+"+str(int(x))+"+"+str(int(y)))

    def countdown(self):
        # print(f"Time left: {self.time_remaining}")
        time.sleep(1)
        self.time_remaining = self.time_remaining - 1 
        if self.time_remaining>=0 and not self.pause:
            self.output_text.set(self.convert(self.time_remaining))
            self.countdown()
        elif not self.pause:
            self.time_over()
        
    def close_timer(self):
        self.pause = True 
        self.pause_countdown() 
        quit()
    def convert(self, seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
     
        return "%d:%02d:%02d" % (hour, minutes, seconds)

if __name__=='__main__':
    win = Window("Timer", 100, 200)