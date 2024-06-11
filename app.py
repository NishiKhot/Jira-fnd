#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/api/data", methods=["GET"])
def get_data():
    # Dummy data
    data = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:


# In[ ]:


# In[ ]:
