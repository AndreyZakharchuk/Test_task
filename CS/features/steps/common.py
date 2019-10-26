from behave import given, when, then
from selene import browser
from selene.support.jquery_style_selectors import s
from selene.support.conditions import be
from selene.support import by
from selenium.common.exceptions import TimeoutException
from time import sleep


@given('открыта страница сайта "{url}"')
def step_impl(context, url):
    """Открывает страницу {url} сайта"""
    context.url = '%s' % url
    browser.open_url(context.url)
    s('.cookies__close').hover().click()  # закрывает уведомление о куках


@when('нажата ссылка с текстом "{step_text}"')
def step_impl(context, step_text):
    """Нажимает на ссылку с текстом step_text"""
    s(by.link_text(step_text)).hover().click()


@then('на странице есть текст "{step_text}"')
def step_impl(context, step_text):
    """Проверяет, что на странице видим текст step_text"""
    try:
        s(by.text(step_text)).should(be.visible)
    except TimeoutException:
        s(by.partial_text(step_text)).should(be.visible)


@then("открыта последняя вкладка в браузере")
def step_impl(context):
    """Переключает на последнюю вкладку браузера"""
    tab_list = browser.driver().window_handles
    browser.driver().switch_to.window(tab_list[len(tab_list) - 1])


@given('удалены все cookies')
def step_impl(context):
    """Удаляет cookies браузера"""
    browser.driver().delete_all_cookies()
    browser.driver().execute_script('window.localStorage.clear();')


@given('ожидание загрузки прелоадера')
def step_impl(context):
    """Ожидает загрузку прелоадера"""
    try:
        s('.block_content #main_container_bot[state="filled"]').should(
            be.existing)
    except TimeoutException:
        sleep(10)
