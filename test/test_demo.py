from demoqa_tests.pages.registration_page_form import RegistrationPage


def test_form_demo():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.type_first_name('Alexander')
    registration_page.type_last_name('Pupkin')

    registration_page.type_user_email('Pupkin@gmail.com')
    registration_page.select_user_gender('Female')
    registration_page.type_user_phone_number('79067777777')
    registration_page.click_input_birthday('1990', 'November', '10')

    registration_page.type_subjects('Computer Science', 'English')
    registration_page.select_hobbies('sport')
    registration_page.chose_file_pafh('pocita.jpg')

    registration_page.type_current_adress('914751, Оренбургская область, город Волоколамск, проезд Сталина, 09')
    registration_page.type_state_and_press_enter('Haryana')
    registration_page.type_city_and_press_enter('Karnal')

    registration_page.press_enter_by_confirm_registration
    registration_page.assert_user_info(
                        'Student Name Alexander Pupkin',
                        'Student Email Pupkin@gmail.com',
                        'Gender Female',
                        'Mobile 7906777777',
                        'Date of Birth 10 November,1990',
                        'Subjects Computer Science,' ' English',
                        'Hobbies Sports',
                        'Picture pocita.jpg',
                        'Address 914751, Оренбургская область, город Волоколамск, проезд Сталина, 09',
                        'State and City Haryana Karnal'
                       )
