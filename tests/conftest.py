import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="chrome/firefox")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(), options=options)
        driver.set_window_size(1920, 1080)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(), options=options)
        driver.set_window_size(1920, 1080)

    else:
        raise ValueError(f"Unsupported browser_name: {browser_name}")

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    # Attach to node so hooks can access it (no globals)
    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Take screenshot and embed into pytest-html report on failure.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()

    extras = getattr(report, "extras", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "Reports")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir, report.nodeid.replace("::", "_") + ".png"
            )

            driver = getattr(item, "driver", None)
            if driver:
                driver.get_screenshot_as_file(file_name)

                # Use relative path so it works when opening report locally
                rel_path = os.path.relpath(file_name, start=os.getcwd())
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>'
                    % rel_path
                )
                extras.append(pytest_html.extras.html(html))

    report.extras = extras
