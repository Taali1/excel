from pylatex import Document, Section, Subsection, Tabular, MiniPage, NoEscape, NewPage, Command
from pylatex.utils import bold
from get_data import get_xml, filter_xml

def create_pdf(products, title: str) -> None:
    doc = Document()

    for product in products:
        with doc.create(Section(f"Nazwa produktu: {product["name"]["text"]}")):
            with doc.create(MiniPage(width=NoEscape(r'0.5\textwidth'))):
                with doc.create(Tabular('|l|l|')) as table:
                    table.add_hline()
                    table.add_row((bold('Kod:'), product['attrs']['a'][1]['text']))
                    table.add_hline()
                    table.add_row((bold('Gramatura:'), 'gramatura'))
                    table.add_hline()
                    table.add_row((bold('Kolor:'), 'color'))
                    table.add_hline()
                    table.add_row((bold('Skład:'), 'composition'))
                    table.add_hline()
                    table.add_row((bold('Szerokość:'), 'width'))
                    table.add_hline()
                    table.add_row((bold('Wysokość:'), 'height'))
                    table.add_hline()

                doc.append(NoEscape(r'\vspace{0.5cm}'))

                with doc.create(Tabular('|l|l|')) as table:
                    table.add_hline()
                    table.add_row((bold('Cena netto:'), product['price']))
                    table.add_hline()
                    table.add_row((bold('Cena po rabacie netto:'), 'price after discount'))
                    table.add_hline()

            with doc.create(MiniPage(width=NoEscape(r'0.5\textwidth'))):
                doc.append(NoEscape(r'\centering'))
                doc.append(NoEscape(r'\includegraphics[width=\textwidth]{' + 'image_path' + '}'))

        doc.append(NewPage())

    # Generate the PDF
    doc.generate_pdf(title, clean_tex=False)
