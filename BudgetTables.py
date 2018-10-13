from pylatex import Document, Tabular, Command
from pylatex.utils import italic
from pylatex.utils import bold
from pylatex.basic import TextColor
from pylatex.package import Package

#modify these four variables below
items = ['Money to Dad', 'September Paycheck', 'Birthday Money', 'Food Budget (month)']
prices = [-250, 460, 230, -80]
bank = 1300
chosenColor = 'yellow'

#leave these variables alone
net = bank - sum(prices)
lightcolor = chosenColor + '!3'
color = chosenColor + '!10'
darkcolor = chosenColor + '!16'

def genenerate_table():
    geometry_options = {
        "margin": "2cm",
        "includeheadfoot": True
    }
    
    doc = Document(page_numbers=False, font_size = 'large', geometry_options=geometry_options)
    doc.generate_pdf(clean_tex=False,compiler='pdflatex')
    # Generate data table
    with doc.create(Tabular('l l')) as table:
                table.add_hline()
                table.add_hline()
                table.add_row(italic("Item"), italic("Price"), color=color)
                table.add_hline()
                for i in range(len(items)):
                    table.add_row(items[i], "$" + str(prices[i]), color=lightcolor)
                table.add_hline()
                table.add_row("Bank Account", "$" + str(bank), color=color)
                table.add_row("Subtotal","$" + str(sum(prices)), color=color)
                table.add_hline()
                if net < 0:
                    table.add_row("Net Total",TextColor("red", bold("$" + str(net))), color=darkcolor)
                else:
                    table.add_row("Net Total",bold("$" + str(net)), color=darkcolor)
                
                table.add_hline()
                table.add_hline()

    doc.generate_pdf("BudgetTable", clean_tex=False)

genenerate_table()

# -p4 0 0 0 0 BudgetTable.pdf -o NewBudgetTable.pdf

#run this in terminal to crop
