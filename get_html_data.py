from requests_html import HTMLSession


URL = 'https://www.e-disclosure.ru/portal/company.aspx?id=321'


def fetch_html():
    session = HTMLSession()
    r = session.get(URL)
    r.html.render()
    return r


def get_elements():
    data = fetch_html()
    links = data.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[3]/a/@href")
    text = data.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[3]/a/text()")
    date = data.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[2]/text()")
    date = [item.replace("\xa0", " ") for item in date]

    d = {k:[i, j] for i,j,k in zip(date, text, links)} 

    for k,v in d.items():
        print("{} {} {}".format(k, v[0], v[1]))

    return d

get_elements()