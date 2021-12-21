import logging
import os

from flask import render_template, flash, redirect

from app import app, db
from app.forms import RecipeForm
from app.models import Recipe
import yaml


def save_recipe(recipe, form):
    form.populate_obj(recipe)
    db.session.add(recipe)
    db.session.commit()


def import_sample_data(path):
    with open(path, mode='r') as file:
        recipe_definition = yaml.load(file, Loader=yaml.FullLoader)
        Recipe.query.filter_by(name=recipe_definition["name"]).delete()
        db.session.commit()

        obj = Recipe()
        obj.name = recipe_definition["name"]
        obj.ingredients = recipe_definition["ingredients"]
        obj.directions = recipe_definition["directions"]
        db.session.add(obj)
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


@app.route("/generate/test-data", methods=["GET"])
def generate_test_data():
    for root, _, files in os.walk("app/sample_data"):
        for f in files:
            if f.split(".")[-1] in ["yaml", "yml"]:
                file_path = os.path.join(root, f)
                logging.info(f"Importing sample recipe {file_path}")
                import_sample_data(file_path)

    return redirect("/index")
