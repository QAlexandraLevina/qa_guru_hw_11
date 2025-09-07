import allure
from selene.support.shared import browser
from pages.registration_page import RegistrationPage
from test_qa_guru_hw_11.demoqa.users import UserData


@allure.title("Успешное заполнение формы")
def test_filled_form():
    """Инициализация экземпляров класса RegistrationPage и UserData"""
    alexandra = UserData(
        "Alexandra",
        "Levina",
        "alexandralevina1@gmail.com",
        "Female",
        "8912345678",
        ("February", "2002", "17"),
        "Computer Science",
        ("Sports", "Reading", "Music"),
        "test_file.txt",
        "Россия, г.Москва, ул.Маршала Жукова 1",
        ("Uttar Pradesh", "Lucknow"),
    )
    registration_page = RegistrationPage()

    with allure.step("Открытие формы регистрации"):
        browser.open("https://demoqa.com/automation-practice-form")

    with allure.step("Заполнение формы"):
        browser.execute_script("window.scrollBy(0, 500)")
        registration_page.registration_user(alexandra)

    with allure.step("Закрытие модального окна"):
        registration_page.close_button()

    with allure.step("Проверка заполненной формы"):
        registration_page.should_registered_user_with(alexandra)