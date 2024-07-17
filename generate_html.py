from template import generate_div, generate_html

def create_page(products: dict, title: str) -> str:
    result_div = ''
    count = 0
    for product in products:
        try: 
            result_div += generate_div(
                product['imgs']['main']['url'], 
                product['name']['text'], 
                product['attrs']['a'][1]['text'], 
                'gramatura', 
                'color', 
                'sklad', 
                'width',
                'height', 
                product['price'], 
                product['price']
                )
        except:
            print("error in adding product")
            continue
        count += 1
        print("Product number "+str(count)+" done")

    html = generate_html(result_div)

    with open(f'{title}.html', 'w', encoding='utf-8') as file:
        file.write(html)

    print("HTML file has been created with name: " + title + ".html")





