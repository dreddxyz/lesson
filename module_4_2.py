def test_funciton():
    def inner_function():
        print("Я в области видимости test_function")
    inner_function()

test_funciton()
inner_function() # выдаст ошибку NameError: name 'inner_function' is not defined, т.к. inner_function объявлен внутри другой функции