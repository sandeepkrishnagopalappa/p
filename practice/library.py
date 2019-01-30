# Function Decorator for element editability
def _wait(original_function):
    def wrapper(*args, **kwargs):
        if original_function.__name__ == 'enter_text':
            wait_for_element_editable(args[0], **kwargs)
        elif original_function.__name__ == 'click_element':
            wait_for_element_clickable(*args, **kwargs)
        elif original_function.__name__ == 'select_item':
            wait_for_element_selectable(*args, **kwargs)
        elif original_function.__name__ == ('accept_alert' or 'dismiss_alert'):
            wait_for_alert(**kwargs)
        return original_function(*args, **kwargs)
    return wrapper


def wait_for_element_editable(webelement, timeout=60):
    print(f'waiting for element to be editable {webelement} for {timeout} seconds')


def wait_for_element_clickable(webelement, timeout=60):
    print(f'waiting for element to be clickable {webelement} for {timeout} seconds')


def wait_for_element_selectable(webelement, item, timeout=60):
    print(f'waiting for element to be selectable {item} for {timeout} seconds')


def wait_for_alert(timeout=60):
    print(f'waiting for alert to be present {timeout} seconds')


def wait_for_element_visibility(webelement, timeout=60):
    print('Waiting for visibility of element')


@_wait
def enter_text(webelement, value, timeout=60):
    print(f'Clicking on element in {timeout} seconds')


@_wait
def select_item(webelement, item, timeout=60):
    print(f'Selecting item in {timeout} seconds')


@_wait
def click_element(webelement, timeout=60):
    print(f'Click element in {timeout} seconds')


@_wait
def accept_alert(timeout=60):
    print(f'Accepting alert {timeout} seconds')


@_wait
def dismiss_alert(timeout=60):
    print(f'Dismissing Alert in {timeout} seconds')


click_element('login')



