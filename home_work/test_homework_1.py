import pytest
from playwright.sync_api import sync_playwright

def test_todomvc_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        #1. Open site
        page.goto("https://demo.playwright.dev/todomvc")

        # Wait page loading
        page.wait_for_selector(".new-todo")

        #2. Add 3 tasks
        todos = ["Buy milk", "Write code", "Walk dog"]
        for task in todos:
            page.locator(".new-todo").fill(task)
            page.locator(".new-todo").press("Enter")

        #3. Mark first task like done
        page.locator(".todo-list li").nth(0).locator(".toggle").click()

        #4 Delete second task
        second_task = page.locator(".todo-list li").nth(1)
        second_task.hover()
        second_task.locator(".destroy").wait_for(state="visible")
        second_task.locator(".destroy").click()

        #5 Check how many task do we have
        remaining = page.locator(".todo-count").text_content()
        print("left tasks: ", remaining)

        assert "1 item left" in remaining

        #done
        context.close()
        browser.close()

if __name__ == "__main__":
    test_todomvc_workflow()


