from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains
driver_path = os.path.join(os.path.abspath(__file__),'../../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.cnblogs.com/tingting-yang/')
driver.get('https://www.baidu.com')
driver.maximize_window()
#1.通过id定位
# driver.find_element_by_id("kw").send_keys("selenium id 定位")

#2.通过name定位
# driver.find_element_by_name("wd").send_keys("selenium name 定位")

#3.通过class_name 定位
# driver.find_element_by_class_name("s_ipt").send_keys("selenium class_name 定位")

#4.通过 tag_name 定位，是最不准的定位，因为一个网上上同一个tag那么重复的可能性很大
# driver.find_element_by_tag_name("input").send_keys("selenium tag_name 定位")

#5.通过link_text 定位
# driver.find_element_by_link_text("新闻").click()

#6.通过partial_link_text 定位
# driver.find_element_by_partial_link_text("新").click()

#7.通过css定位
# driver.find_element_by_css_selector()

#8.通过xpath 定位,xpath 常用有6中定位元素方法
# 8.1 绝对路径，角度路径的开头是一个斜线(/),从网页的根节点html开始，逐层去查找需要定位
#的元素。
# driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input').send_keys('xpath 绝对路径定位')
#备注：当同一个层次有多个相同的元素时，使用下标区分，下标从1开始。
# 8.2 相对路径的开头是两个斜线（//）,表示文件中所有符合模式的元素都会被找到，即使是处于树
# 中不通的层级也会被选出来。
# driver.find_element_by_xpath('//form/span[1]/input').send_keys('selenium xpath 相对路径定位1')
# driver.find_element_by_xpath('//span[1]/input').send_keys('selenium xpath 相对路径定位2')
# 备注：以上都可以定位到百度搜索框，相对路径的长度和开始位置并不受限制，可以采用从后往前逐级定位
#直到定位到即可的方式去定位。

# 8.3 元素索引，遇到同层级相同标签元素时，可以使用索引（下标）表示，缩影的初始值为1
# driver.find_element_by_xpath('//div/div[3]/a[2]').click()

# 8.4 元素属性,要求属性能够定位到唯一一个元素，如果存在多个相同标签，默认定位第一个，
#具体隔离 //标签名[@属性="属性值"] 支持使用 and 和 or 关键字，多个属性一起定位
# driver.find_element_by_xpath('//a[@href="http://news.baidu.com"]').click()
# driver.find_element_by_xpath('//a[@href="http://news.baidu.com" or @class="mnav c-font-normal c-color-t"] ').click()
# driver.find_element_by_xpath('//a[@href="http://news.baidu.com" and @target="_blank"]').click()

# 8.5 元素部分属性值（也称为模糊方法定位）
#属性值如果太长活网页中的元素属性动态变化，可以使用此方法
# (1)元素属性值开头包含内容： start-with()
# driver.find_element_by_xpath("//a[start-with(@name,'')]").click()

#(2)元素属性值结尾包含内容substring()
# driver.find_element_by_xpath("//a[substring(@href,9)='123']").click()

# (3)contains
# driver.find_element_by_xpath("//a[contains(@href,'hao')]").click()

# 8.6 元素文本在xpath中可以通过text()函数获取，也可以用其来进行元素定位。
# driver.find_element_by_xpath('//a[text()="新闻"]').click()
# driver.find_element_by_xpath('//a[contains(text(),"新")]').click()
time.sleep(3)
driver.quit()