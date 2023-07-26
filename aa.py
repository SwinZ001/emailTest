import random
import re
import threading
from time import sleep
import requests
from lxml import etree

lua_script = '''
function main(splash, args)

    -- 自动加载jquery，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-autoload
    assert(splash:autoload("https://code.jquery.com/jquery-3.1.1.min.js"))

    -- 自定义协议头，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-set-custom-headers
    splash:set_custom_headers({
        ["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36",
        ["Referer"] = "https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.6f9a3f34WGw0u9&q=%E5%8F%A3%E7%BA%A2&suggest=history_1&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=%E5%8F%A3%E7%BA%A2&suggest_query=%E5%8F%A3%E7%BA%A2&source=suggest&filter_tianmao=tmall&tab=mall&sort=sale-desc",
        ["Cookie"] = "xlly_s=1; t=a9bc12aa4b32e889888316653c0bc68a; enc=ojMsafNe7loEkpa4N2zMw9HgmRiaK2EM%2BLaed0FLzTy%2BAvL6wTI6a%2FM8UB9RPni5yuf%2BTcbMPsuq4MLPLyEb2A%3D%3D; thw=cn; cna=ZSjhGsr/OSwCAXFvH+S+mjfR; sgcookie=E100gHGI1eD%2B8SMSb7fBC99kT1meGuu5WrITgdfSCc0yZ6x1ajwDZTyByi77%2FqNOldavLLFYUuo6k6DqP0hWxJOtz0%2BmRn2Scm3eW1rlKO%2B8W5VVKpmu4uEW84ge4ETuM1q4; uc3=id2=Uoncj3WS8M%2FmOg%3D%3D&nk2=F5RCYrtywyjivg%3D%3D&vt3=F8dCvChyvJ2Ut2%2BINTI%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; lgc=tb77188312; uc4=id4=0%40UOE2SK0sB1DE3I1K%2FexLbEmtGw1Z&nk4=0%40FY4JjC8oLE5TWfozqVdhXEQPGctu; tracknick=tb77188312; _cc_=URm48syIZQ%3D%3D; _samesite_flag_=true; cookie2=2db9d0ed262ea1dc338c900f0768126b; _tb_token_=3ee8e8b5ee330; _m_h5_tk=316a6bbadd2218c4ce1413635524fa83_1650102755233; _m_h5_tk_enc=389f634d475ed668cfda8cc0074d1f94; mt=ci=-1_0; uc1=cookie14=UoexMnzuiHX%2F7w%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; x5sec=7b227365617263686170703b32223a226664623265623037326436396536353361663734393033636161373634633564434a363336704947454b615a354c4833694b696152526f4d4d5467334e6a59304f4445314e5473784d4b6546677037382f2f2f2f2f77453d227d; JSESSIONID=6BD82B972929FA16C579BC6D9CF069B2; tfstk=cl95BRsnoz47UYhUU3iqL_K5euBCZp3fmb_JVqZCgmwU2wK5if2N5dcvtrXFvi1..; l=eBM2DDc7Lhv7T1otBOfwnurza77tQIRAguPzaNbMiOCP_zCp5pXCW62wGDY9CnGVh64pR38sRq92BeYBqIv4n5U62j-latHmn; isg=BFZW_LMkKHuHCRzSlHLmzVBYpwxY95oxaP_QVMC_WjnUg_YdKINBQPhxHx9vK5JJ"
    })

    -- 设置网络请求的默认超时时间，以秒为单位，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-resource-timeout
    splash.resource_timeout = 30.0

    -- 禁用图像加载，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-images-enabled
    splash.images_enabled = false

    -- 访问目标地址，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-go
    assert(splash:go("https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.6f9a3f34WGw0u9&q=%E5%8F%A3%E7%BA%A2&suggest=history_1&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&ie=utf8&initiative_id=tbindexz_20170306&_input_charset=utf-8&wq=%E5%8F%A3%E7%BA%A2&suggest_query=%E5%8F%A3%E7%BA%A2&source=suggest&filter_tianmao=tmall&tab=mall&sort=sale-desc"))

    -- 等待页面加载，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-wait
    assert(splash:wait(1))

    -- 设置返回类型，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-set-result-content-type
    splash:set_result_content_type("text/html; charset=utf-8")

    -- 返回HTML内容，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-html
    return splash:html()

    -- png = splash:png()   返回以PNG格式的截图，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-png
    -- har = splash:har()   返回有关网络请求和其他 Splash 活动的信息，官方说明：https://splash.readthedocs.io/en/stable/scripting-ref.html#splash-har

end
'''

