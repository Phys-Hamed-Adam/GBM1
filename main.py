import numpy as np 
import matplotlib.pyplot as plt 
import qfin as qf
import yfinance as yf
import pandas as pd
from customtkinter import *

app=CTk()
app.geometry("700x600")

stock= CTkEntry(master=app, placeholder_text="Stock")
stock.place(relx= 0.1, rely =0.25)
drift_price= CTkEntry(master=app, placeholder_text="Drift price")
drift_price.place(relx=0.4, rely= 0.25)
volatility=CTkEntry(master=app,placeholder_text= "volatility" )
volatility.place(relx= 0.7, rely=0.25)
steps=CTkEntry(master=app, placeholder_text="Steps(n)")
steps.place(relx= 0.1,rely=0.5 )
time=CTkEntry(master=app, placeholder_text="Time")
time.place(relx=0.7, rely=0.5)


class Geometric_brownian_motion:
    
    @staticmethod
    
    def simulate(mu,current_price,vol, n, T):

        t= np.linspace(0.0, T, n+1)
        time_step = t[1] - t[0]
        z=np.random.standard_normal(size=n)
        z=np.insert(z,0,0) # Insert 0 at the start for correct path
        w=np.cumsum(np.sqrt(time_step)*z)
        
        path = current_price*np.exp( (mu-0.5*(vol**2))*t + (vol*w))

        return path, t

def generate_models():
    my_mu=float(drift_price.get())
    my_vol=float(volatility.get())
    my_n= int(steps.get())
    my_T= float(time.get())
    
    my_stock= stock.get()
    s = yf.download(my_stock, period="1y")["Close"]
    s= float(s.iloc[-1])
    
    t,path= Geometric_brownian_motion.simulate(mu=my_mu,current_price=s,vol=my_vol,n=my_n, T=my_T)

    plt.plot(t,path)
    plt.xlabel("Time(s)")
    plt.ylabel("Price paths")
    plt.title("Geometric Brownian Motion")
    plt.grid(True)
    return plt.show()

genreate_btn= CTkButton(master= app, text="Generate model", command=generate_models , corner_radius=32)
genreate_btn.place(relx= 0.4, rely=0.5)
app.mainloop()
