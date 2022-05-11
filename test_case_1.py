import re
import mulch

def setup_function():
    input_values = [40, 8, 4, 'n', 25]
    mulch.input = lambda _: input_values.pop(0)

def test_cubic_yards(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('4 *cubic *yards', out)
    assert match, '4 cubic yards not found in output'
    assert err == ''

def test_mulch_cost(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Mulch:\s*\\$\s*144.00', out)
    assert match, 'Mulch: $ 144.00 not found in output'
    assert err == ''

def test_delivery_charge(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Delivery charge:\s*\\$\s*106.25', out)
    assert match, 'Delivery charge: $ 106.25 not found in output'
    assert err == ''

def test_sales_tax(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Sales tax:\s*\\$\s*10.08', out)
    assert match, 'Sales tax: $ 10.08 not found in output'
    assert err == ''

def test_total_cost(capsys):
    mulch.main()
    out, err = capsys.readouterr()

    match = re.search('Total cost:\s*\\$\s*260.33', out)
    assert match, 'Total cost: $ 260.33 not found in output'
    assert err == ''
