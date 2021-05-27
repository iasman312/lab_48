from datetime import datetime, timezone


from django.shortcuts import render


def stats_view(request):
    now = datetime.now(timezone.utc)
    time = now - request.user.last_login
    days, seconds = time.days, time.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    time = hours * 60 + minutes
    my_dic = request.session.get('my_dic', {})
    context = {'time': time, 'my_dic': my_dic}
    return render(request, 'statistics/statistics-view.html', context)
