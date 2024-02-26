from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy survey data (can be replaced with a database)
surveys = []

@app.route('/')
def index():
    return render_template('index.html', surveys=surveys)

@app.route('/create_survey', methods=['GET', 'POST'])
def create_survey():
    if request.method == 'POST':
        question = request.form['question']
        options = request.form.getlist('options')
        surveys.append({'question': question, 'options': options})
        return redirect(url_for('index'))
    return render_template('create_survey.html')

@app.route('/respond_survey/<int:survey_id>', methods=['GET', 'POST'])
def respond_survey(survey_id):
    survey = surveys[survey_id]
    if request.method == 'POST':
        selected_option = request.form['option']
        # Do something with the response, like saving it to a database
        return redirect(url_for('index'))
    return render_template('respond_survey.html', survey=survey, survey_id=survey_id)

if __name__ == '__main__':
    app.run(debug=True)
