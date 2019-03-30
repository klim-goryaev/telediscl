from requests_html import HTMLSession
import timeit


URL = 'https://www.e-disclosure.ru/portal/company.aspx?id=321'

def req_html_test():
    session = HTMLSession()

    r = session.get(URL)
    r.html.render()

    #получение даты публикации новостей
    date_publication = r.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[2]/text()")
    
    #получение анкоров новостей
    anchors = r.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[3]/a/text()")
        
    #получение ссылок новостей
    links =  r.html.xpath("//div[@class='js-events-container']/table/tbody/tr/td[3]/a/@href")
    
    print(links)

    #вывод всего сразу
    printfile=('Дата публикации:', date_publication, 'Названия новостей:', anchors, 'Ссылки:', links)

    with open('export.txt', 'w', encoding='utf-8') as f:
        content = f.write(printfile)
        print(content)
    

req_html_test()