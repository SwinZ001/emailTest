import json
import random
import threading
from time import sleep

import openpyxl
from lxml import etree

import requests
import win32api,win32con
from selenium import webdriver
# from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
# wb = openpyxl.Workbook()
# cart_data_sheet = wb.active

# url = 'https://dy.feigua.cn/api/v1/aweme/search/list?pageSize=10&pageIndex=1&sort=0&period=6&dateFrom=2022-03-19&dateTo=2022-03-19&_=1647620982538'
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#             'Cookie': 'Hm_lvt_b9de64757508c82eff06065c30f71250=1636549762; chl=key=feigua2_baidu-pinzhuan; ASP.NET_SessionId=llv1wjqgtdeeb30nswihb3pn; Hm_lvt_876e559e9b273a58993289470c10403b=1647607059; FEIGUA=UserId=0c4d8af55e3529993cd7d3c1d97e1dda&NickName=9db1c403a424acb933dff3798a704f2bb5369475695da75061ccd07c99a58a18&checksum=84b441686f37&FEIGUALIMITID=ff29a677bd384172adf9b592064c08a7; 3b99f4eb12d4081e11c57420e45ab5f2=11c014ebad67002f9ba5bc3a4abd90b6526906ee58b41019b96baec54827a2ee31c054a9f8bbb7cc33db6f0444f1257e339ae1aedfa0ddfe18dcabf91d20934cfdc7d4641ecc4ce52585f5b303cbe0db0f5fcd503e43655758d6f3ad5a71eaf72eb5c2b1e6feced6e8e23e3c5a737a8a; SaveUserName=18998802954; Hm_lpvt_876e559e9b273a58993289470c10403b=1647620975'
#         }

# response = requests.get(url=url, headers=headers, verify=False)
# response.encoding="utf-8"
# 获取网页HTML代码
# ata_obj = response.text
# tree = etree.HTML(ata_obj)
# print(ata_obj)
# 获取网址返回的json数据
# sixTime_obj = response.json()
# print(sixTime_obj["Data"]["AwemeList"])
# for i in range(len(sixTime_obj["Data"]["AwemeList"])):
#     data_list = []
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["BloggerNickName"])
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["Desc"])
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["VideoUrl"])
#     data_list.append(sixTime_obj["Data"]["AwemeList"][i]["CoverUrl"])
#     cart_data_sheet.append(data_list)
# wb.save('G:\cart_data.xls')
# print ("over+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++over")





#
# option=Options()
# # 伪识别
# option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_experimental_option('detach',True)
# # 无界面浏览器
# # option.add_argument('--headless')
# bro = webdriver.Chrome(executable_path='D:\develop\python\python\Scripts\chromedriver.exe',chrome_options=option)
# bro.get("https://dy.feigua.cn/Member#/staticpage/video")
# 获取cookies
# sleep(30)
# bro.find_element_by_xpath('//*[@id="fb_login_qrcode"]/ul/li[2]/a').click()
# bro.find_element_by_xpath('//*[@id="fb_login_phonepwd_tel"]').send_keys("18998802954")
# bro.find_element_by_xpath('//*[@id="fb_login_phonepwd_pwd"]').send_keys("adfadf2954")
# bro.find_element_by_xpath('//*[@id="fb_login_phonepwd_btnyes"]').click()
# sleep(2)
# aa=bro.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# ActionChains(bro).drag_and_drop_by_offset(aa,350,0).perform()
# sleep(5)
# with open("cookies2.txt","w") as f:
#     f.write(json.dumps(bro.get_cookies()))
# bro.close()
#
# # 用cookies登录
# bro.delete_all_cookies()
# with open("cookies2.txt","r") as f:
#     cookies_list=json.load(f)
#     for cookie in cookies_list:
#         bro.add_cookie(cookie)
# sleep(10)
# bro.refresh()
# bro.get("https://dy.feigua.cn/Member#/staticpage/video")





