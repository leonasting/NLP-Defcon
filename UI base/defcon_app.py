# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:02:16 2021

@author: Checkout
"""
from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
#import plotly
#import plotly.express as px
import json
import matplotlib.pyplot as plt
import os
#fig = px.imshow([[1, 20, 30],
#                 [20, 1, 60],
#                 [30, 60, 1]])


#graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#fig.show()
app = Flask(__name__)
import openai

openai.api_key = "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"

@app.route("/")
def home():
    return render_template("main_1.html")

@app.route("/main", methods=["POST", "GET"])
def main():

    if request.method == "POST":

        contract= request.form["Contract"]
        question= request.form["question"]
        option= request.form["option"]
        #print("wowo"+nd)

        print("Contract:",contract)
        print("question:",question)


        #sentence=nd
        #new_grid=GridPOMDP(int(side.strip()),int(bomb.strip()),start=[int(i) for i in start.split(',')],goal=[int(i) for i in goal.split(',')])
        #new_grid.add_bomb()
        if option=="Fetch Answers":
            print("Query:","Write questions based on the text below\n\nText:"+contract+"\n\nQuestions:\n"+question+"\n\nAnswer:\n1.")
            response = openai.Completion.create(
                                                engine="davinci-instruct-beta",
                                                prompt=f"Get answer based on the question\n\nText:{contract}\n\nQuestions:\n{question}\n\nAnswer:\n1.",
                                                temperature=0,
                                                max_tokens=257,
                                                top_p=1,
                                                frequency_penalty=0,
                                                presence_penalty=0
                                                )
            ans =  response['choices'][0]['text']
            print("response",response)
            print("ans",ans)
            #new_grid.q_learning()
            #df=new_grid.display_path()
            #q_reward=[i for i in new_grid.ls_reward]
            #print(q_reward)
            #new_grid.reset_q_val()



            return render_template("label.html",answer=ans)#,table2=df2.to_html(classes='data'),url ='./static/images/new_plot2.png')
    else:
        return render_template("main_1.html")

"""
esponse = openai.Completion.create(
            engine="davinci-instruct-beta",
            prompt=f"Write questions based on the text below\n\nText: {context}\n\nQuestions:\n{questions}\n\nAnswers:\n1.",
            temperature=0,
            max_tokens=257,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
}
"""
if __name__ == "__main__":
    app.run(debug=True)
