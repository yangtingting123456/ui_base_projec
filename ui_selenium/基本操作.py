from selenium import webdriver
import os
driver_path = os.path.join(os.path.abspath(__file__),'../../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
#1.浏览器中加载URL
driver.get('https://www.baidu.com')
#2.浏览器最大化
driver.maximize_window()
#3.浏览器最小化
driver.minimize_window()
#4.自定义窗口大小
driver.set_window_size(200,200)
# 5.刷新
driver.refresh()
#6.返回上一页
driver.back()
#7.向前进一页
driver.forward()
#8.截图
sreenshot_path = os.path.join(os.path.abspath(__file__),'../../screenshot/a.png')
print(sreenshot_path)
driver.save_screenshot(sreenshot_path)
#9.获取当前页面的url
driver.current_url
#10.获取当前页面的title
driver.title
#11.获取当前页面的源代码
driver.page_source
#12.关闭当前tab
driver.close()
#退出当前driver
driver.quit()

