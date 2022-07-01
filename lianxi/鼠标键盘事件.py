# -- coding: utf-8 --
# @Time : 2022/7/1 9:13
# @Author : siyu.yang
# 在实际的web产品测试中，对于鼠标的操作，不单单只有click(),有时候还要用到
# 右击、双击、拖动等操作，这些操作包含在ActionChains 类中。
# context_click() :右击
# double_click()      :双击
# drag_and_drop()      :拖动
# move_to_element()    :鼠标移动到一个元素上
# click_and_hold()     : 按下鼠标左键在一个元素上
#鼠标右击导包
from selenium.webdriver.common.action_chains import ActionChains
