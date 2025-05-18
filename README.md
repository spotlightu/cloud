# Содержимое
cloud.py — скрипт, содержащий функции обработки списка чисел: поиск чётных, максимум/минимум и сортировка пузырьком.

test_cloud.py — UI-тест с использованием библиотеки Playwright, проверяющий поведение сайта https://example.com.

# Требования
* Python 3.7 или выше
* Библиотеки:
  * playwright==1.32.0 (для test_cloud.py)
# Установка зависимостей
###### bash
    pip install playwright
    playwright install

# Запуск скрипта cloud.py

1) Запустите скрипт:
    ###### bash
        python cloud.py
2) Введите список чисел через запятую (например, 1, 2, 3, 4, 5).

3) Результаты будут выведены на экран.

# Запуск теста test_cloud.py

1) Запустите тест:
    ###### bash
        python test_cloud.py

2) Тест проверит работу веб-страницы example.com:

   * Откроет страницу https://example.com.
   * Проверит наличие "Example" в заголовке.
   * Кликнет на ссылку "More information".
   * Убедится, что произошёл переход на https://www.iana.org/help/example-domains.