from behave import given, when, then
from selene import browser
from selene.support.jquery_style_selectors import s, ss
from selene.support import by
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys


@when('активировать чек бокс про-версия')
def step_impl(context):
    """Активирует чек бокс про-версия"""
    context.pro_version = s(".trade_container.wrapper").get_attribute('version')
    actions = ActionChains(browser.driver())
    actions.click(s(".filter_mobile_container .filter_checkbox_switch [name='proVersion']")).perform()
    sleep(2)


@then('активирован чек бокс про-версия')
def step_impl(context):
    """Проверяет, что фильтр про-версия установлен"""
    assert context.pro_version != s(".trade_container.wrapper").get_attribute('version'), 'Фильтр не установлен'


@when('установить фильтр качества в состояние "{value}" (FN, MW, FT, WW, BS)')
def step_impl(context, value):
    """Устанавливает в фильтре качество"""
    s(by.text('Качества')).hover()
    s('.list_menu_list [data-option="%s"]' % value).hover().click()


@then('установлен фильтр качества в состояние "{value}" (FN, MW, FT, WW, BS)')
def step_impl(context, value):
    """Проверяет, что фильтр качества установлен в состояние '{value}'"""
    assert s('.block_menu_list_link .is_active[data-option="%s"]' % value).get_attribute(
        'class') == 'is_active', 'фильтр качества не установлен'


@when(
    'установить фильтр тип в состояние "{value}" (Ключи, Перчатки, Ножи, Пистолеты, Штурмовые винтовки, Снайперские винтовки, Пистолеты-пулеметы, Дробовики, Музыка, Пулеметы, Значки, Стикеры, Граффити, Кейсы)')
def step_impl(context, value):
    """Устанавливает фильтр тип в состояние {value}"""
    s(by.text('Типы')).hover()
    s('.filter_mobile_container .filter_exterior_type .list_menu_dropdown [title="%s"]' % value).hover().click()


@then(
    'установлен фильтр тип в состояние "{value}" (Ключи, Перчатки, Ножи, Пистолеты, Штурмовые винтовки, Снайперские винтовки, Пистолеты-пулеметы, Дробовики, Музыка, Пулеметы, Значки, Стикеры, Граффити, Кейсы)')
def step_impl(context, value):
    """Проверяет, что фильтр тип установлен в состояние {value}"""

    assert s('.filter_mobile_container .filter_exterior_type .list_menu_dropdown [title="%s"]' % value).get_attribute(
        'class') == 'type_item is_active', 'Фильтр тип не установлен'


@then('листинг товаров отфильтрован по фильтру качества"{value}"')
def step_impl(context, value):
    """Проверяет, что листинг товаров отсортирован по фильтру качества {value}"""
    sleep(3)
    selectors = ss('.items [cc="item"] .s_c .r')
    for selector in selectors:
        assert selector.text == value, 'листинг товаров не отфлильтрофан по филтру качества %s или нет предметов, которые подходяд под условие' % value


@when('установить фильтр цен от "{price1}" до "{price2}"')
def step_impl(context, price1, price2):
    """Устанавливает филтр цен от {price1} до {price2}"""
    s('.filter .price_inputs [input="max"]').hover().click().send_keys(Keys.CONTROL + "a").send_keys(Keys.BACK_SPACE)
    s('.filter .price_inputs [input="max"]').send_keys(price2)
    s('.filter .price_inputs [input="min"]').hover().click().send_keys(Keys.BACK_SPACE)
    s('.filter .price_inputs [input="min"]').send_keys(price1)


@then('установлен фильтр цен от "{price1}" до "{price2}"')
def step_impl(context, price1, price2):
    """Проверяет, что в листинге товаров диапазон цен от {price1} до {price2}"""
    selectors = ss('.items [cc="item"] .wrapper__price div')
    for selector in selectors:
        price = selector.text[2:]
        price = float(price)
        price1 = float(price1)
        price2 = float(price2)
        assert price1 < price < price2, 'Фильтр по цене работает не корректно %s' % price


@when('активировать чек бокс стикеры/стартрэк "{value}" (stickers/stattrack)')
def step_impl(context, value):
    """Активирует чек бокс стикеры/стартрэк зависит от {value}"""
    actions = ActionChains(browser.driver())
    actions.click(s('.filter_mobile_container .filter_checkbox_switch [name="%s"]' % value)).perform()


@then('в листинг предметов выведены товары со стикерами')
def step_impl(context):
    """Проверяет, что все товары в листинге имеют стикеры"""
    selectors_stickers = len(browser.driver().find_elements_by_css_selector('.items [cc="item"]  .s'))
    selectors_all_item = len(browser.driver().find_elements_by_css_selector('.items [cc="item"]'))
    assert selectors_stickers == selectors_all_item, 'Фильтр по стикерам отработал некорректно %s != %s' % (
        selectors_stickers, selectors_all_item)


@then('в листинге предметов выведены товары статтрэк')
def step_impl(context):
    """Проверяет, что все предметы стартрэк"""
    selectors_statTrack = len(browser.driver().find_elements_by_css_selector('.items [cc="item"] .st'))
    selectors_all_item = len(browser.driver().find_elements_by_css_selector('.items [cc="item"]'))
    assert selectors_all_item == selectors_statTrack, 'Фильтр по статтрэку отработал некорректно %s != %s' % (
        selectors_all_item, selectors_statTrack)
