from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a_secret_key'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        new_contact = Contact(
            store_name=form.store_name.data,
            phone_number=form.phone_number.data,
            email=form.email.data,
            address=form.address.data
        )
        db.session.add(new_contact)
        db.session.commit()
        flash('Contact added successfully!')
        return redirect(url_for('index'))
    return render_template('add_contact.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.store_name = form.store_name.data
        contact.phone_number = form.phone_number.data
        contact.email = form.email.data
        contact.address = form.address.data
        db.session.commit()
        flash('Contact updated successfully!')
        return redirect(url_for('index'))
    return render_template('update_contact.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET'])
def search_contact():
    query = request.args.get('query')
    contacts = Contact.query.filter(
        Contact.store_name.contains(query) | Contact.phone_number.contains(query)
    ).all()
    return render_template('index.html', contacts=contacts)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
