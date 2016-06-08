from bs4 import BeautifulSoup

def naive_extract_table_with_span(page):
    result = []
    soup = BeautifulSoup(page, "html.parser")

    for row in soup.findAll("tr"):
        for col in row.findAll("td"):
            data = col.find("span").getText()
            result.append(data)

        result.append("\n")

    return " | ".join(result)


if __name__ == '__main__':
    page = open("scrape_table_with_span.py.html")
    r = naive_extract_table_with_span(page.read())
    print (r)
