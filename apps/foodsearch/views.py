from django.shortcuts import render, redirect
from .models import *
import re
import bcrypt
from django.contrib import messages

def index(request): #render homepage
    return render(request, "foodsearch/index.html")

def viewtest(request): #render homepage
    return render(request, "foodsearch/recipeslist.html")

def view_add(request): #render add page
    context = {
        "recipes": Recipe.objects.all(),
        "ingredents": Ingre.objects.all()
    }
    return render(request, "foodsearch/add.html", context)   

def add_recipe(request): #processing for adding recipe form.cleaned_data['image']
    admin = User.objects.get(id=1)
    Recipe.objects.create(user= admin, recipename=request.POST['recipename'], picture=request.POST['pic'], shortdesc=request.POST['shortdesc'],description=request.POST['description'])
    return redirect("/dashboard")    

def add_ingre(request): #processing for adding ingredients
    admin = User.objects.get(id=1)
    Ingre.objects.create(ingre_name=request.POST['ingre_name'], user= admin )
    return redirect("/dashboard")

def addtogether(request): #Add many to many, recipe amd ingredent together
    this_recipe = Recipe.objects.get(id=request.POST['recipe-list'])
    this_ingre = Ingre.objects.get(id=request.POST['ingre-list'])
    this_ingre.recipes.add(this_recipe)
    return redirect("/dashboard/addtoge")

def delete_recipe(request,id): #Delete recipe
    delete_recipe = Recipe.objects.get(id=id)
    delete_recipe.delete()
    return redirect("/dashboard/viewdatabase")

def delete_ingre(request,id): #Delete ingredient
    delete_ingre = Ingre.objects.get(id=id)
    delete_ingre.delete()
    return redirect("/dashboard/viewdatabase")

def delete_ingre_recipe(request,reid,inid): #Delete ingredient of the recipe
    delete_ingre = Ingre.objects.get(id=inid)
    delete_recipe = Recipe.objects.get(id=reid)
    delete_recipe.ingres.remove(delete_ingre)
    return redirect("/dashboard/viewdatabase")

def admin_login(request): #View Database ALL ingredients and ALL recipes
    return render(request, "foodsearch/login.html")

def logacc(request):
    user = User.objects.get(email = request.POST['log-email'])
    request.session['user_id'] = user.id
    if request.POST['log-pw'] == user.pword:
        request.session['logged'] = True
        return redirect('/dashboard')
    else:
        request.session['logged'] = False
        return redirect("/admin")

def view_admin(request): #View Database ALL ingredients and ALL recipes
    if request.session['logged'] == False:
        return redirect("/admin")
    elif request.session['logged'] == True:
        context = {
                "all_recipes": Recipe.objects.all(), "all_ingredients": Ingre.objects.all()
        }
    return render(request, "foodsearch/superadmin.html",context)

def view_addtoge(request): #View page add together in admin
    if request.session['logged'] == False:
        return redirect("/admin")
    elif request.session['logged'] == True:
        context = {
            "recipes": Recipe.objects.all().order_by('recipename'),
            "ingredents": Ingre.objects.all().order_by('ingre_name')
        }
        return render(request, "foodsearch/addtoge.html", context)

def logoutacc(request): #View page add together in admin
    request.session.clear()
    request.session['logged'] = False
    return redirect("/admin")

def view_database(request): #View page add together in admin
    if request.session['logged'] == False:
        return redirect("/admin")
    elif request.session['logged'] == True:
        context = {
            "recipes": Recipe.objects.all(),
            "ingredents": Ingre.objects.all()
        }
        return render(request, "foodsearch/database.html", context)

def edit_recipe(request,id): #render edit recipe
    context = {
        "recipe": Recipe.objects.get(id=id)
    }
    return render(request, "foodsearch/superedit.html",context)

def edit_ingre(request,id): #render edit ingre
    context = {
        "ingre": Ingre.objects.get(id=id)
    }
    return render(request, "foodsearch/superedit.html",context)

def BTeditingre(request): # processing for editing Ingredient
    ingre = Ingre.objects.get(id=request.POST['idingre'])
    ingre.ingre_name = request.POST['ingre_name_edit']
    ingre.save()
    return redirect("/dashboard/viewdatabase")

def BTeditrecipe(request): # processing for editing Recipe
    recipe = Recipe.objects.get(id=request.POST['idrecipe'])
    recipe.recipename = request.POST['recipe_name_edit']
    recipe.picture = request.POST['picture']
    recipe.shortdesc = request.POST['shortdesc']    
    recipe.description = request.POST['description']
    recipe.save()
    return redirect("/dashboard/viewdatabase")

def process(request): #search bar processing
    in_key = re.split('; |, |\*| |,',request.GET['searchbox']) #in_key = [avocado,bean,penut]
    newlist = list(set(in_key))
    if len(newlist) == 1:
        try:
            ingre_input = Ingre.objects.get(ingre_name=str(in_key[0]).lower())
            finalarray = Recipe.objects.filter(ingres=ingre_input)
            if not finalarray:
                return render(request, "foodsearch/notfound.html")
            else:
                context = {
                    "found": len(finalarray),
                    "recipes": finalarray
                }
        except Ingre.DoesNotExist:
            return render(request, "foodsearch/notfound.html")
    else:
        query_set_array = []
        for i in newlist:
            try:
                ingre_input = Ingre.objects.get(ingre_name=str(i).lower())
                a = Recipe.objects.filter(ingres=ingre_input)
                query_set_array.extend(a)
            except Ingre.DoesNotExist:
                pass
        finalarray = list(set(query_set_array))
        if not finalarray:
            return render(request, "foodsearch/notfound.html")
        else:
            context = {
                "found": len(finalarray),
                "recipes": finalarray
            }
    return render(request, "foodsearch/recipeslist.html", context)

def fulldetail(request,id):
    re = Recipe.objects.get(id=id)
    context = {
        "recipe" : Recipe.objects.get(id=id),
        "ingre": re.ingres.all()
    }
    return render(request, "foodsearch/recipes.html",context)
