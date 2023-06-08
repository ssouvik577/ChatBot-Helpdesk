from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configure OpenAI API credentials
openai.api_key = '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'

# Health conditions and severity options
health_conditions = ['Headache', 'Cough', 'Fever']
severity_levels = ['Low', 'Medium', 'High']

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        # Get selected condition and severity from the form
        condition = request.form.get('condition')
        severity = request.form.get('severity')

        # Generate chatbot response using ChatGPT API
        prompt = f'Condition: {condition}\nSeverity: {severity}\n'
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the generated message from the API response
        message = response.choices[0].text.strip()

        # Render the chatbot template with the message
        return render_template('index.html', message=message, conditions=health_conditions, severities=severity_levels)

    # Render the initial chatbot template
    return render_template('index.html', conditions=health_conditions, severities=severity_levels)

if __name__ == '__main__':
    app.run(debug=False, port="0.0.0.0")
