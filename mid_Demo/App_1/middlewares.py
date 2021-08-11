def my_mid(get_response):
    print('One time initialization')
    def my_fun(request):
        print('Before View')
        res=get_response(request)
        print('After view')
        return res
    return my_fun