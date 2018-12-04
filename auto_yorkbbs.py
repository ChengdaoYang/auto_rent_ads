#租房自动广告机
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time
import random
import tkinter as tk


#your york_bbs account and password
your_account = ''.strip()
your_password = ''.strip()


#创建 GUI 窗口界面
window = tk.Tk()
window.title('租房自动广告机')
window.geometry('400x400')


show_text = tk.StringVar()# 这时文字变量储存器




####function section####

#自动顶帖
def up_rend_yorkbbs():
    #set chrome driver to headerless
    # option_ = Options()
    # option_.add_argument('--headless')

    #create driver to scrape
    # driver = webdriver.Chrome(chrome_options=option_)
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.01)

    #进入登陆 账号的 url
    url = 'http://forum.yorkbbs.ca/login.aspx'
    driver.get(url)
    time.sleep(2)

    #输入账号密码登录
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(your_account)
    time.sleep(random.random())
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(your_password)
    time.sleep(random.random())

    #点击确认登陆 按钮
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(8)

    #进入定帖的 网页
    my_ad_url = 'http://forum.yorkbbs.ca/houserental/4840184.aspx'
    driver.get(my_ad_url)
    time.sleep(2*random.random())

    #输入 帖子的 title
    reply_text = ['欢迎看房', '顶一下，顶～', '对了，可以看见湖哦', '顶，微笑' ,'顶顶顶', '顶', '顶一下', '顶帖']
    rand_reply = reply_text[random.randint(0,len(reply_text))]
    driver.find_element_by_xpath("//textarea[@name='message']").clear()
    driver.find_element_by_xpath("//textarea[@name='message']").send_keys(rand_reply)
    time.sleep(random.random())

    #点击确认
    driver.find_element_by_xpath("//input[@class='pButton']").click()
    time.sleep(10)
    driver.quit()
    show_text.set(f'发送：{rand_reply}')
    return None


#自动发帖
def post_rent_yorkbbs():
    #set chrome driver to headerless
    # option_ = Options()
    # option_.add_argument('--headless')

    #create driver to scrape
    # driver = webdriver.Chrome(chrome_options=option_)
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.01)

    #进入登陆 账号的 url
    url = 'http://forum.yorkbbs.ca/login.aspx'
    driver.get(url)
    time.sleep(2)

    #输入账号密码登录
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(your_account)
    time.sleep(random.random())
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(your_password)
    time.sleep(random.random())

    #点击确认登陆 按钮
    driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(8)

    #进入发帖的 网页
    post_ad_url = 'http://forum.yorkbbs.ca/posttopic.aspx?forumid=161'
    driver.get(post_ad_url)
    time.sleep(2*random.random())

    #输入 帖子的 title
    title = 'your headline'
    driver.find_element_by_xpath("//input[@name='title']").clear()
    driver.find_element_by_xpath("//input[@name='title']").send_keys(title)
    time.sleep(random.random())


    # 上传 图片1 by url
    br_pic_url = 'www.pic_url.png'
    driver.find_element_by_xpath("//a[@onclick='show_impageupload(1)']").click()
    time.sleep(2)
    driver.find_element_by_id("posteditor_btn_www").click()
    time.sleep(2)
    driver.find_element_by_id("posteditor_image_param_1").send_keys(br_pic_url)
    time.sleep(2)
    driver.find_element_by_id("posteditor_image_submit").click()
    time.sleep(6)
    driver.find_element_by_id("posteditor_image_submit").click()
    time.sleep(2)




    ##输入帖子
    #输入帖子的内容
    text = """
    your ads content
    """

    #切换到rich text editor的iframe， 才可以输入 text
    iframe_ = driver.find_element_by_xpath("//iframe[@id='posteditor_iframe']")
    driver.switch_to.frame(iframe_)
    driver.find_element_by_id("wysiwyg").send_keys(text)
    time.sleep(1)

    #上传图片2
    #从 rich text editor的 iframe 退回到 default 的mainframe中。
    driver.switch_to.default_content()
    #打开
    lr_pic_url = 'www.pic_url.com'
    driver.find_element_by_xpath("//a[@onclick='show_impageupload(1)']").click()
    time.sleep(random.random())
    driver.find_element_by_id("posteditor_btn_www").click()
    time.sleep(random.random())
    driver.find_element_by_id("posteditor_image_param_1").send_keys(lr_pic_url)
    time.sleep(2)
    driver.find_element_by_id("posteditor_image_submit").click()
    time.sleep(5)
    driver.find_element_by_id("posteditor_image_submit").click()
    time.sleep(random.random()*8)
    
    #提交
    driver.find_element_by_name('topicsubmit').click()
    time.sleep(8)
    
    #关浏览器
    driver.quit()

    show_text.set('已经POST在yorkbbs完了，亲爱的')
    return None

#逗开心
def mum():
    show_text.set('Post在哪儿？')
    return None



####function section end####




#创建显示text的界面
l = tk.Label(window,           
#     text='OMG! this is TK!',    # 标签的文字
    textvariable=show_text,  # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green',     # 背景颜色
    font=('Arial', 12),     # 字体和字体大小
    width=60, height=6  # 标签长宽
    )
l.pack()    # 固定窗口位置

   

#POST在约克BBS  button   
button_ = tk.Button(window, 
    text='POST 约克BBS',      # 显示在按钮上的文字
    width=20, height=6, 
    command=post_rent_yorkbbs   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置

                            
#顶帖 button   
button_ = tk.Button(window, 
    text='顶帖 约克BBS',      # 显示在按钮上的文字
    width=20, height=6, 
    command=up_rend_yorkbbs   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置
                            
                            
                            
#POST在别的地方？？ button   
button_ = tk.Button(window, 
    text='POST在别的地方？？',      # 显示在按钮上的文字
    width=20, height=6, 
    command=mum   # 点击按钮式执行的命令
             )     
button_.pack()    # 按钮位置

#展示界面
window.mainloop()
