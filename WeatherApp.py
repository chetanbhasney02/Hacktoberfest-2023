from tkinter import *
import requests

root=Tk() 

def get(city):
    api="79de5817a4d223b536ce61a0f630a4b4"
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'appid':api, 'q':city, 'units':'Metric'}
    response=requests.get(url,params=params)
    report=response.json()

    label['text']=show(report)


def show(report):
    try:
        city= report['name']
        weather_condition= report['weather'][0]['description']
        temp= report['main']['temp']
        output= 'City: %s \nCondition: %s \nTemperature(°C): %s' %(city,weather_condition,temp)
    except:
        output='Problem in show weather function'
    return output


canvas=Canvas(root,width=666,height=666)
canvas.pack()


frame=Frame(root,bd=1,bg='black')
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.7,anchor='n')

entry=Entry(frame,font=('Helvetica',20),fg='white',bg='black')
entry.place(relheight=1,relwidth=0.7)

btn=Button(frame,text="Get Weather",bg="cyan",font=20,command=lambda: get(entry.get()))
btn.place(relx=0.7,relheight=1,relwidth=0.3)

low_frame=Frame(root,bd=1)
low_frame.place(relx=0.5,rely=0.3,relheight=0.6,relwidth=.75,anchor='n')


label=Label(low_frame,font=('Helvectica',20),justify='center',bd=4,)
label.config(font=40,bg='white')
label.place(relheight=1,relwidth=1)


root.mainloop()