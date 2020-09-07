import time

def test_guest_should_see_buy_button(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element_by_class_name("btn-add-to-basket")
