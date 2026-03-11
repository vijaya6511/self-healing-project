
from playwright.sync_api import sync_playwright
from login_page import LoginPage
from utils.reporter import HealingReporter


def test_login():

    report = HealingReporter()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        # Capture original DOM
        with open("original_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("DOM saved to original_dom.html")

        # Simulate DOM change
        page.evaluate("""
            document.getElementById('user-name').id = 'dog';
        """)
        print("DOM ID changed from 'password' to 'fail'")
        print("hello")

        # Capture updated DOM
        with open("updated_dom.html", "w", encoding="utf-8") as f:
            f.write(page.content())
        print("DOM saved to updated_dom.html")

        lp = LoginPage(page)
        lp.login("standard_user", "secret_sauce")

        page.wait_for_selector(".inventory_list")
        print("Login successful")

        # generate report automatically
        lp.reporter.generate_report()

        browser.close()


test_login()

# from playwright.sync_api import sync_playwright
# from login_page import LoginPage


# def save_dom(page, file_name):
#     # capture FULL DOM structure (not just UI HTML)
#     dom = page.evaluate("document.documentElement.outerHTML")

#     with open(file_name, "w", encoding="utf-8") as f:
#         f.write(dom)

#     print(f"DOM saved to {file_name}")


# def test_login():

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         page.goto("https://www.saucedemo.com/")

#         page.wait_for_selector("#user-name")

#         save_dom(page, "original_dom.html")

#         # Simulate DOM change (username id changed)
#         page.evaluate("""
#             document.getElementById('user-name').id = 'fail';
#         """)
#         print("DOM ID changed from 'user-name' to 'fail'")

#         # AFTER DOM snapshot
#         save_dom(page, "updated_dom.html")

#         # Continue with framework login
#         lp = LoginPage(page)
#         lp.login("standard_user", "secret_sauce")

#         page.wait_for_selector(".inventory_list")
#         print("Login successful")

#         # Generate healing report
#         lp.reporter.generate_report()

#         browser.close()


# test_login()