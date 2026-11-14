import time
import pyautogui

# Put the lines you want to send inside this list
lines = [
"The capacity to love is determined by the fact that man is ready to seek the good consciously with others, to subordinate himself to this good because of others, or to subordinate himself to others because of this good.",
]

# Gives you 5 seconds to click into the Discord message box
print("Switch to Discord and click the message box! Starting in 5 seconds...")
time.sleep(5)

for line in lines:
  pyautogui.write(line, interval=0.01)  # Types the line
  pyautogui.press("enter")  # Sends the message
  time.sleep(1)  # Waits 1 second before the next line

print("Done!")