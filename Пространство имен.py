def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_function() - вывод будет ошибкой, данная функция работает локально для test_function
test_function()