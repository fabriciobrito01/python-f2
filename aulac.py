import datetime as dt

mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Jullho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
hj = dt.datetime.today()

dataf = dt.datetime.strftime(hj, '%d de %{mes[0]} de %Y')

print(dataf)