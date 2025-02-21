# recipe.py
def calculate_ingredients(servings):
    try:

        if servings < 1:
            raise ValueError("Servings must be at least 1.")
        

        warm_water  = servings * 1.5 
        sugar_needed = servings * 24 #1 tbsp
        instant_yeast = servings * 7 #2.25 tsp


        flour_needed = servings * 570  # 4.75 cups
        salt = servings * 12 #
        butter = servings * 60 #mL

        
        return (f"For {servings} servings:\nFlour: {flour_needed}g\nSugar: {sugar_needed}g\nInstant Yeast: {instant_yeast}g\nSalt: {salt}g\nButter: {butter}g\nWarm Water: {warm_water}g")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of servings.")
