from bs4 import BeautifulSoup
import os.path

def get_html_file_arg():
    
    # get file path and validate file exists
    if len(sys.argv) >= 2:
        html_file = sys.argv[2]
        
        if os.path.isfile(html_file): 
            return html_file
    
    print("Invalid or no argument: requires a valid path as the first argument.")
    exit(-1)

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
    
    file = get_html_file_arg()
    
    with open(file) as page:
        r = naive_extract_table_with_span(page.read())
        print (r)
