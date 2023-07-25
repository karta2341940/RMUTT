import asyncio
from pyppeteer import launch

async def main():
    # Launch a browser
    browser = await launch({
        "headless": True, # This variable control whether show the browser
        "devtools":True,
    })
    # Open a new page
    page = await browser.newPage()
    # Made the page go to the link
    await page.goto('https://www.nptu.edu.tw/p/412-1000-2972.php?Lang=zh-tw')
    # To get all the link and title of the hyperlink in the page
    taga = await page.evaluate("""() => {
        let href = document.querySelectorAll(".ls a")
        let arr = []
        href.forEach(value => arr.push({ "title": value.innerHTML,"href":value.href }))
        return arr
    }""")
    # Close the browser
    await browser.close()
    # Open or create a file that named output
    file = open('output','w+',encoding="utf8")
    for k in taga:
        # Iterable write data into "output"
        file.write(str(k["title"])+":"+str(k["href"])+"\n")

asyncio.get_event_loop().run_until_complete(main())