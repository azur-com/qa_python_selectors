from selene import browser, have, by, be, query


def test_1_todo():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("#firstName").set_value("Alex")
    browser.element("#lastName").set_value("Gladov")
    browser.element("#userEmail").type('alex@gmail.com')
    browser.element("#userEmail").should(be.visible)
    #xl = browser.element('input[type="radio"][value="Female"]')
    browser.element('[name="gender"][value="Female"] + label').click()

    xl = browser.element('input')
    xl.click()
    elements = browser.all('label')
    for e in elements:
        print(e.get(query.text))
    #print(xl.get_attribute('value'))

    '''
    .element_by(have.value('Female')).
    browser.element('#hobbies-checkbox-2').with_(clickable=True)
    xl = browser.element('.custom-control-label').click()
    browser.element('[name=gender][value=Female]+label').click()
    browser.element("#gender-radio-2").type('a').press_enter()
    browser.element("#p").type('b').press_enter()
    browser.element("#p").type('c').press_enter()
    '''
    pass

def mult (a: int, b: int=6):
    print(a*b)

mult(10)

test_1_todo()




