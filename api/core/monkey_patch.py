from rest_framework.response import Response


#########################       rest framework          #########################
def init(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None,
         message=None):
    """
    重写方法,包装data
    """
    super(Response, self).__init__(None, status=status)

    self.data = {
        "data": data,
        "msg": message if message else "",
        "result": True if status == 200 or not status else False,
        "code": status or 200
    }
    self.template_name = template_name
    self.exception = exception
    self.content_type = content_type

    if headers:
        for name, value in headers.items():
            self[name] = value


setattr(Response, '__init__', init)
