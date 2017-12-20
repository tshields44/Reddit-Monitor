


from spyre import server

import os
import pandas as pd
import urllib2
import json
import seaborn as sns

class Reddit(server.App):
    title = "Reddit Monitor"


    inputs = [{     "type":'dropdown',
                    "label": 'Month',
                    "options" : [ {"label": filename, "value": filename} for filename in os.listdir("/Users/TracyShields/data")],
                    "key": 'file',
                    "action_id": "update_data"}]

    controls = [{   "type" : "hidden",
                    "id" : "update_data"}]

    tabs = [ "Plot","Table"]

    outputs = [{ "type" : "plot",
                    "id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot"},
                { "type" : "table",
                    "id" : "table_id",
                    "control_id" : "update_data",
                    "tab" : "Table" }]

    def getData(self, params):
        filename = params["file"]
        df = pd.read_csv("/Users/TracyShields/data/" + filename)
        df = df.drop('Unnamed: 0', 1)

        return df

    def getPlot(self, params):

        filename = params["file"]
        #df = pd.read_csv("/Users/TracyShields/data/" + filename)
        df = self.getData(params).set_index('subreddit')
        #df = df.drop('Unnamed: 0', 1)
        plt_obj = df.plot(kind='bar')
        plt_obj.set_ylabel("Comments")
        plt_obj.set_title("Trends")
        fig = plt_obj.get_figure()
        return fig

app = Reddit()
app.launch(host='0.0.0.0',port=5000)
