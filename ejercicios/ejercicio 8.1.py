#%%
import datetime

def vida_en_segundos(fecha_nac):
    hoy=datetime.date.today()
    nacimiento=datetime.datetime.strptime(fecha_nac,'%d/%m/%Y')
    t1=datetime.date(year= hoy.year,month=hoy.month,day=hoy.day)
    t2=datetime.date(year=nacimiento.year,month=nacimiento.month,day=nacimiento.day)
    t3= t1-t2
    return(t3.total_seconds())

fecha_nac=("23/11/1959")
# %%
