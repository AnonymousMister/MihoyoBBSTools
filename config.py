import os
import json
import tools

#是否启用config
enable_Config = True
#这里的内容会自动获取
mihoyobbs_Login_ticket = ""
mihoyobbs_Stuid = ""
mihoyobbs_Stoken = ""
#这里是米游社的cookie
mihoyobbs_Cookies = ""
#这个dist里面的内容和米游社有关
mihoyobbs = {
    #全局开关，关闭之后下面的都不执行
    "bbs_Gobal": True,
    #讨论区签到
    "bbs_Singin": True,
    #多个讨论区签到
    "bbs_Singin_multi": True,
    #指定签到讨论区
    #1是崩坏3 2是原神 3是崩坏2 4是未定事件簿 5是大别墅
    #可以通过设置讨论区的id位置来设置主讨论区，[5,1]就是大别墅为主社区
    #看帖子 点赞 分享帖子都是使用主社区获取到的列表
    "bbs_Singin_multi_list": [2,5],
    #浏览3个帖子
    "bbs_Read_posts": True,
    #完成5次点赞
    "bbs_Like_posts": True,
    #完成后取消点赞
    "bbs_Unlike": True,
    #分享帖子
    "bbs_Share": True,
}
#原神自动签到
genshin_AutoSingin = True
#崩坏3自动签到
honkai3rd_AutoSing = True

path = os.path.dirname(os.path.realpath(__file__)) + "/config"
config_Path = f"{path}/config.json"

def Load_config():
    with open(config_Path, "r") as f:
        data = json.load(f)
        global enable_Config
        global mihoyobbs_Login_ticket
        global mihoyobbs_Stuid
        global mihoyobbs_Stoken
        global mihoyobbs_Cookies
        global mihoyobbs
        global genshin_AutoSingin
        global honkai3rd_AutoSing
        enable_Config = data["enable_Config"]
        mihoyobbs_Login_ticket = data["mihoyobbs_Login_ticket"]
        mihoyobbs_Stuid = data["mihoyobbs_Stuid"]
        mihoyobbs_Stoken = data["mihoyobbs_Stoken"]
        mihoyobbs_Cookies = data["mihoyobbs_Cookies"]
        mihoyobbs["bbs_Gobal"] = data["mihoyobbs"]["bbs_Gobal"]
        mihoyobbs["bbs_Singin"] = data["mihoyobbs"]["bbs_Singin"]
        mihoyobbs["bbs_Singin_multi"] = data["mihoyobbs"]["bbs_Singin_multi"]
        mihoyobbs["bbs_Singin_multi_list"] = data["mihoyobbs"]["bbs_Singin_multi_list"]
        mihoyobbs["bbs_Read_posts"] = data["mihoyobbs"]["bbs_Read_posts"]
        mihoyobbs["bbs_Like_posts"] = data["mihoyobbs"]["bbs_Like_posts"]
        mihoyobbs["bbs_Unlike"] = data["mihoyobbs"]["bbs_Unlike"]
        mihoyobbs["bbs_Share"] = data["mihoyobbs"]["bbs_Share"]
        genshin_AutoSingin = data["genshin_AutoSingin"]
        honkai3rd_AutoSing = data["honkai3rd_AutoSing"]
        f.close()
        tools.log.info("Config加载完毕")

def Save_config():
    with open(config_Path,"r+") as f:
        data = json.load(f)
        data["mihoyobbs_Login_ticket"] = mihoyobbs_Login_ticket
        data["mihoyobbs_Stuid"] = mihoyobbs_Stuid
        data["mihoyobbs_Stoken"] = mihoyobbs_Stoken
        f.seek(0)
        f.truncate()
        temp_Text = json.dumps(data, sort_keys=False, indent=4, separators=(', ', ': '))
        f.write(temp_Text)
        f.flush()
        f.close()
        tools.log.info("Config保存完毕")

def Clear_cookies():
    with open(config_Path,"r+") as f:
        data = json.load(f)
        data["enable_Config"] = False
        data["mihoyobbs_Login_ticket"] = ""
        data["mihoyobbs_Stuid"] = ""
        data["mihoyobbs_Stoken"] = ""
        data["mihoyobbs_Cookies"] = ""
        f.seek(0)
        f.truncate()
        temp_Text = json.dumps(data, sort_keys=False, indent=4, separators=(', ', ': '))
        f.write(temp_Text)
        f.flush()
        f.close()
        tools.log.info("Cookie删除完毕")