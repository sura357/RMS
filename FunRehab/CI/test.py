import win32api

file = 'C:\\Users\\user\\Desktop\\講義-TA系統.pdf'
win32api.ShellExecute(0, 'open', file, '', '', 1)
