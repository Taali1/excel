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

        # Procesuje tylko dane które mają wszystkie wartości takie jak gramatura itp
        # if len(desc_data) + len(name_data) < 5:
        #     continue


        gross_price = float(product['price'])

        netto_price = round((gross_price*.8130081300813008), 2)
        netto_price_str = str(netto_price)

        off_price = round((netto_price*.75), 2)
        off_price_str = str(off_price)

        if len(off_price_str.split('.')[1]) == 1:
            off_price_str += '0'
        
        if len(netto_price_str.split('.')[1]) == 1:
            netto_price_str += '0'


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
                
                netto_price_str, 
                off_price_str
                )
        except Exception as error:
            print("An exception occurred:", error)
            continue
        count += 1
        # print("Product number "+str(count)+f" done\nIndex: {product['attrs']['a'][1]['text']}")

    html = generate_html(result_div, title)

    with open(f'OUTPUT/{title}.html', 'w', encoding='utf-8') as file:
        file.write(html)

    print("HTML file has been created with name: " + title + ".html")





