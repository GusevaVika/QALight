def time_date(time):
    days = time//(3600*24)
    hours = (time - (days*3600*24))//3600
    minutes = (time - days*3600*24 - hours*3600)//60
    sec = time - days*3600*24 - hours*3600 - minutes*60
    print('Days:' + str(days) + ' and hours:' + str(hours) + ' and minutes:' + str(minutes) + ' and seconds:' + str(sec))

time = int(input())
time_date(time)


