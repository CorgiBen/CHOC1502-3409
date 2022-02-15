#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask


# In[ ]:


app=Flask(__name__)


# In[ ]:


from flask import request, render_template
import joblib


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        sugar=request.form.get("sugar")
        milk=request.form.get("milk")
        print(sugar,milk)
        model=joblib.load("CTaste")
        pred=model.predict([[float(sugar),float(milk)]])
        print(pred)
        pred=pred[0]
        s="The predicted taste is: " + str(pred)
        return(render_template("index.html", result= s))
    else:
        return(render_template("index.html", result="Predict Chocolate Taste"))


# In[ ]:


if __name__== "__main__":
    app.run()


# In[ ]:




