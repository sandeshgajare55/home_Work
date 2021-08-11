class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Intialization")

    def __call__(self, request):
        print('Before View')
        response = self.get_response(request)
        print('After View')



        return response