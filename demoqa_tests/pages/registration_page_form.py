import os.path
from selene import browser, have, command
from demoqa_tests.path.resource import RESOURCES_PATH


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('#adplus-anchor').with_(timeout=3).wait_until(
            have.size_greater_than_or_equal(1)
        )
        browser.all('#adplus-anchor').perform(command.js.remove)


    def type_first_name(self, f_name):
        browser.element('#firstName').click().type(f_name)

    def type_last_name(self, l_name):
        browser.element('#lastName').click().type(l_name)

    def type_user_email(self, email):
        browser.element('#userEmail').click().type(email)

    def select_user_gender(self, gender):
        pass
        if gender == 'Male':
            browser.element('[for=gender-radio-1]').click()
        elif gender == 'Female':
            browser.element('[for=gender-radio-2]').click()
        elif gender == 'Other':
            browser.element('[for=gender-radio-3]').click()
        else:
            raise ValueError('Invalid gender value')

    def type_user_phone_number(self, number):
        browser.element('#userNumber').click().type(number)

    def click_input_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def type_subjects(self, *subjects):
        subjects_input = browser.element('#subjectsInput')
        for subject in subjects:
            subjects_input.type(subject).press_enter()

    def select_hobbies(self, *hobbies):
        sport = 'hobbies-checkbox-1'
        reading = 'hobbies-checkbox-2'
        music = 'hobbies-checkbox-3'

        for hobby in hobbies:
            if hobby == 'sport':
                checkbox = browser.element(f'[for={sport}]')
            elif hobby == 'reading':
                checkbox = browser.element(f'[for={reading}]')
            elif hobby == 'music':
                checkbox = browser.element(f'[for={music}]')
            else:
                continue

            checkbox.click()


    def chose_file_pafh(self, name):
        browser.element('#uploadPicture').send_keys(RESOURCES_PATH + '\\' + f"{name}")

    def scroll_page(self):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    def type_current_adress(self, adress):
        browser.element('#currentAddress').click().type(adress)

    def type_state_and_press_enter(self, state):
        browser.element('#state #react-select-3-input').type(state).press_enter()

    def type_city_and_press_enter(self, city):
        browser.element('#city #react-select-4-input').type(city).press_enter()
    @property
    def press_enter_by_confirm_registration(self):
        return browser.element('#submit').press_enter()

    def assert_user_info(self, *args):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        browser.all('tbody tr').should(have.exact_texts(*args))
