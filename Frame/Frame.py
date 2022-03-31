import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *

import os, sys

class Frame:

    def make_dialog(self, is_input):
        iDir = os.path.abspath(os.path.dirname(__file__))
        iDirPath = filedialog.askdirectory(initialdir = iDir)
        
        if is_input:
            self.input_pass_entry_var.set(iDirPath)
        else :
            self.output_pass_entry_var.set(iDirPath)

    def make_frame2(self):

        self.frame2 = ttk.Frame(self.main_win, padding=10)

        
        

    def __init__(self, main_win):

        self.main_win = main_win
        self.frame1 = ttk.Frame(self.main_win, padding=10)

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
        self.check_bln.set(True)

        self.checkbox = tk.Checkbutton(self.frame1,variable=self.check_bln, text='アスペクト比の維持')

        
        # 実行ボタン
        self.execute_button = tk.Button(self.frame1, text='実行', command=self.make_frame2, font=("MSゴシック","11", "bold"),height=2, width=10, relief=SOLID)


        # frameの配置
        self.frame1.grid(row=0, column=0)

        # widgetの配置
        self.input_pass_label.grid(row=0, column=0)
        self.input_pass_entry.grid(row=0, column=1)
        self.input_pass_button.grid(row=0, column=2)

        self.output_pass_label.grid(row=1, column=0)
        self.output_pass_entry.grid(row=1, column=1)
        self.output_pass_button.grid(row=1, column=2)

        self.checkbox.grid(row=2, column=1)

        self.execute_button.grid(row=3, column=1, pady=15)

