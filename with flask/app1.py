from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'low' not in session or 'high' not in session:
            session['low'] = int(request.form['low'])
            session['high'] = int(request.form['high'])
            session['number'] = random.randint(session['low'], session['high'])
            session['chances'] = 7
            session['guess_count'] = 0
            session['message'] = ''

        guess_input = request.form.get('guess')
        if guess_input:
            guess = int(guess_input)
            # Your logic continues here...
        else:
            return redirect(url_for('index'))
        session['guess_count'] += 1
        number = session['number']
        chances = session['chances']
        count = session['guess_count']

        if guess == number:
            session['message'] = f"🎉 Correct! You guessed the number {number} in {count} attempts."
        elif count >= chances:
            session['message'] = f"❌ Game Over! The correct number was {number}."
        elif guess > number:
            session['message'] = "Too high! Try a lower number."
        else:
            session['message'] = "Too low! Try a higher number."

        return redirect(url_for('index'))

    return render_template('index.html', session=session)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
