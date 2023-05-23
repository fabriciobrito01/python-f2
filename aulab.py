import datetime as dt

data_hora = dt.datetime(2023, 2, 22, 12, 30, 31)
print(f'A data e hora é {data_hora}')

data_horaD = dt.datetime.now()
print(f'A data de hoje é {data_horaD.day}/{data_horaD.month}/{data_horaD.year}')
print(f'A hora atual é {data_horaD.hour}:{data_horaD.minute}:{data_horaD.second}')