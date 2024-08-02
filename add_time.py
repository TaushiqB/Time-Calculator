def add_time(start, duration,  day = 0):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    am_pm = start.split()[1]
    time = start.split()[0]
    hour = time.split(':')[0]
    min = time.split(':')[1]
    add_hour = duration.split(':')[0]    
    add_min = duration.split(':')[1]
    final_hour = int(hour)+int(add_hour)
    final_min = int(min)+int(add_min)
    rem_hour = 0
    new_am_pm = am_pm
    n = 0
    d = ''
    if final_hour>12:
        n+=final_hour//24
        rem_hour = final_hour//12
        final_hour%=12
        if rem_hour%2!=0:
            if am_pm == 'AM':
                new_am_pm = 'PM'
            else:
                new_am_pm = 'AM'
                n+=1
            
            
        
    if final_min>60:
        rem_min = final_min//60
        final_min%=60
        final_hour+=rem_min
        rem_hour+=rem_min
        if final_hour>12:
            rem_hour = final_hour//12
            final_hour%=12
            if rem_hour%2!=0:
                if new_am_pm == 'AM':
                    new_am_pm = 'PM'

                else:
                    new_am_pm = 'AM'
                    n+=1
        # if rem_min%2!=0:
        #     if new_am_pm == 'AM':
        #         new_am_pm = 'PM'
        #     else:
        #         new_am_pm = 'AM'
    if final_hour==12:
        if new_am_pm == 'AM':
            new_am_pm = 'PM'
            
        else:
            new_am_pm = 'AM'
            n+=1    
                    
    #print(n)  
    if day == 0:
        if n>0:
            if n == 1:
                new_time = str(final_hour)+':'+str(final_min).rjust(2,'0')+' '+new_am_pm + " (next day)"
                return new_time
                    
            else:
                new_time = str(final_hour)+':'+str(final_min).rjust(2,'0')+' '+new_am_pm + " ("+str(n)+" days later)"
                return new_time
    elif day!=0:
        # print(day)
        # print(days)
        i = 0
        for i in range(len(days)):
            if day.lower() == days[i].lower():
                d = days[i]
                # print(d)
                # print(days[i])
                # print(i)
                break
        if n == 0:
            new_time = str(final_hour)+':'+str(final_min).rjust(2,'0')+' '+new_am_pm+', '+d
            return new_time
        if n == 1:
            new_time = str(final_hour)+':'+str(final_min).rjust(2,'0')+' '+new_am_pm+', '+days[i+1]+' (next day)'
            return new_time            
        else:
            # print(i)
            new_time = str(final_hour)+':'+str(final_min).rjust(2,'0')+' '+new_am_pm+', '+days[i+(n%7)]+ " ("+str(n)+" days later)"
            return new_time
        
       

    new_time = str(final_hour)+':'+str(final_min).rjust(2,'0')+' '+new_am_pm
    return new_time


print(add_time('8:16 PM', '466:02', 'tuesday'))
