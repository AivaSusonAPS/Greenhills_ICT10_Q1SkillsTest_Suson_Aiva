# Computing for total using Arithemetic & strings
from pyscript import document, display


def create_order(e):
    document.getElementById('output').innerHTML = ' '

    drink1 = document.getElementById('item1')
    drink2 = document.getElementById('item2')
    drink3 = document.getElementById('item3')
    drink4 = document.getElementById('item4')

    subtotal = float(drink1.value) * drink1.checked
    subtotal = float(drink2.value) * drink2.checked
    subtotal = float(drink3.value) * drink3.checked
    subtotal = float(drink4.value) * drink4.checked
    display(subtotal, target="output")