from bs4 import BeautifulSoup
from IPython import embed

def generate_html():
    return """
        <html>
            <head></head>
            <body>
                <div href="/a.html">A</div>
                <div href="/b.html">B</div>
                <div href="/c.html">C</div>
                <div href="/d.html">D</div>
                
                <script>
                    var hello ="yah";
                    alert(hello);
                </script>
            </body>
        </html>
    """


def main():
    html_doc = generate_html()
    embed()
    # soup = BeautifulSoup(html_doc, 'html.parser')
    # div_elements = soup.find_all("div")

    # for div_element in div_elements:
    #     print(div_element.get_text())   

        
if __name__ == "__main__":
    main()