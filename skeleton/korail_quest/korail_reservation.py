import asyncio
from playwright.async_api import async_playwright
from time import time, sleep

from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수 가져오기
ID = os.getenv('ID')
PW = os.getenv('PW')

async def korail_reservation(page, *personal_info):
    login = await page.wait_for_selector('#txtMember')
    pw = await page.wait_for_selector('#txtPwd')
    
    user_id = personal_info[0]
    user_pw = personal_info[1]
    
    await login.type(user_id)
    await pw.type(user_pw)
    await page.evaluate("""() => {
        click_button = document.querySelector('img[src="/images/btn_login.gif"]');
        click_button.click()
        };""")
    
    # 도착역 거제 변경
    # await page.evaluate("""() => {return btnPopWin(1,'txtGoEnd')};""")
    await page.evaluate("""
        document.querySelector('a[onclick="return btnPopWin(1,'txtGoEnd');"]').click();
    """)
    
    # 출발일 변경
    
    # 승차권 예매 버튼 클릭
    
    
    
    sleep(10)
    
async def main(user_id, user_pw):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = False)
        context = await browser.new_context()
        page = await browser.new_page()
        await page.goto('https://www.letskorail.com/korail/com/login.do')
        
        personal_info = (user_id, user_pw)
        await korail_reservation(page, *personal_info)
        
if __name__ == '__main__':
    asyncio.run(main(ID, PW))

