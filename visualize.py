# -*- coding: utf-8 -*-
from sizes import Anecoop
import plotly.graph_objects as go
import pandas as pd  
if __name__ == "__main__":  
  #df = pd.read_csv('measurements.csv')
  #px.scatter(df, x='diameter', y='diameter')
  datos = Anecoop('measurements.csv', "ESP")
  datos.set_comercial(65)
  datos.set_bin_width(10)
  """
  fig = datos.chart_scatter_px()
  fig.update_layout(title ="Scatter PX")
  fig.show()


  fig = go.Figure()
  fig.add_trace(datos.chart_scatter_go())
  fig.add_trace(datos.chart_scatter_go('UNDER'))
  fig.add_trace(datos.chart_scatter_go('COM'))
  fig.add_annotation(x=datos.mean, y=datos.mean,
              text= f'Full average = {round(datos.get_mean(),2)}',
              showarrow=True,
              arrowhead=0)
  fig.add_annotation(x=datos.get_mean("UNDER"), y=datos.get_mean("UNDER"),
              text= f'industry average = {round(datos.get_mean("UNDER"),2)}',
              showarrow=True,
              arrowhead=0)
  fig.add_annotation(x=datos.get_mean("COM"), y=datos.get_mean("COM"),
              text= f'Commercial average = {round(datos.get_mean("COM"),2)}',
              showarrow=True,
              arrowhead=0)
  fig.update_layout(title ="Scatter GO")

  fig.show()
"""
  fig = go.Figure()
  fig.add_trace(datos.chart_scatter_go())
  fig.add_trace(datos.chart_scatter_go('UNDER'))
  fig.add_trace(datos.chart_scatter_go('COM'))
  fig.add_annotation(x=datos.get_mean(), y=datos.get_mean(),
              text= f'Full mean = {round(datos.get_mean(),2)}',
              font=dict(color = 'Blue'),
              showarrow=True,
              arrowhead=0)
  fig.add_annotation(x=datos.get_mean("UNDER"), y=datos.get_mean("UNDER"),
              text= f'Industry mean = {round(datos.get_mean("UNDER"),2)}',
              font=dict(color = 'Red'),
              showarrow=True,
              arrowhead=0)
  fig.add_annotation(x=datos.get_mean("COM"), y=datos.get_mean("COM"),
              text= f'Commercial mean = {round(datos.get_mean("COM"),2)}',
              font=dict(color = 'Green'),
              showarrow=True,
              arrowhead=0)

  fig.show()

  

  fig =datos.chart_histogram()

  fig.show()


  fig=datos.violin_bins('distance')
  fig.show()


  
  datos.set_comercial(68)
  datos.set_bin_width(5)
  fig = datos.chart_histogram()
  fig.show()

  fig=datos.violin_bins('distance')
  fig.show()




  #px.histogram(datos.df, x='diameter', nbins = datos.num_bins, marginal='violin')
  print("Trabajo terminado desde Windows")
  fig.add_annotation(
          text=f'Full mean = {round(datos.get_mean(),2)}',
          xref="paper", yref="paper",
          font=dict(color = 'Blue'),
          x=0, y=0.99, showarrow=False) 
  fig.add_annotation(
          text=f'Commercial mean = {round(datos.get_mean(self.__commercial_label),2)}',
          xref="paper", yref="paper",
          font=dict(color = 'Green'),
          x=0, y=0.95, showarrow=False)
  fig.add_annotation(
          text=f'Industry mean = {round(datos.get_mean(self.__under_commercial_label),2)}',
          xref="paper", yref="paper",
          font=dict(color = 'Red'),
          x=0, y=0.91, showarrow=False)
  """
