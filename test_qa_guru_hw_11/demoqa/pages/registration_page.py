import os
from selene import browser, have, by
from test_qa_guru_hw_11.demoqa.users import UserData


class RegistrationPage:
    def __init__(self):
        self.user_first_name = browser.element("#firstName")
        self.user_last_name = browser.element("#lastName")
        self.user_email = browser.element("#userEmail")
        self.user_gender = browser.element("#genterWrapper")
        self.user_mobile = browser.element("#userNumber")
        self.user_date_of_birth = browser.element("#dateOfBirthInput")
        self.user_month_of_birth = browser.all(".react-datepicker__month-select option")
        self.user_year_of_birth = browser.all(".react-datepicker__year-select option")
        self.user_day_of_birth = browser.all(
            ".react-datepicker__day:not(.react-datepicker__day--outside-month)"
        )
        self.user_subject = browser.element("#subjectsInput")
        self.user_hobbies = browser.element("#hobbiesWrapper")
        self.user_picture = browser.element("#uploadPicture")
        self.user_address = browser.element("#currentAddress")
        self.user_state = browser.element("#state input")
        self.user_city = browser.element("#city input")
        self.submit_button = browser.element("#submit")
        self.close_button = browser.element("#closeLargeModal")
        self.registered_user_data = browser.all("tbody tr td:nth-child(2)")

    """Заполнение поля Date of Birth"""

    def fill_date_of_birth(self, month, year, day):
        self.user_date_of_birth.click()
        self.user_month_of_birth.element_by(have.exact_text(month)).click()
        self.user_year_of_birth.element_by(have.exact_text(year)).click()
        self.user_day_of_birth.element_by(have.exact_text(day)).click()
        return self

    """Выбор чек-бокса Hobbies"""

    def set_hobbies(self, tuple_hobbies):
        for h in tuple_hobbies:
            self.user_hobbies.element(by.text(h)).click()
        return self

    """Выбор State and City"""

    def set_state_city(self, tuple_state_city):
        state, city = tuple_state_city
        self.user_state.type(state).press_enter()
        self.user_city.type(city).press_enter()
        return self

    """Проверка заполненной формы"""

    def should_registered_user_with(self, user: UserData):
        self.registered_user_data.should(
            have.exact_texts(
                user.full_name,
                user.email,
                user.gender,
                user.mobile,
                user.date_of_birth,
                user.subject,
                user.hobby,
                user.picture,
                user.address,
                user.state_n_city,
            )
        )
        return self

    """Заполнение полей для регистрации"""

    def registration_user(self, user: UserData):
        self.user_first_name.type(user.first_name)
        self.user_last_name.type(user.last_name)
        self.user_email.type(user.email)
        self.user_gender.element(by.text(user.gender)).click()
        self.user_mobile.type(user.mobile)
        self.fill_date_of_birth(*user.birthday)
        self.user_subject.type(user.subject).press_enter()
        self.set_hobbies(user.hobbies)
        self.user_picture.send_keys(
            os.path.join(os.path.dirname(__file__), "test_file.txt")
        )
        self.user_address.type(user.address)
        self.set_state_city(user.state_city)
        self.submit_button.click()