params = {
    'lua_source': lua_script  # 执行lua脚本
}

'''
    http://127.0.0.1:8050/render.html?url=https://so.gushiwen.cn/user/collect.aspx&wait=5
'''

url = 'http://127.0.0.1:8050/execute'
session=requests.session()
html = session.get(url, params=params)

print(html.text)
tree=etree.HTML(html.text)
aa=tree.xpath('//*[@id="mainsrp-itemlist"]//*[@class="row row-2 title"]/a/@href')
print(len(aa))




def craw(url):
    pro_dict = ["http://114.99.6.84:4231", "http://49.89.222.115:4245", "http://114.239.1.38:4231",
                "http://183.165.249.87:4245", "http://117.95.235.214:4236", "http://180.104.255.187:4231"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
        'Cookie': 't=4ec729498dc3e30332dc544ef01ac4f6; _tb_token_=e3130e3e97e8a; cookie2=13a5045da0a9c298e1c557d2b3e01f45; dnk=tb77188312; uc1=cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie14=UoexMn3DCQoBww%3D%3D&pas=0&existShop=false&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=W5iHLLyFOGW7aA%3D%3D; uc3=id2=Uoncj3WS8M%2FmOg%3D%3D&nk2=F5RCYrtywyjivg%3D%3D&vt3=F8dCvChz3cCjAjno%2Bhc%3D&lg2=URm48syIIVrSKA%3D%3D; tracknick=tb77188312; lid=tb77188312; _l_g_=Ug%3D%3D; uc4=id4=0%40UOE2SK0sB1DE3I1K%2FexLbc7TFR8U&nk4=0%40FY4JjC8oLE5TWfozqVdhXaDmDsut; unb=1876648155; lgc=tb77188312; cookie1=Vv8bdck4Z%2BcX54ucGauOHUx19F83tZsuK2b0n0b%2BRqo%3D; login=true; cookie17=Uoncj3WS8M%2FmOg%3D%3D; _nk_=tb77188312; sgcookie=E100hJLKQX19AcOysS40ADA19v8PNZC%2FUPBQ9ZqprGj04gx%2BzdY5qOKAhwWXev2pykOK0Ri5KHM2eWZCIfiILEY7QqACdhfRnGBFP8bZdBChqx%2B6R8GPyyMsV0I3CED7Zu5B; cancelledSubSites=empty; sg=25b; csg=c3a4c57e; cna=p5PiGp65cQsCAXeD2Zrw2MU0; xlly_s=1; pnm_cku822=098%23E1hvAvvUvbZvUvCkvvvvvjiWRLshzj3WPFS9zjD2PmPOljlnPszvgjnHn2MU1jr8i9hvChCvCCpvvpvVphhvvvvvmvhvLhh6wQmFdcZIfvc6D40OjoE1paFZ5Cl0p5nC%2BnezrmphwhKn3feAOHHzLwexRdIAcVvHfwmK5eUpEZ8aiLyubhv3xw0tiCH%2BmB%2B%2BaNoIvpvUphvhv3%2Bvv8VUvpvjpyUWCE9Owb9Cvm3vpvvvvvCvphCv22Ivvh8pphvOvvvvpAnvpC9vvvC2J6CvVvvvvhnq29hvCvvvMMGgvpvhphvvvv%3D%3D; tfstk=cJiPB30Fk3KPSEZBWuZeOwx6rAVRZ9F31iyarCmbgHyed-4liu1LnGB43JWVtzf..; l=eBLvLxPuLhNWIWHBBOfwourza77OSIRAguPzaNbMiOCP9wfe5hNFW62M8PTwC3GVh6c9R38sRq94BeYBqQAonxvOa6Fy_Ckmn; isg=BMTEtpy1euz_Bc6jbXgti1YJlUK23ehHLsViSt5lUA9TCWTTBu241_qrSaHRESCf'

    }
    ip = random.choice(pro_dict)
    print(ip)
    response = session.get(url=url, headers=headers, proxies={'http': ip})
    ata_obj = response.text
    xq_tree = etree.HTML(ata_obj)
    cc = xq_tree.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/text()')
    # print(ata_obj)
    print(cc)
    print(1111111111111111111111111111111111111111111111111111111111111111111111111111111111)


threads=[]
for i in range(len(aa)):
    sleep(2)
    bb = re.sub('\w+:', "", aa[i])
    dd = "https:" + bb
    threads.append(
        threading.Thread(target=craw, args=(dd,))
    )

for thread in threads:
    thread.start()












