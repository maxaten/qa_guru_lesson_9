from demoqa_tests.pages.registration_page_form import RegistrationPage
from demoqa_tests.data.users import user_1


def test_form_demo():
    registration_page = RegistrationPage()

    # open browser
    registration_page.open()

    # filling in user fields
    registration_page.type_registration_user(user_1)

    # registration user
    registration_page.press_enter_by_confirm_registration(user_1)
