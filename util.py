'''
Library for saving and loading lxml tree's from files or drivers.
Takes care of encoding and decoding to preserve unicode.
'''
import lxml.html


def create_page_from_file(fn):
    '''Creates an lxml document from a file.'''
    with open(fn) as f:
        return lxml.html.fromstring(f.read().decode('utf-8'))


def create_page(driver):
    '''Creates an lxml document from the driver's active window.'''
    page = lxml.html.fromstring(driver.page_source,
                                base_url=driver.current_url)
    return page


def create_page_from_element(element):
    '''Creates an lxml document from the element's html'''
    page = lxml.html.fromstring(element.html)
    return page


def save_page(page, filename):
    '''Saves an lxml document to a file.'''
    with open(filename, 'w') as f:
        f.write(lxml.html.tostring(page, encoding=unicode).encode('utf-8'))


def create_and_save_page(driver, filename):
    '''Creates and saves page to file. Returns page.'''
    page = create_page(driver)
    save_page(create_page(driver), filename)
    return page
