from app import app
from flask import render_template, flash, redirect
from app.forms import ItemForm
from app.modules import item

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ItemForm()
    if form.validate_on_submit():
        flash('Item {}, {}, {}'.format(
            form.itemname.data, form.avaclass.data, form.have_it.data))
        newItem = item()
        newItem.save_item(form.itemname.data,form.avaclass.data, form.itemclass.data, form.have_it.data)
        return redirect('/index')
    return render_template('index.html', title='Home', form=form)

