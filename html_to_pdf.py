import asyncio
from pyppeteer import launch
import os

async def save_pdf(url, output_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.pdf({'path': output_path, 'format': 'A4'})
    await browser.close()

def html_to_pdf(url):
    loop = asyncio.get_event_loop()
    output_pdf_path = os.getcwd() + 'processed_files/output.pdf'
    loop.run_until_complete(save_pdf(url, output_pdf_path))