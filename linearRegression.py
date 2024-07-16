#importing packages
#sample data
import numpy as np
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression

cakes=[10,20,30,40,50]
money=[25,50,75,100,125]

fig=go.Figure()

fig.add_trace(go.Scatter(x=cakes,y=money,mode='markers',))
fig.update_layout(title='Relationship between cake and money',xaxis_title='Cakes sold',yaxis_title='Money made')


x=np.array(cakes).reshape(-1,1)
y=np.array(money)
model=LinearRegression().fit(x,y)
new_cake=[[25]]
new_money=model.predict(new_cake)
print("New money made is:",new_money[0])
fig.show()