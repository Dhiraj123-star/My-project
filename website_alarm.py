import time
import webbrowser

set_alarm = input("Enter time when you want to open website as H:M:S ")

url = input("Enter the website you want to open: ")

actual_time = time.strftime("%I:%M:%S")

while(actual_time!=set_alarm):
    print("The time is: "+actual_time)
    actual_time=time.strftime("%I:%M:%S")
    time.sleep(1)

if (actual_time==set_alarm):
    print("You should see your webpage now :-)")
    webbrowser.open(url)
