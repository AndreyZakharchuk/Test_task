from behave import given
from selene import browser
from warnings import warn

CLICK_VIEW = '''
document.addEventListener('click',function (event) {
        var body = document.querySelector('body');
        var x = event.x;
        var y = event.y;

        var div = document.createElement('div');

        div.style.position = "fixed";
        div.style.left = x - 2.5 + "px";
        div.style.top = y - 2.5 + "px";
        div.style.width = "5px";
        div.style.height = "5px";
        div.style.background = "red";
        div.style.borderRadius = "50%";
        div.style.zIndex = "100000000000000000000000";

        body.appendChild(div);

        setTimeout(function () {
          div.remove();
        },300);
    });
'''


@given("выполнен скрипт отображения места клика")
def script_click_view(context):
    """Добавляет скрипт на страницу, который показывает место клика"""
    try:
        browser.driver().execute_script(CLICK_VIEW)
    except Exception:
        warn('Не удалось выполнить скрипт отображения места клика.', stacklevel=2)
