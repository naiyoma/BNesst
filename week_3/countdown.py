import tkinter as tk
from datetime import datetime, timedelta

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")

        # set up labels and entry boxes for user input
        self.day_label = tk.Label(master, text="Day:")
        self.day_label.grid(row=0, column=0)
        self.day_entry = tk.Entry(master)
        self.day_entry.grid(row=0, column=1)

        self.month_label = tk.Label(master, text="Month:")
        self.month_label.grid(row=1, column=0)
        self.month_entry = tk.Entry(master)
        self.month_entry.grid(row=1, column=1)

        self.year_label = tk.Label(master, text="Year:")
        self.year_label.grid(row=2, column=0)
        self.year_entry = tk.Entry(master)
        self.year_entry.grid(row=2, column=1)

        self.hour_label = tk.Label(master, text="Hour:")
        self.hour_label.grid(row=3, column=0)
        self.hour_entry = tk.Entry(master)
        self.hour_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(master, text="Start Countdown", command=self.start_countdown)
        self.submit_button.grid(row=4, column=0, columnspan=2)

        # set up the countdown timer label
        self.timer_label = tk.Label(master, font=("Arial", 20, "bold"), text="00:00:00")
        self.timer_label.grid(row=5, column=0, columnspan=2)

    def start_countdown(self):
        # get user input and create datetime object
        day = int(self.day_entry.get())
        month = int(self.month_entry.get())
        year = int(self.year_entry.get())
        hour = int(self.hour_entry.get())
        countdown_datetime = datetime(year, month, day, hour)

        # check if entered time has already passed
        if datetime.now() > countdown_datetime:
            self.timer_label.configure(text="Please enter a valid future date and time.")
            return

        # update the countdown timer label every second
        def update_timer():
            time_remaining = countdown_datetime - datetime.now()
            if time_remaining <= timedelta():
                self.timer_label.configure(text="Countdown Finished!")
                return
            time_string = str(time_remaining).split(".")[0]
            self.timer_label.configure(text=time_string)
            self.timer_label.after(1000, update_timer)

        update_timer()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="yellow")
    countdown = CountdownTimer(root)
    root.mainloop()
