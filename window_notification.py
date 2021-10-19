
import os

from win10toast import ToastNotifier

def notification():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    toast = ToastNotifier()
    title = "Notification"
    message = "Dhiraj loves Python"

    icon= 'Pythonlogo.jpg'
    length=30
    toast.show_toast(title,message,icon_path=icon,duration=length)


notification()
