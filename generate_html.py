from template import generate_div, generate_html
from get_data import separate_desc

def exists(data, value):
    if data[value]:
        return data[value]
    return '.'

def create_page(products: dict, title: str) -> str:
    result_div = ''
    count = 0
    for product in products:
        desc_data, name_data = separate_desc(product['desc']['text'], product['name']['text'])

        # if len(desc_data) + len(name_data) < 5:
        #     continue

        try: 
            result_div += generate_div(
                product['imgs']['main']['url'], 
                product['name']['text'], 
                product['attrs']['a'][1]['text'], 
                desc_data.get('gramatura') or '<i>Null</i>',
                desc_data.get('color') or '<i>Null</i>', 
                desc_data.get('sklad') or '<i>Null</i>', 
                name_data.get('width') or '<i>Null</i>',
                name_data.get('height') or '<i>Null</i>', 
                product['price'], 
                product['price']
                )
        except Exception as error:
            print("An exception occurred:", error)
            continue
        count += 1
        # print("Product number "+str(count)+f" done\nIndex: {product['attrs']['a'][1]['text']}")

    html = generate_html(result_div, title)

    with open(f'{title}.html', 'w', encoding='utf-8') as file:
        file.write(html)

    print("HTML file has been created with name: " + title + ".html")





