# Sample of a Web-based Voice User Interface (in Python)

This repository is an example for getting started with voice user interfaces.

It uses the Web Speech API (experimental) for speech-to-text and text-to-speech operations. For Natural Language Processing, it uses [Dialogflow ES](https://dialogflow.cloud.google.com) agent, included as a `.zip` file.

Tested in Chrome 57+, Firefox 70+, and Safari 10.1+. Please, notice that speech-to-text capability does not work in Safari and Firefox.

To get started with the project, import the `WeatherAgent.zip` into Dialogflow, generate a _service key_ from Google (in JSON), and download it into the root of the project as `client-secret.json`.
