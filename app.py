#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime

app = Flask(__name__)


@app.route("/api/data", methods=["GET"])
def get_data():
    # Dummy data
    data = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    return jsonify(data)


@app.route("/webhook", methods=["POST"])
def jira_webhook():
    # Ensure the request is in JSON format
    if request.is_json:
        data = request.json
        # Log the received data to the console

        # Process the webhook data here
        issue_key = data["issue"]["key"] if "issue" in data else "No issue key"
        event_type = data["webhookEvent"] if "webhookEvent" in data else "No event type"

        print(f"Received webhook data: {issue_key} and {event_type}")

        return (
            jsonify(
                {
                    "message": "Webhook received!",
                    "issue_key": issue_key,
                    "event_type": event_type,
                }
            ),
            200,
        )
    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:


# In[ ]:


# In[ ]:
