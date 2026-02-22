import secrets
from flask import Flask, render_template, url_for, flash, redirect
from loguru import logger
from forms import Expense


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(22)


@app.route('/')
def index():
    logger.debug("We're home")
    return render_template('index.html')


@app.route('/expense', methods=['GET', 'POST'])
def expense():
    logger.debug("At expense view")
    form = Expense()

    if form.validate_on_submit():
        flash("Thanks for filling out our expense form!")
        logger.debug("Expense for filled out!")
        return redirect(url_for('index'))

    return render_template('expense.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
