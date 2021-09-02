import random


name_list =["Bucatini Cacio e Pepe (Roman Sheep Herder's Pasta)", "Italian Shrimp and Scallop Risotto", "Hearty Minestrone Soup", "Italian Baked Meatballs", "Lemony Pork Piccata", "Lasagne Alla Bolognese Saporite", "Chef John's Italian Meatballs", "Balsamic Bruschetta", "Spaghetti Sauce with Ground Beef", "Caprese Salad with Balsamic Reduction", "Panna Cotta", "Focaccia", "Chicken Katsu", "Spongy Japanese Cheesecake", "Beef Kushiyaki", "Okonomiyaki (Japanese Pancake)", "Sesame Seared Tuna", "Miso Soup", "Homemade Sushi", "Japanese Chicken Curry", "Homemade Chicken Ramen", "Japanese Clear Soup Recipe", "Mochi", "Japanese Beef Curry", "Tonkotsu Ramen Broth Recipe", "Soup Dumplings", "Chinese Lion's Head Soup", "Chicken Lo Mein", "Chinese Spareribs", "Sweet and Sour Chicken", "Chinese Green Bean Stir-Fry", "Tsao Mi Fun (Taiwanese Fried Rice Noodles)", "Chinese Steamed White Fish Fillet with Tofu (Cantonese Style)", "Chinese Steamed Buns with Meat Filling", "Fried Rice", "Chinese Noodle Soup", "Eggplant with Garlic Sauce", "Pork Dumplings", "Two-Ingredient Naan", "Roti Canai/Paratha", "Idli", "Anda di Purjee", "Keema Aloo (Ground Beef and Potatoes)", "Indian Chicken Curry (Murgh Kari)", "Naan", "Red Split Lentils (Masoor Dal)", "Tamarind Sauce Fish Curry", "Delicious Chana Masala", "Roti", "Saag Paneer", "All-American Banana Split", "Wisconsin Butter-Basted Burgers", "Pressure-Cooker Philly Cheesesteak Sandwiches", "Macaroni and Cheese", "Chocolate Chip Cookies", "Honey Chicken Wings", "Tater Tot Casseroles", "Gooey Butter Cake", "Texas Pecan Rice", "Barbecue Pork Cobb Salad", "Carolina-Style Pork Barbecue", "Honey-Glazed Turkey", "Carne Asada Street Tacos", "Mexican Hot Chocolate", "Huevos con Chorizo", "Spanish Rice/Mexican Rice", "Arroz Con Leche", "Chicken Enchiladas", "Arroz con Pollo", "Authentic Mole Sauce", "Chicken Fajitas", "Pozole Rojo (Mexican Pork and Hominy Stew)", "Carnitas (Mexican Slow Cooker Pulled Pork)", "Pan Dulce"] 
Link_list= ["https://www.allrecipes.com/recipe/274411/bucatini-cacio-e-pepe-roman-sheep-herders-pasta/","https://www.allrecipes.com/recipe/262799/italian-shrimp-and-scallop-risotto/", "https://www.allrecipes.com/recipe/262925/hearty-minestrone-soup-instant-pot/", "https://www.allrecipes.com/recipe/268249/italian-baked-meatballs/", "https://www.allrecipes.com/recipe/246757/lemony-pork-piccata/", "https://www.allrecipes.com/recipe/257379/lasagne-alla-bolognese-saporite/","https://www.allrecipes.com/recipe/220854/chef-johns-italian-meatballs/", "https://www.allrecipes.com/recipe/54165/balsamic-bruschetta/", "https://www.allrecipes.com/recipe/158140/spaghetti-sauce-with-ground-beef/", "https://www.allrecipes.com/recipe/228126/caprese-salad-with-balsamic-reduction/", "https://www.allrecipes.com/recipe/72567/panna-cotta/", "https://www.foodnetwork.com/recipes/anne-burrell/focaccia-recipe-1949756", "https://familyapp.com/skip-the-take-out-japanese-recipes-to-make-at-home/", "https://www.allrecipes.com/recipe/256398/spongy-japanese-cheesecake/", "https://www.allrecipes.com/recipe/218058/beef-kushiyaki/", "https://www.allrecipes.com/recipe/255416/okonomiyaki-japanese-pancake/", "https://www.allrecipes.com/recipe/71698/sesame-seared-tuna/", "https://pickledplum.com/japanese-miso-soup-recipe/", "https://www.happyfoodstube.com/homemade-sushi/", "https://www.justonecookbook.com/simple-chicken-curry/", "https://www.forkknifeswoon.com/simple-homemade-chicken-ramen/", "https://www.aspicyperspective.com/japanese-clear-soup-recipe/", "https://www.allrecipes.com/recipe/193307/easy-mochi/", "https://www.justonecookbook.com/japanese-beef-curry/", "https://www.seriouseats.com/rich-and-creamy-tonkotsu-ramen-broth-from-scratch-recipe", "https://thewoksoflife.com/steamed-shanghai-soup-dumplings-xiaolongbao/", "https://www.allrecipes.com/recipe/135367/chinese-lions-head-soup/", "https://dinnerthendessert.com/chicken-lo-mein/", "https://www.allrecipes.com/recipe/77408/chinese-spareribs/", "https://www.allrecipes.com/recipe/8536/sweet-and-sour-chicken-i/", "https://www.allrecipes.com/recipe/49350/chinese-green-bean-stir-fry/", "https://www.allrecipes.com/recipe/173959/tsao-mi-fun-taiwanese-fried-rice-noodles/", "https://www.allrecipes.com/recipe/53519/chinese-steamed-white-fish-fillet-with-tofu-cantonese-style/", "https://www.allrecipes.com/recipe/7031/chinese-steamed-buns-with-meat-filling/", "https://www.gimmesomeoven.com/fried-rice-recipe/", "https://www.recipetineats.com/chinese-noodle-soup/", "https://redhousespice.com/eggplant-with-garlic-sauce/", "https://redhousespice.com/pork-cabbage-dumpling/", "https://www.allrecipes.com/recipe/280310/two-ingredient-naan/", "https://www.allrecipes.com/recipe/247233/roti-canaiparatha-indian-pancake/", "https://hebbarskitchen.com/idli-recipe-soft-idli-idli-rava/","https://www.harighotra.co.uk/anda-di-purjee-recipe", "https://www.allrecipes.com/recipe/231026/keema-aloo-ground-beef-and-potatoes/", "https://www.allrecipes.com/recipe/212721/indian-chicken-curry-murgh-kari/", "https://www.allrecipes.com/recipe/14565/naan/","https://www.allrecipes.com/recipe/247204/red-split-lentils-masoor-dal/", "https://www.allrecipes.com/recipe/245131/tamarind-sauce-fish-curry/", "https://www.allrecipes.com/recipe/236563/delicious-chana-masala/", "https://cooking.nytimes.com/recipes/1020906-roti", "https://www.foodnetwork.com/recipes/aarti-sequeira/saag-paneer1-1927603","https://www.tasteofhome.com/recipes/all-american-banana-split/","https://www.tasteofhome.com/recipes/wisconsin-butter-basted-burgers/","https://www.tasteofhome.com/recipes/pressure-cooker-philly-cheesesteak-sandwiches/","https://www.tasteofhome.com/recipes/creamy-macaroni-and-cheese/","https://www.tasteofhome.com/recipes/big-buttery-chocolate-chip-cookies/", "https://www.tasteofhome.com/recipes/sticky-honey-chicken-wings/","https://www.tasteofhome.com/recipes/tater-tot-casseroles/", "https://www.tasteofhome.com/recipes/gooey-butter-cake/","https://www.tasteofhome.com/recipes/texas-pecan-rice/", "https://www.tasteofhome.com/recipes/barbecue-pork-cobb-salad/","https://www.tasteofhome.com/recipes/carolina-style-pork-barbecue/","https://www.tasteofhome.com/recipes/honey-glazed-turkey/","https://www.eatingonadime.com/easy-carne-asada-street-tacos-recipe/","https://www.isabeleats.com/mexican-hot-chocolate/","https://www.foodnetwork.com/recipes/food-network-kitchen/huevos-con-chorizo-3631788","https://lilluna.com/food-tutorial-spanish-rice/", "https://mexicanfoodjournal.com/arroz-con-leche/","https://www.gimmesomeoven.com/best-chicken-enchiladas-ever/","https://www.foodnetwork.com/recipes/melissa-darabian/arroz-con-pollo-recipe-2121998","https://www.allrecipes.com/recipe/223261/authentic-mole-sauce/","https://www.delish.com/cooking/recipe-ideas/a19665622/easy-chicken-fajitas-recipe/", "https://www.simplyrecipes.com/recipes/posole_rojo/","https://www.recipetineats.com/pork-carnitas-mexican-slow-cooker-pulled-pork/", "https://preppykitchen.com/pan-dulce/"]


