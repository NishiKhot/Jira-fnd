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


@app.route("/webhook", methods=["POST"])
def jira_webhook():
    # Ensure the request is in JSON format
    if request.is_json:
        data = request.json
        # Log the received data for debugging
        print(f"Received webhook data: {data}")

        # Process the webhook data here
        # For example, you can extract the issue key and event type
        issue_key = data["issue"]["key"] if "issue" in data else "No issue key"
        event_type = data["webhookEvent"] if "webhookEvent" in data else "No event type"

        # Add your custom processing logic here

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
