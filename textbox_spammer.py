import time
import pyautogui

# Put the lines you want to send inside this list
lines = [
"Line 1",
"Line 2",
"Line 3",
  #..... put as much line you want and it'll spam on any chatbox.
]

# Gives you 5 seconds to click into the Discord message box
print("Switch to Discord and click the message box! Starting in 5 seconds...")
time.sleep(5)

for line in lines:
  pyautogui.write(line, interval=0.01)  # Types the line
  pyautogui.press("enter")  # Sends the message
  time.sleep(1)  # Waits 1 second before the next line

print("Done!")
