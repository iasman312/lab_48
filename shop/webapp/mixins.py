from django.views import View


class HitsMixin():
    def dispatch(self, request, *args, **kwargs):
        try:
            my_dic = request.session.get('my_dic', {})
            my_dic['hits'] = my_dic['hits'] + 1
            request.session['my_dic'] = my_dic
        except KeyError:
            my_dic = request.session.get('my_dic', {})
            my_dic['hits'] = 1
            request.session['my_dic'] = my_dic
        return super(HitsMixin, self).dispatch(request, *args, **kwargs)