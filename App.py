import sys
import tkinter as tk

from Frame import Frame

if __name__ == '__main__':
    
    main_win = tk.Tk()
    main_win.title('画像 Resize')
    main_win.geometry('350x190')
    
    frame = Frame.Frame(main_win)

    main_win.mainloop()