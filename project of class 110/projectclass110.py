import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("data.csv")
data=df["reading_time"].to_list()

meanpop=statistics.mean(data)
sdpop=statistics.stdev(data)

print(sdpop)
print(meanpop)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)    
    return mean



def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        setofmeans=random_set_of_mean(100)
        mean_list.append(setofmeans)
    #show_fig(mean_list)
    mean=statistics.mean(mean_list)  
    sd=statistics.stdev(mean_list)  

    print("meanofsamplinglist",mean)
    print("sdofsamplinglist",sd)
    
    

setup()