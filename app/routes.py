from app import app, db
from app.models import Recipe
from app.forms import RecipeForm
from flask import render_template, flash, redirect


def save_recipe(recipe, form):
    form.populate_obj(recipe)
    db.session.add(recipe)
    db.session.commit()


@app.route("/")
@app.route("/index")
def index():
    recipes = Recipe.query.all()
    return render_template("index.html", title="Home", recipes=recipes)


@app.route("/recipe/<id>")
def recipe(id):
    recipe = Recipe.query.filter_by(id=id).first_or_404()
    return render_template("details.html", title=recipe.name, recipe=recipe)


@app.route("/edit/recipe/<id>", methods=["GET", "POST"])
def edit_recipe(id):
    recipe = Recipe.query.filter_by(id=id).first_or_404()
    form = RecipeForm(obj=recipe)
    if form.validate_on_submit():
        save_recipe(recipe, form)
        flash("Recipe {} saved succesfully".format(form.name.data))
        return redirect("/recipe/{}".format(recipe.id))

    return render_template("edit.html", title="Edit recipe", form=form)


@app.route("/new/recipe", methods=["GET", "POST"])
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe()
        save_recipe(recipe, form)
        flash("Recipe {} added successfully".format(form.name.data))
        return redirect("/index")

    return render_template("edit.html", title="Create recipe", form=form)
