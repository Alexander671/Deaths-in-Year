import os
import sys
import time
import pickle

import wikipediaapi

from email_sender import send_email

# from logging import basicConfig

from dotenv import load_dotenv
load_dotenv()
# переменная которая отвечает за отправку старых сообщений
# при первом запуске скрипта
SEND_OLD_UPDATES = os.getenv("SEND_OLD_UPDATES") == "True"

wiki_wiki = wikipediaapi.Wikipedia("TestDeathPage (matveevalex97@yandex.ru)",
                                   "en")


def check_person(deaths_links_new_check):
    """
    Проверяет каждую ссылку - "это действительно человек?"
    и отправляет электронное письмо, если это персона,
    которая умерла в 2023 году
    """
    for link_check in deaths_links_new_check:

        # получаем не весь текст
        page = wiki_wiki.page(link_check.split(',')[0])

        if page.exists and page.categories.get('Category:2023 deaths'):

            langlinks = page.langlinks

            if langlinks.get('ru'):
                page = langlinks['ru']

            send_email(page.summary.split('\n')[0] + '\n' + page.fullurl)


def safe_death_link(deaths_links_new):
    """
    Сохраняет новые ссылки на смерть в файл и проверяет изменения.
    """

    # создаем файл, если до этого не был создан
    from pathlib import Path

    filePath = Path("deaths_links.pickle")

    filePath.touch(exist_ok=True)

    # открываем файл для чтения, сохраняем полученный результат
    # в переменную deaths_links_old
    with open('deaths_links.pickle', 'rb') as links_file_read:

        try:

            deaths_links_old = pickle.load(links_file_read)

        except (OSError, IOError, EOFError) as e:

            print(e)
            deaths_links_old = None

        links_file_read.close()

    # октрываем для сохранения новых значений(если есть)
    with open('deaths_links.pickle', 'ab') as links_file_write:

        if not deaths_links_old:

            pickle.dump(deaths_links_new, links_file_write)

            deaths_links_old = deaths_links_new

            if SEND_OLD_UPDATES:

                check_person(deaths_links_new)

        elif deaths_links_old != deaths_links_new:

            print('Есть изменения: ', deaths_links_new - deaths_links_old)

            check_person(deaths_links_new - deaths_links_old)

            deaths_links_old.update(deaths_links_new)

            open('deaths_links.pickle', 'w').close()
            pickle.dump(deaths_links_old, links_file_write)

        else:

            print('Измнений нет')

        links_file_write.close()


def get_updates():
    """
    Получает обновления о смертях и вызывает функцию для сохранения
    и проверки изменений.
    """
    page_py = wiki_wiki.page('Deaths in 2023')

    safe_death_link(set(page_py.links))

    # Пауза между запросами
    time.sleep(10)  # Например, пауза в 10 секунд


if __name__ == "__main__":

    fpid = os.fork()

    if fpid != 0:

        # Running as daemon now. PID is fpid

        sys.exit(0)

    sys.stdin = open('/dev/null', 'r')
    sys.stdout = open('output.log', 'w')
    sys.stderr = open('error.log', 'w')

    while True:
        get_updates()