time_list= ["ta", "tb", "tc", "tb", "tb", "td", "tc", "ta", "tc", "ta", "td", "td", "ta", "td", "tb", "tb", "ta", "ta", "tb", "tc", "tc", "tc", "td", "td", "td", "td", "tb", "tb", "td", "tc", "tb", "tc", "ta", "td", "ta", "ta", "ta", "tc", "ta", "td", "ta", "ta", "tc", "tb", "td", "td", "tb", "tb", "tc", "tc", "ta", "ta", "ta", "tb", "tb", "tb", "tc", "tc", "tc", "td", "td", "td", "ta", "ta", "ta", "tb", "tb", "tb", "tc", "tc", "tc", "td", "td", "td"]


cuisine_list= ["ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cb", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cc", "cd", "cd", "cd", "cd", "cd", "cd", "cd", "cd", "cd", "cd", "cd", "cd", "ce", "ce", "ce", "ce", "ce", "ce", "ce", "ce", "ce", "ce", "ce", "ce", "cf", "cf", "cf", "cf", "cf", "cf", "cf", "cf", "cf", "cf", "cf", "cf"]  


def find_recipe(cuisine, cook_time, chefs_choice):
  
  result_list = list()
  name = list()
  
  if chefs_choice != None:
    digits = list(range(0, 74))
    random.shuffle(digits)
    
    for i in range(0,3): 
      value = digits[i]
      result_list.append(Link_list[value])
      name.append(name_list[value])
 
    
  else: 
    for i in range(0, len(Link_list)):
      
      if cuisine_list[i] == cuisine and time_list[i] == cook_time and chefs_choice == None:
        result_list.append(Link_list[i])
        name.append(name_list[i])
      if cuisine_list[i] == cuisine and cook_time == None and chefs_choice == None: 
        result_list.append(Link_list[i])
        name.append(name_list[i])
      if cuisine==None and time_list[i] == cook_time and chefs_choice == None: 
        result_list.append(Link_list[i])
        name.append(name_list[i])
  return result_list, name


      



import os

from flask import Flask, url_for, render_template, request



app = Flask(__name__)



@app.route('/')

def render_main():

  return render_template('home.html')

@app.route('/quizpage')

def render_quizpage():

  return render_template('quizpage.html')




@app.route('/results', methods =["GET", "POST"])
def get_results():
  if request.method == "POST":
      
    cuisine = request.form.get("cuisine")
      
    cook_time = request.form.get("cook_time") 

    chefs_choice = request.form.get("random")
    string_blank = str()  
    if cuisine == None and cook_time == None and chefs_choice == None:
      string_blank= "No recipes found."  
      result_list, name = list(), list()
     
    else:
      result_list, name = find_recipe(cuisine, cook_time, chefs_choice)
      
 
  return render_template('results.html', length = len(result_list), results=result_list, recipe_name = name, no_results = string_blank)

    


if __name__=="__main__":

  app.run(host='0.0.0.0')

