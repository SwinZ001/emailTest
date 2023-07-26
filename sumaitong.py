from time import sleep
import undetected_chromedriver.v2 as uc
import win32api
import win32con
from selenium.webdriver.common.by import By
import threading

class Ali_Express_Register():
    # 初始化
    def __init__(self):
        # 浏览器设置
        bro = self.chrome_set()
        # 速卖通界面
        # self.Ali_Expres_Interface(bro)

        self.Gmail_Interface(bro)




    # 浏览器设置
    def chrome_set(self):
        chrome_options = uc.ChromeOptions()
        # --禁用扩展
        chrome_options.add_argument("--disable-extensions")
        # # --禁用弹出窗口阻止
        chrome_options.add_argument("--disable-popup-blocking")
        # --配置文件目录=默认值
        chrome_options.add_argument("--profile-directory=Default")
        # --忽略证书错误
        chrome_options.add_argument("--ignore-certificate-errors")
        # --禁用插件发现
        chrome_options.add_argument("--disable-plugins-discovery")
        # --隐姓埋名
        chrome_options.add_argument("--incognito")
        # --没有第一次运行
        chrome_options.add_argument('--no-first-run')
        # --无服务自动运行
        chrome_options.add_argument('--no-service-autorun')
        # --无默认浏览器检查
        chrome_options.add_argument('--no-default-browser-check')
        # --密码存储=基本
        chrome_options.add_argument('--password-store=basic')
        # --没有沙箱
        chrome_options.add_argument('--no-sandbox')


        bro = uc.Chrome(version_main=104,use_subprocess=True, options=chrome_options)
        # //浏览器最大化，不覆盖任务栏
        bro.maximize_window()

        return bro

    # # 不是加载网址的停止超时页面加载
    # def stop_load_page(self, sec):
    #     sleep(sec)
    #     win32api.keybd_event(27, 0, 0, 0)
    #     win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)

    # 登录速卖通
    def login_Interface(self,bro):
        bro.get("https://www.aliexpress.com/")
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@class="_24EHh"]').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@class="btn-close"]').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@class="_34l2i"]').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH,'//*[@label="Email"]').send_keys('fa267754@gmail.com')
        bro.find_element(By.XPATH,'//*[@label="Password"]').send_keys('During81287')
        bro.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div/div/div[2]/div/div/button[2]').click()


    # 速卖通注册界面
    def Ali_Expres_Interface(self,bro):
        bro.get("https://www.aliexpress.com/")
        sleep(50)
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@class="_24EHh"]').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@class="btn-close"]').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@id="home-firstscreen"]/div/div/div[4]/div/div[2]/div/span[1]').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH,'//*[@label="Email address"]').send_keys('alvarezwann@gmail.com')
        bro.find_element(By.XPATH,'//*[@label="Password"]').send_keys('s61711cHtQ3')
        bro.find_element(By.XPATH, '//*[@id="batman-dialog-wrap"]/div/div/div[1]/div[2]/div/div/div/button').click()
        #邮箱登录接受验证码
        self.Gmail_Interface(bro)




    # 邮箱登录接受验证码界面
    def Gmail_Interface(self,bro):
        js = 'window.open("https://accounts.google.com/b/0/AddMailService");'
        bro.execute_script(js)
        bro.switch_to.window(bro.window_handles[-1])
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('alvarezwann@gmail.com')
        bro.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
        bro.implicitly_wait(30)
        bro.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('s61711cHtQ3')
        bro.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
        bro.implicitly_wait(60)
        # 点击邮件
        bro.find_element(By.XPATH, '//*[@class="ae4 aDM nH oy8Mbf"]/div[3]/div/table/tbody/tr[1]/td[5]').click()

        try:
            bro.implicitly_wait(2)
            mail_code = bro.find_element(By.XPATH,
                                         '//*[@jslog="20277; u014N:xr6bB; 4:W251bGwsbnVsbCxbXV0."]/div/div[1]/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/table/tbody/tr/td/div/div/div[4]').text
        except:
            try:
                mail_code = bro.find_element(By.XPATH,
                                             '//*[@jslog="20277; u014N:xr6bB; 4:W251bGwsbnVsbCxbXV0."]/div/div[1]/table/tbody/tr/td/div/table/tbody/tr/td/div/table/tbody/tr/td/div/div/div[1]').text
            except:
                bro.find_element(By.XPATH, '//*[@class="h7 bg ie nH oy8Mbf"]/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div/img').click()
                bro.implicitly_wait(2)
                mail_code = bro.find_element(By.XPATH,
                                             '//*[@jslog="20277; u014N:xr6bB; 4:W251bGwsbnVsbCxbXV0."]/div/div/div[2]/div[1]/table/tbody/tr/td/div[3]/table/tbody/tr/td/div/table/tbody/tr/td/div/div/div[4]').text

        for i in mail_code:
            print(i, end="\n")
        sleep(500)



if __name__ == "__main__":
    Ali=Ali_Express_Register()