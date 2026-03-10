from bs4 import BeautifulSoup

def extract_elements(html, tag):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all(tag)

    extracted = []

    for el in elements:
        data = {
            "tag": el.name,
            "id": el.get("id", ""),
            "class": " ".join(el.get("class", [])) if el.get("class") else "",
            "text": el.text.strip()
        }
        extracted.append(data)

    return extracted