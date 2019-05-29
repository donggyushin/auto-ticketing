import time
from selenium import webdriver
from secret import *

driver = webdriver.Chrome('/Users/sindong-gyu/Documents/chromedriver')
driver.get('http://txbus.t-money.co.kr/main.do')

# Select departure
departure = driver.find_element_by_css_selector('#depr_Trml_Nm').click()
# Waiting for render of departure selector
time.sleep(2)


# Finding '동서울' then click
lists = driver.find_elements_by_class_name('case')
i = 0
for l in lists:
    i = i + 1
    a_tag_to_click = driver.find_element_by_css_selector(
        '#areaList01 > li:nth-child({}) > a'.format(i))
    span_text = driver.find_element_by_css_selector(
        '#areaList01 > li:nth-child({}) > a > span:nth-child(1)'.format(i)).text
    if span_text == '서울남부':
        break

a_tag_to_click.click()


# Select arrival
arrival = driver.find_element_by_css_selector('#arvl_Trml_Nm').click()
time.sleep(2)

lists = driver.find_elements_by_class_name('case')
i = 0
# areaList02 > li:nth-child(127) > a
for l in lists:
    i = i + 1
    a_tag_to_click = driver.find_element_by_css_selector(
        '#areaList02 > li:nth-child({}) > a'.format(i))
    span_text = driver.find_element_by_css_selector(
        '#areaList02 > li:nth-child({}) > a > span:nth-child(1)'.format(i)).text
    if span_text == '양지':
        break

a_tag_to_click.click()

# Search
search_button = driver.find_element_by_css_selector('#onewayInfo > div > p >a')
driver.execute_script("arguments[0].click();", search_button)
agree_button = driver.find_element_by_css_selector(
    '#onewayInfo > div > div > div > a:nth-child(1)')
driver.execute_script('arguments[0].click();', agree_button)


# Find appropriate time ticket
# forth button
# contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child(7) > td:nth-child(7) > div > a
# fifth button
# contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child(9) > td:nth-child(7) > div > a
# Not working button
# contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child(1) > td:nth-child(7) > div > a
# This button's a tag classname is btn_reservation disabled
i = 5
while True:
    i = i + 2
    ticket_reservation_btn = driver.find_element_by_css_selector(
        '#contents > div.cont_wrap > div > div.right_cont > div > div.accordian_table.pc_ver > table > tbody > tr:nth-child({}) > td:nth-child(7) > div > a'.format(i))
    class_name = ticket_reservation_btn.get_attribute('class')
    if class_name != 'btn_reservation disabled':
        break

ticket_reservation_btn.click()
alert = driver.switch_to.alert
alert.accept()

# Select seat from number 1
# first seat
# contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu2 > div > ul.line1 > li:nth-child(1) > a > img
# second seat
# contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu2 > div > ul.line1 > li:nth-child(2) > a > img
# disabled seat
#contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu2 > div > ul.line2 > li.case1.disabled > a > img
# disabled seat's classname is disabled or case1 disabled

line = 1
child = 0

while True:

    if child == 4:
        child = 0
        line = line + 1
    child = child + 1
    seat = driver.find_element_by_css_selector(
        '#contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu2 > div > ul.line{} > li:nth-child({}) > a'.format(line, child))
    seat_classname = driver.find_element_by_css_selector(
        '#contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu2 > div > ul.line{} > li:nth-child({})'.format(line, child)).get_attribute('class')
    if seat_classname == 'disabled' or seat_classname == 'case1 disabled':
        continue
    break


seat.click()
next_btn = driver.find_element_by_css_selector(
    '#contents > div.cont_wrap > div > div.right_cont > div > div.buy_area > ul > li.menu4.mgt_type11 > p > a')
next_btn.click()

all_agree_btn = driver.find_element_by_css_selector(
    '#contents > div.cont_wrap > div > div.right_cont > div > div.private > label:nth-child(2) > input')
all_agree_btn.click()
card_selecotr = driver.find_element_by_css_selector(
    '#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(2) > td > div > div > p > a')
card_selecotr.click()

NH_card = driver.find_element_by_css_selector(
    '#cardInfo > div:nth-child(34) > table > tbody > tr:nth-child(2) > td > div > div > ul > li:nth-child(4) > a')
NH_card.click()

INPUT = driver.find_element_by_name('card_No1')
INPUT.send_keys(CARD_NUM1)
INPUT = driver.find_element_by_name('card_No2')
INPUT.send_keys(CARD_NUM2)
INPUT = driver.find_element_by_name('card_No3')
INPUT.send_keys(CARD_NUM3)
INPUT = driver.find_element_by_name('card_No4')
INPUT.send_keys(CARD_NUM4)

INPUT = driver.find_element_by_name('month')
INPUT.send_keys(VALIDITY_MONTH)
INPUT = driver.find_element_by_name('year')
INPUT.send_keys(VALIDITY_YEAR)
INPUT = driver.find_element_by_name('card_Pwd')
INPUT.send_keys(CARD_PASSWORD)
INPUT = driver.find_element_by_name('brdt')
INPUT.send_keys(RESIDENT_REGISTRATION_NUMBER)
INPUT = driver.find_element_by_name('mrsp_Brdt')
INPUT.send_keys(RESIDENT_REGISTRATION_NUMBER)
INPUT = driver.find_element_by_name('mrsp_Tel_No2')
INPUT.send_keys(PHONE_NUM1)
INPUT = driver.find_element_by_name('mrsp_Tel_No3')
INPUT.send_keys(PHONE_NUM2)
INPUT = driver.find_element_by_name('mobile_pwd')
INPUT.send_keys(PHONE_NUM2)
