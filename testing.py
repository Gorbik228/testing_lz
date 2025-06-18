import pytest
import function as f

# тестируемая часть приложения
def test_pos_int_difff():
    assert f.func(2, 1, 2, 1) == 1

def test_integer_negative_numbers():
    assert f.func(2, -1, 2, -1) == 0.5774

def test_zero():
    with pytest.raises(ZeroDivisionError) as er:
        assert f.func(2,2,2,2) in str(er.value)

def test_positive_numbers():
    assert f.func(0.2, -0.1, 0.2, -0.1) == 1.8257

def test_negative_root():
    assert f.func(-2, 1, 1, 1) == "can't divide zero without complex"

def test_error_input():
    assert f.func('asdff', 0,0,0) == 'this is not a number'
    assert f.func('', 0,0,0) ==  'this is not a number'
    assert f.func('10**-9', 0,0,0) == 'this is not a number'


#Проверял  для начала деление на ноль для этого c, d должны принимать одинаковые значения.Программа должна вывести "Деление на ноль невозможно"(2,2,2,2)
#Дальше возьмем под корнем отрицательное число. Программа должна вывести "Невозможно извлечь конень из отрицательного числа"(-2,1,1,1)
#Далее введем в программу не числа. Программа должна вывести "Введенные вами значения не являются число"(asdff,0,0,0)
#Рабочее выполнение программы. Программа должна вывести "0.5774"(2, -1, 2, -1)
#Выволнение с дробными числами.Программа должна вывести "1.8257"(0.2, -0.1, 0.2, -0.1)