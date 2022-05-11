import re
import mulch

def setup_function():
    input_values = [50, 10, 4, 'y', 75, 20, 4, 'y', 15, 3, 4, 'n', 10]
    mulch.input = lambda _: input_values.pop(0)

def test_cubic_yards(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('26\s*cubic\s*yards', out)
    assert match, '26 cubic yards not found in output'
    assert err == ''

def test_mulch_cost(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Mulch:\s*\\$\s*825.00', out)
    assert match, 'Mulch: $ 825.00 not found in output'
    assert err == ''

def test_delivery_charge(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Delivery charge:\s*\\$\s*42.50', out)
    assert match, 'Delivery charge: $ 42.50 not found in output'
    assert err == ''

def test_sales_tax(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Sales tax:\s*\\$\s*57.75', out)
    assert match, 'Sales tax: $ 57.75 not found in output'
    assert err == ''

def test_total_cost(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Total cost:\s*\\$\s*925.25', out)
    assert match, 'Total cost: $ 925.25 not found in output'
    assert err == ''
