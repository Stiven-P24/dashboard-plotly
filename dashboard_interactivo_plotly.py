import pandas as pd
import plotly.express as px
import panel as pn

pn.extension('plotly')

# Cargar datos
df = pd.read_csv(
    "C:/Users/stive/OneDrive/Documents/Ing_Sistemas/Analisis de Datos/Analisis-de-datos-masivos-main/Proyecto Final/DELITOS_INFORM_TICOS_FECHA_UNIFICADA.csv",
    encoding="cp1252",
    sep=";"
)
df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce', dayfirst=True)
df['AÑO'] = df['FECHA'].dt.year
df['MES'] = df['FECHA'].dt.month

# Opciones para filtros
anios = sorted(df['AÑO'].dropna().unique().astype(int))
departamentos = sorted(df['DEPARTAMENTO'].dropna().unique())
conductas = sorted(df['DESCRIPCION CONDUCTA'].dropna().unique())

anio_selector = pn.widgets.MultiChoice(name='Año', options=anios, value=[])
departamento_selector = pn.widgets.MultiChoice(name='Departamento', options=departamentos, value=[])
conducta_selector = pn.widgets.MultiChoice(name='Conducta Delictiva', options=conductas, value=[])
conducta_selector_especifica = pn.widgets.Select(name="Conducta a analizar (Gráfico 5)", options=conductas)

# Función para filtrar dataframe según selecciones
def filtrar_df(anios, departamentos, conductas):
    d = df.copy()
    if anios:
        d = d[d['AÑO'].isin(anios)]
    if departamentos:
        d = d[d['DEPARTAMENTO'].isin(departamentos)]
    if conductas:
        d = d[d['DESCRIPCION CONDUCTA'].isin(conductas)]
    return d

# Gráficos dependientes de filtros
@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico1(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    data = d.groupby('AÑO').size().reset_index(name='Delitos')
    fig = px.line(data, x='AÑO', y='Delitos', title='Evolución Anual de Delitos')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico2(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    top = d['MUNICIPIO'].value_counts().head(10).reset_index()
    top.columns = ['Municipio', 'Delitos']
    fig = px.bar(top.sort_values('Delitos'), x='Delitos', y='Municipio', orientation='h', title='Top 10 Municipios')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico3(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    tabla = d.pivot_table(index='MES', columns='AÑO', values='CANTIDAD', aggfunc='sum', fill_value=0).reset_index().melt(id_vars='MES')
    fig = px.density_heatmap(tabla, x='AÑO', y='MES', z='value', color_continuous_scale='Viridis', title='Delitos por Mes y Año')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico4(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    comunes = d['DESCRIPCION CONDUCTA'].value_counts().head(10).reset_index()
    comunes.columns = ['Conducta', 'Cantidad']
    fig = px.bar(comunes.sort_values('Cantidad'), x='Cantidad', y='Conducta', orientation='h', title='Delitos más comunes')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector, conducta_selector_especifica)
def grafico5(anios, departamentos, conductas, conducta_especifica):
    d = filtrar_df(anios, departamentos, conductas)
    d = d[d['DESCRIPCION CONDUCTA'] == conducta_especifica]
    data = d.groupby('AÑO').size().reset_index(name='Casos')
    fig = px.line(data, x='AÑO', y='Casos', title=f'Evolución de \"{conducta_especifica}\"')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico6(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    data = d.groupby(['AÑO', 'MUNICIPIO']).size().reset_index(name='Casos')
    top = data.groupby('MUNICIPIO')['Casos'].sum().nlargest(5).index
    data = data[data['MUNICIPIO'].isin(top)]
    fig = px.line(data, x='AÑO', y='Casos', color='MUNICIPIO', title='Crecimiento de delitos por municipio')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico7(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    data = d.groupby('AÑO').size().reset_index(name='Total')
    fig = px.bar(data, x='AÑO', y='Total', title='Total de delitos por Año')
    return fig

@pn.depends(anio_selector, departamento_selector, conducta_selector)
def grafico8(anios, departamentos, conductas):
    d = filtrar_df(anios, departamentos, conductas)
    data = d.groupby(['MUNICIPIO', 'DESCRIPCION CONDUCTA']).size().reset_index(name='Total')
    pivot = data.pivot(index='MUNICIPIO', columns='DESCRIPCION CONDUCTA', values='Total').fillna(0)
    pivot = pivot.loc[pivot.sum(axis=1).nlargest(10).index]
    fig = px.imshow(pivot, aspect='auto', title='Delitos por Municipio y Conducta')
    return fig

# Crear plantilla BootstrapTemplate
template = pn.template.BootstrapTemplate(title="Dashboard Interactivo de Delitos Informáticos")

# Barra lateral con filtros
sidebar = pn.Column(
    "# Filtros",
    anio_selector,
    departamento_selector,
    conducta_selector,
    conducta_selector_especifica,
    sizing_mode='stretch_width',
    css_classes=['p-3']  # padding Bootstrap
)

# Área principal con gráficos organizados
content = pn.Column(
    pn.Row(pn.Column(grafico1, sizing_mode='stretch_width'), pn.Column(grafico2, sizing_mode='stretch_width')),
    pn.Row(pn.Column(grafico3, sizing_mode='stretch_width'), pn.Column(grafico4, sizing_mode='stretch_width')),
    pn.Row(pn.Column(grafico5, sizing_mode='stretch_width'), pn.Column(grafico6, sizing_mode='stretch_width')),
    pn.Row(pn.Column(grafico7, sizing_mode='stretch_width'), pn.Column(grafico8, sizing_mode='stretch_width')),
    sizing_mode='stretch_width',
    css_classes=['p-3']
)

# Añadir filtros y contenido al template
template.sidebar.append(sidebar)
template.main.append(content)

# Mostrar dashboard
template.show()
