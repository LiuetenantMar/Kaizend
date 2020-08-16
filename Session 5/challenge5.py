import requests

from IPython import embed

BASE_URL = "https://sample-target-bucket-with-html-pages.s3-ap-southeast-1.amazonaws.com/group2"

def extract_html_content(target_url):
    response = requests.get(target_url)
    return response.text

def main():
    target_page = BASE_URL + "/index.html"
    print(target_page)

    html_content = extract_html_content(target_page)

    print(html_content)

    embed()

        
if __name__ == "__main__":
    main()