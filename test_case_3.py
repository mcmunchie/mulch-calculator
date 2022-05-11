import re
import mulch

def setup_function():
    input_values = [20, 3, 3, 'y', 10, 3, 3, 'n', 29]
    mulch.input = lambda _: input_values.pop(0)

def test_cubic_yards(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('3 *cubic *yards', out)
    assert match, '3 cubic yards not found in output'
    assert err == ''

def test_mulch_cost(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Mulch:\s*\\$\s*108.00', out)
    assert match, 'Mulch: $ 108.00 not found in output'
    assert err == ''

def test_delivery_charge(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Delivery charge:\s*\\$\s*123.25', out)
    assert match, 'Delivery charge: $ 123.25 not found in output'
    assert err == ''

def test_sales_tax(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Sales tax:\s*\\$\s*7.56', out)
    assert match, 'Sales tax: $ 7.56 not found in output'
    assert err == ''

def test_total_cost(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Total cost:\s*\\$\s*238.81', out)
    assert match, 'Total cost: $ 238.81 not found in output'
    assert err == ''
