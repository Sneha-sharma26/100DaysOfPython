## Write a py program which reminds you of drinking water every hour of two.
## Your program can either beep or send dekstop notifications for a specific operating system.

#----------Code--------#

# # 1. plyer module: allows developers to write code that can interact with device-specific functionalities.
# from plyer import notification
# import time

# if __name__ == "__main__" :
#     while True:
#         notification.notify(title="Water Break Sneha!!", app_name="Water Reminder", message="Stay hydrated for glowing skin", timeout=5)
#         time.sleep(3600)   # delays the next execution to 1hr = 3600sec


# # 2. Using plyer & tkinter module
# from plyer import notification
# import tkinter as tk
# root = tk.Tk()
# tk.Label(root , text = 'NOTIFICATION DEVELOPER').grid(row = 0, column = 0)
# tk.Label(root , text = 'Notification Title:').grid(row = 3, column = 0)
# tk.Label(root , text = 'Notification Message').grid(row = 4, column = 0)
# tk.Label(root , text = 'Seconds for which it appears'). grid(row = 5, column = 0)

# t1 = tk.Entry(root)
# t1.grid(row = 3, column = 1)
# m = tk.Entry(root)
# m.grid(row = 4, column = 1)
# tm = tk.Entry(root)
# tm.grid(row = 5, column = 1)

# def strt():
#     a = int(tm.get())
#     notification.notify(
#     title = t1.get(),
#     message = m.get(),
#     timeout = a
#     )
# tk.Button(root , text = 'START NOTIFICATION' , command = strt).grid(row = 6, column = 0)
# root.mainloop()

# 3. win10toast module
# from win10toast import ToastNotifier
# toast = ToastNotifier()
# toast.show_toast(
#     "Drink Water",
#     "Stay hydrated Sneha!",
#     duration = 7,
#     threaded = True,
# )