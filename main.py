import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({
        "headless": True, # This variable control whether show the browser
        "devtools":True,
    })
    page = await browser.newPage()
    await page.goto('https://www.nptu.edu.tw/p/412-1000-2972.php?Lang=zh-tw')
    
    taga = await page.evaluate("""() => {
        let href = document.querySelectorAll(".ls a")
        let arr = []
        href.forEach(value => arr.push({ "title": value.innerHTML,"href":value.href }))
        return arr
    }""")
    # await browser.close()
    
    file = open('output.txt','w+',encoding="utf8")
    for k in taga:
        file.write(str(k["title"])+":"+str(k["href"])+"\n")

asyncio.get_event_loop().run_until_complete(main())