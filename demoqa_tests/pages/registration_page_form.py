from selene import browser, have,
from demoqa_tests.path.resource import RESOURCES_PATH
from demoqa_tests.data.users import User

class RegistrationPage:


    def open(self):
        browser.open('/automation-practice-form')
        browser.all('#adplus-anchor').with_(timeout=3).wait_until(
            have.size_greater_than_or_equal(1)
        )
        browser.all('#adplus-anchor').perform(command.js.remove)


    def type_registration_user(self, user: User):
        browser.element('#firstName').click().type(user.first_name)
        browser.element('#lastName').click().type(user.last_name)
        browser.element('#userEmail').click().type(user.email)
        browser.element('[for=gender-radio-1]').click()
        browser.element('#userNumber').click().type(user.phone_number)
        browser.element('#dateOfBirthInput').click()

        

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
        

    def scroll_page(self):
        browser.element('.react-datepicker__year-select').type('1990')
        browser.element('.react-datepicker__month-select').type('November')
        browser.element(f'.react-datepicker__day--0{10}:not(.react-datepicker__day--outside-month)').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.element(f"label[for='hobbies-checkbox-{user.hobbies}']").click()
        browser.element('#uploadPicture').send_keys(RESOURCES_PATH + '\\' + f"{user.image}")
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        browser.element('#currentAddress').click().type(user.address)
        browser.element('#state #react-select-3-input').type(user.state).press_enter()
        browser.element('#city #react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def press_enter_by_confirm_registration(self, user: User):
        browser.all('tbody tr').should(have.exact_texts(
                f'Student Name {user.first_name} {user.last_name}',
                f'Student Email {user.email}',
                f'Gender {user.gender}',
                f'Mobile {user.phone_number}',
                f'Date of Birth {user.birthday}',
                f'Subjects {user.subjects}',
                f'Hobbies {user.hobby}',
                f'Picture {user.image}',
                f'Address {user.address}',
                f'State and City {user.state} {user.city}'
                ))
