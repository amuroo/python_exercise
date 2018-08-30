import sys
import requests
import random

from tkinter import *
from bs4 import BeautifulSoup
from lxml import html
import tkinter.messagebox as mb



def siritori(Event):
    res = EditBox.get(1.0, END)
    r_l = res[-1]
    print(r_l)
    r = requests.get('https://dictionary.goo.ne.jp/srch/jn/{}/m0u/'.format(r_l))
    tree = html.fromstring(r.content)
    #soup = BeautifulSoup(html,'lxml')
    r_word = tree.xpath('//dt[@class="title search-ttl-a"]/text()')
    rnd_word = random.choice(r_word)
    mb.showinfo(res, rnd_word)

ans = mb.askyesno("提案", "しりとりをしませんか？")
if ans == True:
    root = Tk()
    root.title('しりとり')
    
    #文字入力
    EditBox = Text(root)    
    EditBox.pack()

    #送信
    ok_button = Button(root, text = "OK")
    ok_button.bind("<1>",siritori)
    ok_button.pack()

else:
    mb.showinfo("悲しい", '私はとても悲しいです。')

root.mainloop()

# if __name__ == '__main__':
    

