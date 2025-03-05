from datetime import date,timedelta
from itertools import count


def schedule(first_date:date,first_day_of_week:int,*days_of_week:int,total_days:int,format='%d/%m/%Y'):

    global vacations
    dates = list()
    dates.append(first_date)

    lessondays = list()
    lessondays.append(first_day_of_week)
    lessondays.extend(days_of_week)

    while len(dates)<total_days:
        for el in count(1):
            flag = False
            if ((dates[-1]+timedelta(el)).isoweekday() in lessondays):
                flag = True
                for vac in vacations:
                    if vac[0]<dates[-1]+timedelta(days=el)<(vac[0]+vac[1]):
                        flag = False
                        #print(f"{dates[-1] + timedelta(days=el)} in vacation")
                        break
            if flag:
                dates.append(dates[-1]+timedelta(el))
                break

    return [el.strftime(format) for el in dates]
#
# >>> vacations = [(date(2023, 5, 1), timedelta(weeks=1)),(date(2023, 7, 17), timedelta(weeks=1)),]
# >>> py321 = schedule(date(2023, 4, 1), 6, 7, total_days=70)
# >>> print(py321)
# ['01/04/2023', '02/04/2023', '08/04/2023', '09/04/2023', '15/04/2023', '16/04/2023', '22/04/2023', '23/04/2023', '29/04/2023', '30/04/2023', '13/05/2023', '14/05/2023', '20/05/2023', '21/05/2023', '27/05/2023', '28/05/2023', '03/06/2023', '04/06/2023', '10/06/2023', '11/06/2023', '17/06/2023', '18/06/2023', '24/06/2023', '25/06/2023', '01/07/2023', '02/07/2023', '08/07/2023', '09/07/2023', '15/07/2023', '16/07/2023', '29/07/2023', '30/07/2023', '05/08/2023', '06/08/2023', '12/08/2023', '13/08/2023', '19/08/2023', '20/08/2023', '26/08/2023', '27/08/2023', '02/09/2023', '03/09/2023', '09/09/2023', '10/09/2023', '16/09/2023', '17/09/2023', '23/09/2023', '24/09/2023', '30/09/2023', '01/10/2023', '07/10/2023', '08/10/2023', '14/10/2023', '15/10/2023', '21/10/2023', '22/10/2023', '28/10/2023', '29/10/2023', '04/11/2023', '05/11/2023', '11/11/2023', '12/11/2023', '18/11/2023', '19/11/2023', '25/11/2023', '26/11/2023', '02/12/2023', '03/12/2023', '09/12/2023', '10/12/2023']

