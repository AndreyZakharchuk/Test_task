from behave import given, when, then
from selene.support.jquery_style_selectors import s, ss
from selenium.common.exceptions import TimeoutException
from time import sleep

@given('открыто "{count}" слайдера на странице faq')
def step_impl(context, count):
    """Проверят, что при открытие страницы открыто "{count}" слайдеров"""
    count_new = len(ss('.faq_item.is_active'))
    count = int(count)
    assert count_new == count, 'Два слайдера не открыто'


@when('закрыть все открытые слайдеры на странице faq')
def step_iml(context):
    """Предусловие для теста: закрывает все открытые слайдеры на странице faq"""
    count = len(ss('.is_active .item_title'))
    while count != 0:
        s('.is_active .item_title').hover().click()
        count -= 1


@then('закрыты все слайдеры на странице faq')
def step_impl(context):
    """Проверяет, что закрыты все открытые слайдеры на странице faq"""
    count = len(ss('.is_active .item_title'))
    assert count == 0, 'Все слайдеры не закрыты'


@when('открыть все слайдеры на странице faq')
def step_impl(context):
    """Открывает все слайдеры на странице faq"""
    selectors = ss('.faq_item')
    context.count = 0
    for selector in selectors:
        try:
            sleep(0.5)
            selector.hover().click()
            context.count += 1
        except TimeoutException:
            pass


@then('открыты все слайдеры на странице faq')
def step_impl(context):
    """Проверяет, что открыты все сладйеры на странице faq"""
    count_new = len(ss('.faq_item.is_active'))
    assert context.count == count_new, 'Все слайдеры не открыты'


@then("ссылка '{url}' равна внешней ссылке в футере '{URL2}'")
def step_impl(context, url, URL2):
    """Сравнвиает две ссылки"""
    URL2 = int(URL2)
    assert ss('.footer_bottom_social .footer_bottom_social_link')[URL2].get_attribute(
        "href") == url, 'Ссылки в футере не равны'
