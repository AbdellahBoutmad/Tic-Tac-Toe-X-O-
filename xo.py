from tkinter import *

win = Tk()

entries = []

i = 1

def ecrire(index):
    global i
    if entries[index].cget("text") == "":
        if i % 2 == 0:
            entries[index].config(text="X")
            i = i + 1
        else:
            entries[index].config(text="O")
            i = i + 1
    check()

def check():
    for i in range(len(entries)):
        if entries[i].cget("text") != "":
            if entries[0].cget("text") == entries[1].cget("text") == entries[2].cget("text")!= "":
                text="ROW 1 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[3].cget("text") == entries[4].cget("text") == entries[5].cget("text")!= "":
                text="ROW 2 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[6].cget("text") == entries[7].cget("text") == entries[8].cget("text")!= "":
                text="ROW 3 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[0].cget("text") == entries[3].cget("text") == entries[6].cget("text")!= "":
                text="COL 1 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[1].cget("text") == entries[4].cget("text") == entries[7].cget("text")!= "":
                text="COL 2 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[2].cget("text") == entries[5].cget("text") == entries[8].cget("text")!= "":
                text="COL 3 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[0].cget("text") == entries[4].cget("text") == entries[8].cget("text")!= "":
                text="DIAG 1 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return
            elif entries[2].cget("text") == entries[4].cget("text") == entries[6].cget("text")!= "":
                text="DIAG 2 WIN"
                result = Label(win, text=text, font=('Arial 18'))
                result.grid(row=3, columnspan=3)
                for j in range(len(entries)):
                    entries[j].config(state=DISABLED)
                return


for i in range(3):
    for j in range(3):
        name = Button(win, text="", width=5, bg="yellow", border=5, font=('Arial 24'), command=lambda i=i*3+j: [ecrire(i), update_time()])
        name.grid(row=i, column=j, padx=5, pady=5)
        entries.append(name)












            # Other win conditions omitted for brevity...

minutes = 0
seconds = 0

time_label =Label(win, text=f"Time: {minutes:02d}:{seconds:02d}", font=('Arial 18'))
time_label.grid(row=3, columnspan=3)

def update_time():
    global minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    time_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
    win.after(1000, update_time)












win.mainloop()














#def check(entries):
#    for i in range(4):
#        for j in range(i + 2, 9):
#            if entries[i].cget("text") == entries[j].cget("text"):
#                print("You lose!")
#                return
#   print("You win!")