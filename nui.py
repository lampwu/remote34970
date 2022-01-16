from ast import If
import random
import time
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Feet to Meters")

def my_mainloop():
  print ('Hello World!')
  xg = random.randint(1, 100)
  feet.set(xg)
  meters.set(int(0.3048 * xg * 10000.0 + 0.5)/10000.0)
  #root.update
  #root.update_idletasks
  intValue = int((interalTime.get()))
  if stst == True:
    root.after(intValue*1000, my_mainloop)
  else:
    pass
    
    #root.after(10000000,my_mainloop)
  
stst = False

def stScan():
  global stst
  print(stst)
  stst = not stst
  if stst == True:
    print('yes')
    try:
      intValue = int(interalTime.get())
      starStop.set("Stop Scan")
      root.after(intValue*1000, my_mainloop)
    except ValueError:
      pass
  else:
    print('stop')
    starStop.set("Start Scan")
    pass

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Label(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

#ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

interalTime = StringVar()
ttk.Label(mainframe, text="interal").grid(column=1, row=3, sticky=W)
interalTimeEntry = ttk.Entry(mainframe, width=3, textvariable=interalTime)
interalTimeEntry.grid(column=2, row=3, sticky=W)

#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Second").grid(column=3, row=3, sticky=W)
starStop = StringVar()
starStop.set("Start Scan")
ttk.Button(mainframe, textvariable=starStop, command=stScan).grid(column=1, row=4, sticky=W)

  #root.after(int(interalTime.get())*1000, my_mainloop)


#root.after(1000, my_mainloop)    
interalTimeEntry.focus()
#root.bind("<Return>", stScan)



root.mainloop()

