#!/usr/bin/env python
# coding: utf-8

# In[217]:


import tkinter as tk 
from tkinter import ttk
import tkinter.font as font


# In[218]:


root=tk.Tk()
root.geometry("280x180")
root.title("DISTANCE CALCULATOR")


myfont = font.Font(family='Merlin')


# In[219]:


meterget=tk.StringVar()
feetset=tk.StringVar(value="Converted feet will be shown here!")

def calculate(*args):
    meters=float(meterget.get())
    feets= meters * 3.28084
    feetset.set(feets)


# In[220]:


frame=ttk.Frame(root,padding=(10,20))
frame.grid()


root.columnconfigure(0,weight=1)

meter=ttk.Label(frame,text="METERS : ")
meterinput=ttk.Entry(frame,width=10,textvariable=meterget)
feet=ttk.Label(frame,text="FEET : ")
feetlabel=ttk.Label(frame,textvariable=feetset)
calculate=ttk.Button(frame,text="Calculate",command=calculate)

meter.grid(row=0,column=0,padx=5,pady=5)
meterinput.grid(row=0,column=1,padx=5,pady=5)
meterinput.focus()
feet.grid(row=1,column=0,padx=5,pady=5)
feetlabel.grid(row=1,column=1,padx=5,pady=5)
calculate.grid(row=2,column=0,columnspan=2,padx=5,pady=5)


# In[ ]:


root.mainloop()


# In[ ]:




