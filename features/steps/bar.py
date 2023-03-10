from behave import given, when, then

@given(u'I navigate to the customer pages')
def nav(context):
    """ 
    Navigate to the type information page
    """
    context.browser.get('http://localhost:5000/Type_information')

@when(u'I click on the link to customer details')
def click(context):
    """ 
    Find the desired link
    """
    context.browser.find_element_by_partial_link_text('2').click()

@then(u'I should see the order for that customer')
def details(context):
    """ 
    if successful, then we should be directed to the size information page
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/Size_information'
    assert '01595 Amanda Loaf' in context.browser.page_source