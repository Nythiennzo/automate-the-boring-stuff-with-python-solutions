import pyautogui, pyperclip

notepad_windows = pyautogui.getWindowsWithTitle('Notepad')

if len(notepad_windows) > 0:
    notepad_window = notepad_windows[0] 
    
notepad_window.activate()

pyautogui.click(notepad_window.top + 200, notepad_window.left + 200)

pyautogui.hotkey('ctrl', 'a')

pyautogui.hotkey('ctrl', 'c')

print(pyperclip.paste())