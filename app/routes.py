from app import app
from flask import render_template, flash, redirect
from app.forms import ItemForm, FilterItem
from app.modules import item
from app.tabels import ItemTable

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ItemForm()
    form2 = FilterItem()
    if form.validate_on_submit():
        newItem = item()
        newItem.save_item(form.itemname.data,form.avaclass.data, form.itemclass.data, form.have_it.data)
        return redirect('/index')
    if form2.validate_on_submit():
        filterItem = item()
        data = filterItem.filter({"haveit":form2.have_it.data})
        tabel = ItemTable(data)
        return render_template('index.html', title='Home', form=form, form2=form2, tabel=tabel)
    allItems = item()
    dinge = allItems.read_items()
    tabel = ItemTable(dinge)
    return render_template('index.html', title='Home', form=form, form2=form2, tabel=tabel)

@app.route('/update/<id>/<richtung>', methods=['POST'])
def update(id,richtung):
    updateItem = item()
    if richtung == "True":
        updateItem.update(id, False)
    else:
        updateItem.update(id, True)
    flash("Item " + id + " wurde geändert! " + richtung)
    return redirect('/index')