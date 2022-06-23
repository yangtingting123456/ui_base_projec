from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver_path = os.path.join(os.path.abspath(__file__),'../../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.cnblogs.com/tingting-yang/')
driver.get('https://www.baidu.com')
driver.maximize_window()
#1.通过id定位
# driver.find_element(By.ID,"kw").send_keys("selenium id 定位")

#2.通过name定位
# driver.find_element(By.NAME,"wd").send_keys("selenium name 定位")

#3.通过class_name 定位
# driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("selenium class_name 定位")

#4.通过 tag_name 定位，是最不准的定位，因为一个网上上同一个tag那么重复的可能性很大
# driver.find_element(By.TAG_NAME,"input").send_keys("selenium tag_name 定位")

#5.通过link_text 定位
# driver.find_element(By.LINK_TEXT,"新闻").click()

#6.通过partial_link_text 定位
# driver.find_element(By.PARTIAL_LINK_TEXT,"新").click()

#7.通过css定位
# 7.1 绝对路径是从网页的根节点html开始，逐层去查找需要定位的元素。
# 此方法缺点显而易见，当页面元素位置发生变化时，都需要修改，因此不推荐
# driver.find_element(By.CSS_SELECTOR,'html body div#wrapper div#head div.head_wrapper div.s_form div.s_form_wrapper.soutu-env-mac.soutu-env-index form#form span.bg.s_ipt_wr.quickdelete-wrap input#kw').send_keys('selenium css 绝对路径定位')
# 备注：当同一层次有多个相同的元素时，使用id或class区分，遇到id用#号，遇到class用.

# 7.2 通过相对路径,相对路径表示文件中所有符合模式的元素都会被选出来，即使是处于不同的层级也会被选出来。
# driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('selenium css 相对定位1')
# driver.find_element(By.CSS_SELECTOR,'input#kw').send_keys('selenium css 相对定位2')

# 7.3 使用元素属性爹娘各位
# 元素属性定位要求属性能够定位唯一一个元素，如果存在多个相同标签
# 默认第一个，具体格式 //标签名[属性 = ‘属性值’],支持使用多个属性一起定位元素
# driver.find_element(By.CSS_SELECTOR,'input[name="wd"]').send_keys('selenium css 属性值定位')
# driver.find_element(By.CSS_SELECTOR,'input[name="wd"][class="s_ipt"]').send_keys('selenium css 多属性值定位')

# 7.4 使用部分属性值匹配（也称为模糊方法定位）
# 属性值如果太长或网页中的元素属性动态变化，可以使用此方法
# 元素属性值开头包含内同： ^=
# driver.find_element(By.CSS_SELECTOR,'a[href^="http://news."]').click()
#元素属性值结尾包含内容： $=
# driver.find_element(By.CSS_SELECTOR,'a[href$="news.baidu.com"]').click()
#圆度属性
# driver.find_element(By.CSS_SELECTOR,'a[href*="news"]').click()

# 7.5查询子元素
# 1）子元素 A>B
# driver.find_element(By.CSS_SELECTOR,'form>span>input').send_keys('css 子元素定位')
# 2）后代元素 A空格B (类似 >)
# driver.find_element(By.CSS_SELECTOR,'form span input').send_keys('后代元素')
# 3）第一个后代元素： first-child
driver.find_element(By.CSS_SELECTOR,'a#s-top-username a:first-child').click()

# 4）最后一个后代元素
# a = driver.find_element(By.CSS_SELECTOR,'div#u1 a:last-child')

# 5）第n个元素： nth-child
# driver.find_element(By.CSS_SELECTOR,'div#u1 a:nth-child(3)').click()

# 7.6查询兄弟元素
# 1)同层级下一个元素  +
# driver.find_element(By.CSS_SELECTOR,'div#u1 a+a')
# 2）选择同层级多个相同标签的元素
# driver.find_element(By.CSS_SELECTOR,'div#u1 a ~ a')


#8.通过xpath 定位,xpath 常用有6中定位元素方法
# 8.1 绝对路径，角度路径的开头是一个斜线(/),从网页的根节点html开始，逐层去查找需要定位
#的元素。
# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input').send_keys('xpath 绝对路径定位')
#备注：当同一个层次有多个相同的元素时，使用下标区分，下标从1开始。
# 8.2 相对路径的开头是两个斜线（//）,表示文件中所有符合模式的元素都会被找到，即使是处于树
# 中不通的层级也会被选出来。
# driver.find_element(By.XPATH,'//form/span[1]/input').send_keys('selenium xpath 相对路径定位1')
# driver.find_element_(By.XPATH,'//span[1]/input').send_keys('selenium xpath 相对路径定位2')
# 备注：以上都可以定位到百度搜索框，相对路径的长度和开始位置并不受限制，可以采用从后往前逐级定位
#直到定位到即可的方式去定位。

# 8.3 元素索引，遇到同层级相同标签元素时，可以使用索引（下标）表示，缩影的初始值为1
# driver.find_element(By.XPATH,'//div/div[3]/a[2]').click()

# 8.4 元素属性,要求属性能够定位到唯一一个元素，如果存在多个相同标签，默认定位第一个，
#具体隔离 //标签名[@属性="属性值"] 支持使用 and 和 or 关键字，多个属性一起定位
# driver.find_element(By.XPATH,'//a[@href="http://news.baidu.com"]').click()
# driver.find_element(By.XPATH,'//a[@href="http://news.baidu.com" or @class="mnav c-font-normal c-color-t"] ').click()
# driver.find_element(By.XPATH,'//a[@href="http://news.baidu.com" and @target="_blank"]').click()

# 8.5 元素部分属性值（也称为模糊方法定位）
#属性值如果太长活网页中的元素属性动态变化，可以使用此方法
# (1)元素属性值开头包含内容： start-with()
# driver.find_element(By.XPATH,"//a[start-with(@name,'')]").click()

#(2)元素属性值结尾包含内容substring()
# driver.find_element(By.XPATH,"//a[substring(@href,9)='123']").click()

# (3)contains
# driver.find_element(By.XPATH,"//a[contains(@href,'hao')]").click()

# 8.6 元素文本在xpath中可以通过text()函数获取，也可以用其来进行元素定位。
# driver.find_element(By.XPATH,'//a[text()="新闻"]').click()
# driver.find_element(By.XPATH,'//a[contains(text(),"新")]').click()
time.sleep(3)
driver.quit()