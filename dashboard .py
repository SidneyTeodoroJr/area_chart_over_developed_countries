import plotly.graph_objs as go
import numpy as np

# Gerando dados aleatórios para 18 países
np.random.seed(42)
x_data = np.arange(2010, 2021)

# Dados fictícios para cada país
y1 = np.random.randint(1000, 3000, size=11)
y2 = np.random.randint(1200, 3500, size=11)
y3 = np.random.randint(1500, 4000, size=11)
y4 = np.random.randint(1800, 4500, size=11)
y5 = np.random.randint(2000, 5000, size=11)
y6 = np.random.randint(2200, 5500, size=11)
y7 = np.random.randint(2500, 6000, size=11)
y8 = np.random.randint(2800, 6500, size=11)
y9 = np.random.randint(3000, 7000, size=11)
y10 = np.random.randint(3200, 7500, size=11)
y11 = np.random.randint(3500, 8000, size=11)
y12 = np.random.randint(3800, 8500, size=11)
y13 = np.random.randint(4000, 9000, size=11)
y14 = np.random.randint(4200, 9500, size=11)
y15 = np.random.randint(4500, 10000, size=11)
y16 = np.random.randint(4800, 10500, size=11)
y17 = np.random.randint(5000, 11000, size=11)
y18 = np.random.randint(5500, 12000, size=11)

# Criando os gráficos de área para cada país
trace1 = go.Scatter(x=x_data, y=y1, mode='lines', fill='tozeroy', name='Estados Unidos')
trace2 = go.Scatter(x=x_data, y=y2, mode='lines', fill='tozeroy', name='Holanda')
trace3 = go.Scatter(x=x_data, y=y3, mode='lines', fill='tozeroy', name='Reino Unido')
trace4 = go.Scatter(x=x_data, y=y4, mode='lines', fill='tozeroy', name='Suíça')
trace5 = go.Scatter(x=x_data, y=y5, mode='lines', fill='tozeroy', name='Finlândia')
trace6 = go.Scatter(x=x_data, y=y6, mode='lines', fill='tozeroy', name='Canadá')
trace7 = go.Scatter(x=x_data, y=y7, mode='lines', fill='tozeroy', name='Nova Zelândia')
trace8 = go.Scatter(x=x_data, y=y8, mode='lines', fill='tozeroy', name='Suécia')
trace9 = go.Scatter(x=x_data, y=y9, mode='lines', fill='tozeroy', name='Austrália')
trace10 = go.Scatter(x=x_data, y=y10, mode='lines', fill='tozeroy', name='Japão')
trace11 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Bélgica')
trace12 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Áustria')
trace13 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='França')
trace14 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Luxemburgo')
trace15 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Alemanha')
trace16 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Irlanda')
trace17 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Dinamarca')
trace18 = go.Scatter(x=x_data, y=y11, mode='lines', fill='tozeroy', name='Noruega')

# Criando o layout do dashboard
layout = go.Layout(
    title='Dados fictícios do desenvolvimento de países desenvolvidos',
    xaxis=dict(title='Ano'),
    yaxis=dict(title='GDP'),
    hovermode='closest'
)

# Combinando os gráficos em um objeto Figure
fig = go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18], layout=layout)

# Exibindo o dashboard
fig.show()