from flask import Flask, request, render_template
from google.oauth2 import service_account
import dialogflow_v2 as dialogflow

app = Flask(__name__)


@app.route('/')
def home():
    # just render the HTML homepage
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def detect_intent():
    # create a new session
    credentials = service_account.Credentials.from_service_account_file("homie-key.json")
    session_client = dialogflow.SessionsClient(credentials=credentials)

    # replace the project id, since it is fake
    # 123456 is the session id, which should not be changed within an entire conversation with a single user
    session = session_client.session_path("homie-l9jt", 123456)

    # prepare a new query input with the inner text, taken from the POST request
    text_input = dialogflow.types.TextInput(text=request.form["message"], language_code="en-US")
    query_input = dialogflow.types.QueryInput(text=text_input)

    # send the request and get the response
    response = session_client.detect_intent(session=session, query_input=query_input)

    # reply to the POST request: the textual response is in "fullfilment"
    return response.query_result.fulfillment_text


if __name__ == '__main__':
    app.run()
