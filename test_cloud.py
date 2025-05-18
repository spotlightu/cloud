from playwright.sync_api import sync_playwright

def test_page_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()
        page.goto("https://example.com") # переходим по ссылке
        assert "Example" in page.title() # проверяем наличие Example в заголовке
        page.locator("a:has-text('More information')").click() # ищем элемент, содержащий 'More information', по css - селектору и кликаем на него
        page.wait_for_url("https://www.iana.org/help/example-domains") # проверяем, что произошёл редирект по нужной ссылке
