def generate_html(data, title):
    base_start = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        
    '''

    base_middle = '''
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .product {
                display: flex;
                border: 1px solid #ccc;
                padding: 20px;
                margin: 20px 0;
            }
            .product img {
                width: auto;
                height: auto;
                max-width: 20em;
                max-height: 20em;
                margin-right: 20px;
            }
            .product-info {
                flex: 1;
                margin-left: 10em;
            }
            .product-info table {
                width: 60%;
                border-collapse: collapse;
            }
            .product-info th, .product-info td {
                padding: 5px;
                text-align: left;
            }
                
            .product-info table, .product-info th, .product-info td {
            border: 1px solid #000;
            }

            .product-info th {
                width: 150px;
            }
            .price {
                margin-top: 10px;
                width: 100%;
            }
            .price td {
                padding: 5px;
            }
        </style>
    </head>
    <body>
    '''


    base_end = '''
    </body>
    </html>
    '''
    return base_start + base_middle + data + base_end


def generate_div(img_link, name, index, gramatura, color, sklad, width, height, netto_price, discount_price):
    if width != '<i>Null</i>':
        width += ' cm'
    if height != '<i>Null</i>':
        height += ' cm'
    
    div_product = f'''
    <div class="product">
        <img src="{img_link}" alt="Product Image">
        <div class="product-info">
            <h2>{name}</h2>
            <table>
                <tr>
                    <th>Kod:</th>
                    <td>{index}</td>
                </tr>
                <tr>
                    <th>Gramatura:</th>
                    <td>{gramatura}</td>
                </tr>
                <tr>
                    <th>Kolor:</th>
                    <td>{color}</td>
                </tr>
                <tr>
                    <th>Skład:</th>
                    <td>{sklad}</td>
                </tr>
                <tr>
                    <th>Szerokość:</th>
                    <td>{width}</td>
                </tr>
                <tr>
                    <th>Wysokość:</th>
                    <td>{height}</td>
                </tr>
            </table>
            <div class="price">
                <table>
                    <tr>
                        <td>Cena netto:</td>
                        <td>{netto_price}</td>
                    </tr>
                    <tr>
                        <td>Cena po rabacie netto:</td>
                        <td>{discount_price}</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
    '''
    return div_product