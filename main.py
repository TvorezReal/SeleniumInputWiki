from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def navigate_wikipedia():
    browser = webdriver.Chrome()
    browser.get('https://ru.wikipedia.org')

    search_query = input("Введите ваш запрос для Википедии: ")
    search_box = browser.find_element(By.ID, 'searchInput')
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    while True:
        print("\nТекущая статья: ", browser.title)
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        links = browser.find_elements(By.CSS_SELECTOR, 'p a')

        print("Выберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Ваш выбор (1, 2, или 3): ")

        if choice == '1':
            for index, paragraph in enumerate(paragraphs):
                print(f"Параграф {index + 1}: {paragraph.text}")
                if input("Нажмите Enter для продолжения, 'q' для выхода: ") == 'q':
                    break
        elif choice == '2':
            for index, link in enumerate(links):
                print(f"{index + 1}: {link.get_attribute('href')} - {link.text}")
            link_choice = int(input("Выберите страницу для перехода (номер): ")) - 1
            links[link_choice].click()
            time.sleep(2)
        elif choice == '3':
            break
        else:
            print("Неизвестная команда, попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    navigate_wikipedia()