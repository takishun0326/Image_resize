import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
from PIL import ImageGrab, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True


import os, sys

class Frame:

    # フォルダのパス選択
    def make_dialog(self, is_input):
        iDir = os.path.abspath(os.path.dirname(__file__))
        iDirPath = filedialog.askdirectory(initialdir = iDir)
        
        if is_input:
            self.input_pass_entry_var.set(iDirPath)
        else :
            self.output_pass_entry_var.set(iDirPath)
    
    # 終了
    def pushed_exit(self):
        self.main_win.destroy()

    # 続行
    def destroy_frame2(self):
        self.frame2.destroy()



    # Frame2
    def make_frame2(self):
        self.frame2 = ttk.Frame(self.main_win, padding=10)

        # プログレスバー
        self.progress = ttk.Progressbar(self.frame2, orient='horizontal', length=200, mode='determinate')
        self.set_progress_maximum()
        
        self.current_count = StringVar()
        self.current_count.set("0")
        self.current_count_label = tk.Label(self.frame2, textvariable=self.current_count)

        self.slash_label = tk.Label(self.frame2, text=' / ')

        self.maximum_count = StringVar()
        self.maximum_count.set(str(self.max_value))
        self.maximum_count_label = tk.Label(self.frame2, textvariable=self.maximum_count)

        # continue
        self.continue_button = tk.Button(self.frame2, text='続行', command=self.destroy_frame2)
        
        # exit
        self.exit_button = tk.Button(self.frame2, text='終了', command=self.pushed_exit)


        # frame
        self.frame2.grid(row=0, column=0, sticky=NSEW)

        # widget
        self.progress.grid(row=0, column=0)
        self.current_count_label.grid(row=1, column=1)
        self.slash_label.grid(row=1, column=2)
        self.maximum_count_label.grid(row=1, column=3)

        self.continue_button.grid(row=2, column=1)
        self.exit_button.grid(row=2, column=3)



        # frame2を最前面にする
        self.frame2.tkraise()
        
        self.resize_images()



            # プログレスバーの最大値の設定
    def set_progress_maximum(self):
        self.max_value = sum(os.path.isfile(os.path.join(self.input_pass_entry_var.get(), name)) for name in os.listdir(self.input_pass_entry_var.get()))
        self.progress.configure(maximum=self.max_value, value=0)

    # プログレスバーの経過の更新
    def update_progress(self, current_value):
        self.current_value = current_value
        self.current_count.set(str(self.current_value))
        self.progress.configure(value=self.current_value)


    def resize_images(self):
        files = os.listdir(self.input_pass_entry_var.get())
        count = 0

        for file in files:
            photo = Image.open(os.path.join(self.input_pass_entry_var.get(),file))
            photo_resize = photo.resize((256,256))
            photo_resize.save(os.path.join(self.output_pass_entry_var.get(), file))
            count += 1
            self.update_progress(count)


    def __init__(self, main_win):

        self.main_win = main_win
        self.frame1 = ttk.Frame(self.main_win, padding=10)

        self.main_win.grid_rowconfigure(0, weight=1)
        self.main_win.grid_columnconfigure(0,weight=1)

        # 画像のパス
        self.input_pass_label = ttk.Label(self.frame1, text='画像のパス')
        
        # 「画像のパス」エントリーの作成
        self.input_pass_entry_var = StringVar()
        self.input_pass_entry =  ttk.Entry(self.frame1, textvariable=self.input_pass_entry_var, width=30)
        
        # 「フォルダ参照」ボタンの作成
        self.input_pass_button = ttk.Button(self.frame1, text='参照', command=lambda: self.make_dialog(True))

        # 保存先のパス
        self.output_pass_label = ttk.Label(self.frame1, text='保存先')

        # 「保存先のパス」エントリーの作成
        self.output_pass_entry_var = StringVar()
        self.output_pass_entry = ttk.Entry(self.frame1, textvariable=self.output_pass_entry_var, width=30)

        # 「フォルダ参照」ボタンの作成
        self.output_pass_button = ttk.Button(self.frame1, text='参照', command=lambda: self.make_dialog(False))


        # チェックボックス
        self.check_bln = tk.BooleanVar()
        self.check_bln.set(False)

        self.checkbox = tk.Checkbutton(self.frame1,variable=self.check_bln, text='アスペクト比の維持')

        
        # 実行ボタン
        self.execute_button = tk.Button(self.frame1, text='実行', command=self.make_frame2, font=("MSゴシック","11", "bold"),height=2, width=10, relief=SOLID)


        # frameの配置
        self.frame1.grid(row=0, column=0, sticky=NSEW)

        # widgetの配置
        self.input_pass_label.grid(row=0, column=0)
        self.input_pass_entry.grid(row=0, column=1)
        self.input_pass_button.grid(row=0, column=2)

        self.output_pass_label.grid(row=1, column=0)
        self.output_pass_entry.grid(row=1, column=1)
        self.output_pass_button.grid(row=1, column=2)

        self.checkbox.grid(row=2, column=1)

        self.execute_button.grid(row=3, column=1, pady=15)

