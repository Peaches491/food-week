from django.http import HttpResponseRedirect


class AjaxRedirect(object):

    @staticmethod
    def process_response(request, response):
        if request.is_ajax():
            if type(response) == HttpResponseRedirect:
                response.status_code = 278
        return response