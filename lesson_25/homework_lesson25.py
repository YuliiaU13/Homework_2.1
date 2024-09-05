"""Написати 25 XPath та 25 CSS локаторів для сайту
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
Дані для входу на сайт -
login - guest
pass - welcome2qauto
Для доступу через селеніум можна використати наступну конструкцію -
driver.get("<https://UserName:Password@qauto2.forstudy.space>;");"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
time.sleep(2)

# xpath
xpath_locator = driver.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']")
css_locator = driver.find_element(By.CSS_SELECTOR, 'a.contacts_link.h4')


XPATH_LOCATORS = {
    "header_basic": '//header[@class="header bg-basic-dark"]',
    "header_logo": '//a[@class="header_logo"]',
    "home_link": '//a[@class="btn header-link -active"]',
    "about_item": '//button[text()="About"]',
    "contacts_item": '//button[@appscrollto="contactsSection"]',
    "guest_log_in": '//button[text()="Guest log in"]',
    "sign_in_button": '//div[@class="header_right d-flex align-items-center"]/button[text()="Sign In"]',
    "hero_title": '//*[@*="hero-descriptor_title display-2"]',
    "hero_description": '//p[@class="hero-descriptor_descr lead"]',
    "sign_up_button": '//button[@class="hero-descriptor_btn btn btn-primary"]',
    "player_area": '//*[@*="ytp-cued-thumbnail-overlay-image"]',
    "player_logo": '//*[@*="ytp-title-channel-logo"]',
    "player_title_link": '//*[@*="ytp-title-link yt-uix-sessionlink"]',
    "player_watch_logo": '//button[@class="ytp-watch-later-button ytp-button ytp-show-watch-later-title"]//div[1]',
    "player_share_logo": '//body[@dir="ltr"]//div[@data-layer="1"]//div[@class="ytp-share-icon"]',
    "player_watch_text": '//div[text()="Смотреть позже"]',
    "player_share_text": '//div[text()="Поделиться"]',
    "play_button": '//body[@dir="ltr"]//div[@data-layer="4"]//button[@aria-label="Смотреть"]',
    "about_section": '//div[@id="aboutSection"]',
    "about_section_left":
        '//div[@class="about-block_picture about-picture"]/img[@src="/assets/images/homepage/info_1.jpg"]',
    "about_section_right":
        '//div[@class="about-block_picture about-picture"]/img[@src="/assets/images/homepage/info_2.jpg"]',
    "contacts_left": '//div[@class="col-md-6 d-flex flex-column align-items-center align-items-md-start"]',
    "contacts_right":
        '//div[@class="col-md-6 d-flex flex-column align-items-center align-items-md-end justify-content-md-end mb-2 '
        'mt-3 mt-md-0"]',
    "contacts_linked_in_logo": '//div[@class="col-md-6 d-flex flex-column align-items-center align-items-md-start"]/div//a[5]',
    "contacts_it_hillel_logo": '//div[@class="section contacts"]//a[@href="https://ithillel.ua"]',
    "contacts_email": '//div/a[@href="mailto:developer@ithillel.ua"]'
}

CSS_LOCATORS = {
    "header_basic": "header.header.bg-basic-dark",
    "header_left_menu_items": ".container .header_nav",
    "header_logo": "div.container .header_left.d-flex.align-items-center a.header_logo",
    "home_link": "a.btn.header-link.-active",
    "about_item": 'button[appscrollto="aboutSection"]',
    "contacts_item": 'button[appscrollto="contactsSection"]',
    "sign_in_button": "button.btn.btn-outline-white.header_signin",
    "hero_title": "h1.hero-descriptor_title.display-2",
    "hero_description": "p.hero-descriptor_descr.lead",
    "sign_up_button": ".hero-descriptor_btn.btn.btn-primary",
    "player_area": "div.ytp-cued-thumbnail-overlay-image",
    "player_logo": "a.ytp-title-channel-logo",
    "player_bottom_link": "a.ytp-watermark.yt-uix-sessionlink",
    "player_watch_logo": "div.ytp-watch-later-icon",
    "player_share_logo": "div.ytp-share-icon",
    "player_watch_text": "div.ytp-watch-later-title",
    "player_share_text": "div.ytp-share-title",
    "play_button": 'button[aria-label="Смотреть"]',
    "about_section": "#aboutSection",
    "about_section_left": 'img[src="/assets/images/homepage/info_1.jpg"]',
    "about_section_right": 'img[src="/assets/images/homepage/info_2.jpg"]',
    "contacts_left": ".section.contacts .col-md-6.d-flex.flex-column.align-items-center.align-items-md-start",
    "contacts_facebook_logo": 'div.contacts_socials.socials a[href="https://www.facebook.com/Hillel.IT.School"]',
    "contacts_telegram_logo": 'a.socials_link span.socials_icon.icon.icon-telegram,'
    "contacts_email" 'a.contacts_link.h4'
}

"input[name='username']"
"div.header a[href='/home']"
"button.login-btn"

driver.quit()