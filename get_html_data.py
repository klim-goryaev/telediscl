from requests_html import HTMLSession
import timeit


URL = 'https://www.e-disclosure.ru/portal/company.aspx?id=321'

def req_html_test():
    session = HTMLSession()

    r = session.get(URL)
    r.html.render()

    res = r.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[3]/a/text()")
    
    print(res)

req_html_test()