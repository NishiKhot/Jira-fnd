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
        # Log the received data for debugging
        print(f"Received webhook data: {data}")

        # Process the webhook data here
        issue_key = data["issue"]["key"] if "issue" in data else "No issue key"
        event_type = data["webhookEvent"] if "webhookEvent" in data else "No event type"

        # Create or append to a file with the received data
        file_path = "webhook_data.txt"
        with open(file_path, "a") as f:
            f.write(
                f"{datetime.now()} - Issue Key: {issue_key}, Event Type: {event_type}\n"
            )
            f.write(f"{data}\n\n")

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
