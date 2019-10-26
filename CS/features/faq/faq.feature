Feature: Страница FAQ
  Тут следует описывать сценарии для взаимодействия со страницей FAQ

  Scenario: Проверка открытия/закрытия слайдеров на странице faq
    Given открыта страница сайта "https://cs.money/faq/ru/"
    Given открыто "2" слайдера на странице faq
    When закрыть все открытые слайдеры на странице faq
    Then закрыты все слайдеры на странице faq
    When открыть все слайдеры на странице faq
    Then открыты все слайдеры на странице faq
    When закрыть все открытые слайдеры на странице faq
    Then закрыты все слайдеры на странице faq

  Scenario Outline: Проверка доступности внутренних ссылок в футере
    Given открыта страница сайта "https://cs.money/faq/ru/"
    When нажата ссылка с текстом "<url_text>"
    Then открыта последняя вкладка в браузере
    Then на странице есть текст "<page_text>"
    Examples:
      | url_text              | page_text                              |
      | Условия использования | УСЛОВИЯ ИСПОЛЬЗОВАНИЯ СЕРВИСА CS.MONEY |
      | Bug bounty            | Bug bounty program                     |
      | Политика приватности  | Privacy Policy                         |
      | Сookie policy         | ПОЛИТИКА В ОТНОШЕНИИ ФАЙЛОВ COOKIE     |
      | Вакансии              | Открытые вакансии                      |

  Scenario Outline: Проверка доступности внешних ссылок в футере
    Given открыта страница сайта "https://cs.money/faq/ru/"
    Then ссылка '<URL>' равна внешней ссылке в футере '<URL2>'
    Examples:
      | URL                                            | URL2 |
      | https://steamcommunity.com/groups/csmoneytrade | 0    |
      | https://twitter.com/csmoneytrade               | 1    |
      | https://www.instagram.com/csmoneytrade/        | 2    |
      | https://vk.com/csmoneytrade                    | 3    |
      | https://discord.gg/vmUuupq                     | 4    |
      | https://facebook.com/csmoneytrade/             | 5    |