# option=Options()
# option.add_argument('--disable-blink-features=AutomationControlled')
# # option.add_argument('--headless')
# bro = webdriver.Chrome(executable_path='F:\python\python3.9.10\Scripts\chromedriver.exe',chrome_options=option)
# bro.get("https://www.51job.com/")
# sleep(2)
# # .//*[@target="_blank"],加点就是当前组件内的子组件，不加就是整个html文件的子组件
# aa=bro.find_element_by_xpath('/html/body/div[5]/div[2]/div').find_elements_by_xpath('.//*[@target="_blank"]')
# print(aa)



# url = 'https://www.51job.com/'
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#             'Cookie': 'Hm_lvt_b9de64757508c82eff06065c30f71250=1636549762; chl=key=feigua2_baidu-pinzhuan; ASP.NET_SessionId=llv1wjqgtdeeb30nswihb3pn; Hm_lvt_876e559e9b273a58993289470c10403b=1647607059; FEIGUA=UserId=0c4d8af55e3529993cd7d3c1d97e1dda&NickName=9db1c403a424acb933dff3798a704f2bb5369475695da75061ccd07c99a58a18&checksum=84b441686f37&FEIGUALIMITID=ff29a677bd384172adf9b592064c08a7; 3b99f4eb12d4081e11c57420e45ab5f2=11c014ebad67002f9ba5bc3a4abd90b6526906ee58b41019b96baec54827a2ee31c054a9f8bbb7cc33db6f0444f1257e339ae1aedfa0ddfe18dcabf91d20934cfdc7d4641ecc4ce52585f5b303cbe0db0f5fcd503e43655758d6f3ad5a71eaf72eb5c2b1e6feced6e8e23e3c5a737a8a; SaveUserName=18998802954; Hm_lpvt_876e559e9b273a58993289470c10403b=1647620975'
#         }
#
# response = requests.get(url=url, headers=headers, verify=False)
# response.encoding="utf-8"
# # 获取网页HTML代码
# ata_obj = response.text
# tree = etree.HTML(ata_obj)
# aa=tree.xpath('/html/body/div[5]/div[2]/div/a')
# # print(aa)
# b=list=[]
# for i in aa:
#     b.append(i.xpath("./@href"))
#
#
# print(str(b))



option=Options()
# pro_dict = ["http://114.106.156.32:4245", "http://49.89.127.134:4236", "http://114.99.20.169:4225",
#                 "http://114.99.15.71:4278", "http://114.99.13.8:4231", "http://36.62.217.157:4245"]
# option.add_argument('--proxy-server='+random.choice(pro_dict))
# 无界面浏览器
# option.add_argument('--headless')

# 伪识别
option.add_argument('--disable-blink-features=AutomationControlled')

option.add_experimental_option('detach',True)

bro = webdriver.Chrome(executable_path='D:\develop\python\python\Scripts\chromedriver.exe',chrome_options=option)
bro.get("https://accounts.google.com/b/0/AddMailService")
# 登录
bro.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("13178800635")
bro.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("swinz1319kfy")
bro.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
# 获取数据列表
bro.implicitly_wait(30)
bb=bro.find_element_by_xpath('//*[@id="mainsrp-itemlist"]').find_elements_by_xpath('..//*[@class="row row-2 title"]/a')
print(len(bb))

# 循环跳页获取数据
def craw(url_i):
    bro.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[' + str(url_i) + ']/div[2]/div[2]/a').click()
    # 跳转操作页权限
    bro.switch_to_window(bro.window_handles[-1])
    sleep(3)
    # 模拟按下esc按钮，停止加载网页（按下抬起要一起设置，不然会一直按下，会出错）
    # 按下
    win32api.keybd_event(27, 0, 0, 0)
    # 按下抬起
    win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
    try:
        aa = bro.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1').text
    except:
        aa = bro.find_element_by_xpath('//*[@id="J_Title"]/h3').text
    finally:
        print(aa)
        bro.close()
        bro.switch_to_window(bro.window_handles[-1])
