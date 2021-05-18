import _tkinter
import tkinter

import itchat
import threading
import time

# 生成主窗口对象
from tool import wx_login, thread_it

win = tkinter.Tk()
win.title("微咖管理助手")
# 设置窗口大小和位置
# 500x500 表示窗口大小
# +200+50 表示窗口距离电脑屏幕的左边缘和上边缘的距离
win.geometry("500x500+300+100")
win.resizable(0, 0)

wx_login_status_msg = tkinter.StringVar()
wx_login_status_msg.set("未登录")
wx_login_color = tkinter.StringVar()
wx_login_color.set("red")


# 菜单栏 ############

menubar = tkinter.Menu(win)
# 操作
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='操作', menu=file_menu)
file_menu.add_command(label='登录', command=lambda: thread_it(wx_login,wx_login_status_msg,wx_login_color,login_label,wx_friend))

# 日志
edit_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='日志', menu=edit_menu)
edit_menu.add_command(label='操作日志', command=lambda: thread_it(wx_login, ))
edit_menu.add_command(label='错误日志', command=lambda: thread_it(wx_login, ))


# 监控
monitoring_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='监控', menu=monitoring_menu)

monitoring_menu.add_command(label='群', command=lambda: thread_it(wx_login, ))
monitoring_menu.add_command(label='好友', command=lambda: thread_it(wx_login, ))

# 帮助
help_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='帮助', menu=help_menu)
help_menu.add_command(label='使用手册', command=lambda: thread_it(wx_login, ))
help_menu.add_command(label='联系作者', command=lambda: thread_it(wx_login, ))

#####################


tkinter.Label(win, text='微信登陆状态:').place(x=5, y=5)
login_label = tkinter.Label(win, text=wx_login_status_msg.get(), fg=wx_login_color.get())
login_label.place(x=85, y=5)

wx_friend = tkinter.Listbox(win, height=25)
wx_friend.place(x=340, y=30)

wx_friend_title = tkinter.Label(win,text="通讯录:").place(x=336,y=4)
search_friend = tkinter.Entry(win, show=None,width=11)
search_friend.place(x=400,y=3)
search_friend.insert(tkinter.END, "搜索")

news_hall = tkinter.Label(win, text='消息广场', bg='gray', font=('Arial', 12), width=35, height=1)
news_hall.place(x=10,y=40)

wx_group_msg = tkinter.Text(win, height=8,width=45)
wx_group_msg.place(x=10,y=90)


friend_msg = tkinter.Text(win, height=8,width=45)
friend_msg.place(x=10,y=225)

canvas = tkinter.Canvas(win, height=85, width=100,bg="green")
people_jc = tkinter.PhotoImage(file='people_jc.png')
canvas.create_image(48, 0, anchor='n',image=people_jc)
canvas.place(x=8,y=340)

file_ = tkinter.Canvas(win, height=85, width=100,bg="green")
file_gl = tkinter.PhotoImage(file='file_gl.png')
file_.create_image(55,0, anchor='n',image=file_gl)
file_.place(x=130,y=340)

win.config(menu=menubar)
win.mainloop()
