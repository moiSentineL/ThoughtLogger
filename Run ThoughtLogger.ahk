; Running ThoughtLogger with a Hotkey.
; moiSentineL
; Paste this script on C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup (shell:startup on Run Menu)
; to run this script on startup.
; AutoHotkey required.

^!t::Run C:\Users\%A_UserName%\AppData\Roaming\ThoughtLogger\thoughtlogger.exe, C:\Users\%A_UserName%\AppData\Roaming\ThoughtLogger