# threads=[]
# for i in range(1,len(bb)):
    # craw(i)
    # threads.append(
    #     threading.Thread(target=craw,args=(i,))
    # )
    # data_threading = threading.Thread(target=craw, args=(i,))
    # data_threading_name='线程'+str(1)
    # data_threading.start()

# for thread in threads:
#     thread.start()









#
# url = 'https://s.taobao.com/search?q=%E5%8F%A3%E7%BA%A2'
# # temp='t=fd1546dced2f11f4aa627e7e5cff8ea6; xlly_s=1; enc=j%2FDIIwjNYqiG8B014qLBHiyG70BWAFGeIniQUGkcTt5%2FJnfnCCFwDYjadyzkeaMzj6ILhPTCdRZ1MtlkPzqxzQ%3D%3D; cna=inHdGkB4gVwCAbcFVg8mX6EJ; _samesite_flag_=true; cookie2=1c85cd5ce2feadd07017c3e33622c930; _tb_token_=76be586155583; sgcookie=E100DxP%2B9cBq27xb1Hy9Rebzwy0KS0VSPyDVxDxmClnnwj1CFy0L89wBb2yh%2BrsAkuzBzU83Zi2otdmcEX4WaETd1WCQaHDrkzi8%2BFJN%2BNEogynFbiyqH3Gd1lE5Q1kAi%2FJi; unb=1876648155; uc3=id2=Uoncj3WS8M%2FmOg%3D%3D&vt3=F8dCvChwvEQAs40oGiw%3D&nk2=F5RCYrtywyjivg%3D%3D&lg2=URm48syIIVrSKA%3D%3D; csg=0d0173d1; lgc=tb77188312; cancelledSubSites=empty; cookie17=Uoncj3WS8M%2FmOg%3D%3D; dnk=tb77188312; skt=fdeca7348f360956; existShop=MTY0OTg5NDQ5OQ%3D%3D; uc4=nk4=0%40FY4JjC8oLE5TWfozqVb0Ftt0PMrj&id4=0%40UOE2SK0sB1DE3I1K%2Fe3oN%2BcsGZW8; tracknick=tb77188312; _cc_=U%2BGCWk%2F7og%3D%3D; _l_g_=Ug%3D%3D; sg=25b; _nk_=tb77188312; cookie1=Vv8bdck4Z%2BcX54ucGauOHUx19F83tZsuK2b0n0b%2BRqo%3D; mt=ci=0_1; thw=cn; _m_h5_tk=d617b8a60d9805c4974c8c3fe4206839_1649903868916; _m_h5_tk_enc=9aa0e9e77b5a0256c8a194c6b946cba6; uc1=cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&existShop=false&pas=0&cookie14=UoewCZwcLGnMWg%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D; l=eBM2DDc7Lhv7TfubBO5wKurza77ONIOfCsPzaNbMiInca6iR6F6_TNC3EqYXJdtjgtfxtety52gX3RHJ-m4U-Kwpp4wpRs5mpyJw-; tfstk=cJMhBDVtkXPCDKNiGpwBFrYWd7tOZWRURYkZQHqZ3zi_nfDNi-1NgaQ2jyLX8_1..; isg=BL6-wCZaUD4gT4Qa_GrOlXjQD9QA_4J5kAconGjGB4H8C1vl0I65iCHpg9fHM3qR; x5sec=7b227365617263686170703b32223a22626135326131356565643166323265663539616132613834643139383238333243504849335a4947454c7552354a75706f344f5a43426f4d4d5467334e6a59304f4445314e5473784b414977703457436e767a2f2f2f2f2f41513d3d227d'
# proxies_dict = {
#     "http":"http://183.151.248.104:4231",
#
# }
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#             'Cookie': "enc=j%2FDIIwjNYqiG8B014qLBHiyG70BWAFGeIniQUGkcTt5%2FJnfnCCFwDYjadyzkeaMzj6ILhPTCdRZ1MtlkPzqxzQ%3D%3D; thw=cn; cna=inHdGkB4gVwCAbcFVg8mX6EJ; sgcookie=E100sRpi5InlFwj1RQfKCr9IoMtsIeQrMpJhKluQFfT%2BIPJ9GWdKNYmQowj4KqPXyspuEyHGNG1p76Fk1rAdNWiaqjpgBNSsNb1wJlGor8wBtfYZ909wi2qK1MyPLFSQN1U8; uc3=nk2=F5RCYrtywyjivg%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dCvChwvEowjazaDrQ%3D&id2=Uoncj3WS8M%2FmOg%3D%3D; lgc=tb77188312; uc4=id4=0%40UOE2SK0sB1DE3I1K%2Fe3oN%2BcuOM%2Fm&nk4=0%40FY4JjC8oLE5TWfozqVb0Ftt2tbIP; tracknick=tb77188312; _cc_=URm48syIZQ%3D%3D; mt=ci=-1_0; xlly_s=1; JSESSIONID=E1EB85582C26A364DEF1FC6959F5CC12; cookie2=24713be23d382bf6885c37ae219142aa; t=5d318f326c4cbb6391c66861a529fc08; _samesite_flag_=true; _m_h5_tk=503ac5b46e53d8d16f9820c0e7b10080_1650011754314; _m_h5_tk_enc=475ec953989c17a00c5e4c70cddd1e82; _tb_token_=f5553ee3b8f3e; uc1=cookie14=UoexMnznk9%2Bygg%3D%3D; v=0; tfstk=cFRCBybojkqCXskzTegZa3B3jL55Zkn1SvspRcZTb6-LfMYCijVVcID9ElfPyN1..; l=eBM2DDc7Lhv7TDjEBOfZlurza779lIRfguPzaNbMiOCPO_Cp5Kb5W62_TtY9CnGVnsL9R38sRq94BXYncyzHhJpKPJLCgsDLrdTh.; isg=BCcnC_TSCWdSro3ljZmngpmztlvxrPuO0URhw_mUJLbd6EaqAX3736LqCuj2ANMG; x5sec=7b227365617263686170703b32223a226462666365663331373566373633356236626166633837663462666334633664434a7575354a4947455044446d73376d764b6d514d786f4d4d5467334e6a59304f4445314e5473784b414977703457436e767a2f2f2f2f2f41513d3d227d"
#         }
#
# response = requests.get(url=url, headers=headers, proxies=proxies_dict,verify=False)
# response.encoding="utf-8"
# # 获取网页HTML代码
# ata_obj = response.text
# tree = etree.HTML(ata_obj)
# aa=tree.xpath('/html/head/title')
# print(aa)
# b=list=[]
# for i in aa:
#     b.append(i.xpath("./@href"))


# print(str(b))



#
# pro_dict=["https://125.125.78.70:4231","http://114.230.122.107:4212","http://114.99.12.188:4213","http://58.243.29.230:4231","http://49.89.143.218:42315","http://125.125.152.96:4231"]
# for ip in pro_dict:
#     try:
#         response = requests.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=ip&fenlei=256&oq=%25E8%258A%259D%25E9%25BA%25BB%25E4%25BB%25A3%25E7%2590%2586&rsv_pq=8b88f62b000414b4&rsv_t=3105PVlLKg2qtCeMTF%2FKjY7FpiDnYwKqTydPTtop%2FutKLiLcuTRfkE8zcQ0&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&inputT=2295&rsv_sug3=14&rsv_sug1=10&rsv_sug7=100&prefixsug=ip&rsp=0&rsv_sug4=2295", proxies={'http':ip}, timeout=5)
#         print(response.status_code)
#         print(response.text)
#         if(response.status_code==200):
#             print(f'{ip} 可用')
#         else:
#             print(f'{ip} 不可用')
#     except:
#         print(f'{ip} 失败')

# proxies_dict={
#     "http":"http://"+pro_dict[1]
# }
