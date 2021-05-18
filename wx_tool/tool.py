import _tkinter
import time
import itchat
import threading


def thread_it(func, *args):
    """将函数打包进线程"""
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()


def wx_login(*args):
    """判断微信登陆状态,登陆微信"""
    wx_login_status_msg = args[0]
    wx_login_color = args[1]
    login_label = args[2]
    wx_friend = args[3]

    if wx_login_status_msg.get() == "未登录":
        itchat.auto_login()
        login = itchat.search_friends()
        if login.get('Signature') is not None:
            wx_login_status_msg.set("登陆成功")
            wx_login_color.set("green")
            login_label.configure(text=wx_login_status_msg.get(), fg=wx_login_color.get())

            # 获取全部好友

            friend_x = itchat.get_friends()
            log_time = time.strftime('%Y-%m-%d', time.localtime())
            for people in friend_x:
                if people['RemarkName'] != "":
                    try:
                        wx_friend.insert('end', people['RemarkName'])
                    except _tkinter.TclError:
                        with open('./{}_error_people.txt'.format(log_time), 'a', encoding='utf-8') as f:
                            f.write(people['RemarkName'] + "\n")
                else:
                    try:
                        wx_friend.insert('end', people['NickName'])
                    except _tkinter.TclError:
                        with open('./{}_error_people.txt'.format(log_time), 'a', encoding='utf-8') as f:
                            f.write(people['NickName'] + "\n")

            # 获取用户信息
            @itchat.msg_register(itchat.content.TEXT)
            def text_reply(msg):
                print(msg)

            itchat.run()