# def craw(url):
#     response = session.get(url=url)
#     ata_obj = response.text
#     xq_tree = etree.HTML(ata_obj)
#     cc = xq_tree.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/text()')
#     if cc==[]:
#         return
#     print(url)
#     print(cc)
#
#
#
# threads=[]
# for i in range(len(aa)):
#     bb=re.sub('\w+:',"",aa[i])
#     dd="https:"+bb
#     craw(dd)
#     # threads.append(
#     #     threading.Thread(target=craw, args=(dd,))
#     # )
#
# # for thread in threads:
# #     thread.start()





# '''写入HTML'''
# with open('splash-api登录后页面2.html', 'w', encoding='utf-8') as f:
#     f.write(html.text)


# def craw(url):
#     pro_dict = ["https://125.125.78.70:4231", "http://114.230.122.107:4212", "http://114.99.12.188:4213",
#                 "http://58.243.29.230:4231", "http://49.89.143.218:42315", "http://125.125.152.96:4231"]
#     for ip in pro_dict:
#         try:
#             response = session.get(url=url, proxies={'http': ip}, timeout=5)
#             headers = {
#                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
#                             'Cookie': "_m_h5_tk=86427da79b884f633486eeb11b2166aa_1650088278552; _m_h5_tk_enc=18d68afe4eb74dfa9d24489307c96009; xlly_s=1; t=a9bc12aa4b32e889888316653c0bc68a; enc=ojMsafNe7loEkpa4N2zMw9HgmRiaK2EM%2BLaed0FLzTy%2BAvL6wTI6a%2FM8UB9RPni5yuf%2BTcbMPsuq4MLPLyEb2A%3D%3D; x5sec=7b227365617263686170703b32223a223462343865653362363864396639363532626535666261663931656664663936434f4432364a4947454f504a69504b5035626e7a45786f4d4d5467334e6a59304f4445314e5473784b414977703457436e767a2f2f2f2f2f41513d3d227d; thw=cn; cna=ZSjhGsr/OSwCAXFvH+S+mjfR; _samesite_flag_=true; cookie2=11123f3941079b42d3ce0571e37638d2; _tb_token_=b1e8773eb916; sgcookie=E100gHGI1eD%2B8SMSb7fBC99kT1meGuu5WrITgdfSCc0yZ6x1ajwDZTyByi77%2FqNOldavLLFYUuo6k6DqP0hWxJOtz0%2BmRn2Scm3eW1rlKO%2B8W5VVKpmu4uEW84ge4ETuM1q4; unb=1876648155; uc3=id2=Uoncj3WS8M%2FmOg%3D%3D&nk2=F5RCYrtywyjivg%3D%3D&vt3=F8dCvChyvJ2Ut2%2BINTI%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; csg=269f3f8e; lgc=tb77188312; cancelledSubSites=empty; cookie17=Uoncj3WS8M%2FmOg%3D%3D; dnk=tb77188312; skt=a2f0ba2c00a7ea77; existShop=MTY1MDA4MTgwNg%3D%3D; uc4=id4=0%40UOE2SK0sB1DE3I1K%2FexLbEmtGw1Z&nk4=0%40FY4JjC8oLE5TWfozqVdhXEQPGctu; tracknick=tb77188312; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=25b; _nk_=tb77188312; cookie1=Vv8bdck4Z%2BcX54ucGauOHUx19F83tZsuK2b0n0b%2BRqo%3D; mt=ci=0_1; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie14=UoexMnzv5H2JmQ%3D%3D&existShop=false&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; JSESSIONID=5CD5793D6E9F64BBA7F4729BAEE46D26; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; l=eBM2DDc7Lhv7TV_CBOfwourza77OSIRAguPzaNbMiOCPOBfp5P6cW62ZQtT9C3GVh6q2R38sRq92BeYBqIv4n5U62j-la_kmn; tfstk=cTqVB_4wyiIq3Hi1JmiN1f4U1EmAZDhiO3kEo6qc9_4VHx0ciPOtEHprUAJysqf..; isg=BMvLH6B7LcgJuHERSaUD3gUnWm-1YN_i3bC9Vz3Ip4phXOu-xTBvMmn-Mlyy_Dfa"
#                         }
#             response = session.get(url=url)
#             print(response.status_code)
#             if (response.status_code == 200):
#                 ata_obj = response.text
#                 xq_tree = etree.HTML(ata_obj)
#                 cc = xq_tree.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/text()')
#                 print(url)
#                 print(cc)
#                 print(f'{ip} 可用')
#             else:
#                 print(f'{ip} 不可用')
#         except:
#             print(f'{ip} 失败')