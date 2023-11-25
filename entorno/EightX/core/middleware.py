class AcortadorI18nMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Imprimir información de la solicitud
        path = request.path_info
        print(f"Solicitud: {path}")
        print(f"Idioma actual de la solicitud: {getattr(request, 'LANGUAGE_CODE', 'No disponible')}")
        print(f"Datos de la sesión: {request.session.items()}")
        print(f"Cookies: {request.COOKIES}")

        # Continuar con el procesamiento normal de la solicitud
        response = self.get_response(request)

        # Imprimir información de la respuesta
        print(f"Respuesta URL: {response['Location']}" if 'Location' in response else "Sin redirección")
        print(f"Idioma en la respuesta: {getattr(response, 'LANGUAGE_CODE', 'No disponible')}")
        print(f"Datos de la sesión después: {request.session.items()}")
        # Imprimir información de idioma desde la sesión, si está disponible
        idioma_sesion = request.session.get('_language', 'No definido en la sesión')
        print(f"Idioma en la sesión: {idioma_sesion}")


        return response