import numpy as np
import random
import csv

class Generator:
    
    def __init__(self,filepath):
        
        # Open arg file and convert to string np array
        datafile = open(filepath)
        data = list(csv.reader(datafile))
        data = np.array(data)
        
        self.nutrients = data[0] # get top row (name of the nutrients)
        self.names = data[:,0] # get left column (name of the ingredients)
        self.ingrs = np.array(data[1:,1:],dtype=float) # split array leaving only data, convert data to float
        self.ingrs /= 100 #scale by 1g instead of 100g
            
        self.recipes = None
        self.quant = None
        self.scalers = {}
        
  
    def generate(self,num):
        self.quant = self._build_quantity(num)
        self.recipes = self._build_recipes(self.quant,self.ingrs)
    
    def _build_recipes(self,recipe_ingr,ingr_nutr):
        recipes = []
        
        for i in range(recipe_ingr.shape[0]): # for each recipes
            recipe = recipe_ingr[i]
            for j in range(recipe_ingr.shape[1]): # for ingr quantity in recipe
                quant = recipe[j]
                recipes.append(quant * ingr_nutr[j])
                
        recipes = np.array(recipes)
        recipes = recipes.reshape((-1,ingr_nutr.shape[0],ingr_nutr.shape[1]))
        
        recipe_nutrients = []
        for recipe in recipes:
            nutrients = []
            for c in range(recipe.shape[1]):
                col = recipe[:,c]
                sum_col = np.sum(col)
                nutrients.append(sum_col)
            recipe_nutrients.append(nutrients)
        
        
        recipe_nutrients = np.array(recipe_nutrients)
        
        return recipe_nutrients
        
    def _build_quantity(self, num_of_recipes):
        
        quants = []
        ing_max = [14, 472, 28.5,544,28,25.2,49.6,8.48,630,28.6,19.5,10.6,66.7,540,240]
        
        for i in range(num_of_recipes):
        
            ingrs = np.zeros((15))
            ingrs[0] = 1

            r = random.random()
            # Liquids
            if r < 0.2: #1/5 chance of Milk
                ingrs[14] = 1
            if r >= 0.1:#9/10 chance of Water
                ingrs[1] = 1

            # Which flour?
            r = random.random()    
            if r < .6:
                ingrs[3] = 1
            elif r < .9:
                ingrs[13] = 1
            else:
                ingrs[8] = 1
                
            # Which - if any - sweetener
            r = random.random()
            if r < .1:
                ingrs[11] = 1
            elif r < .2:
                ingrs[12] = 1
            elif r < .8:
                ingrs[5] = 1

            # Which - if any - lipids?
            r = random.random()    
            if r < .25:
                ingrs[9] = 1
            elif r < .5:
                ingrs[10] = 1
            elif r < .75:
                ingrs[4] = 1

            ingrs[2] = 1 #salt

            #Egg ?
            r = random.random()    
            if r < .2:
                ingrs[6] = 1

            #Dry Milk ?
            r = random.random()    
            if r < .1:
                ingrs[7] = 1

            ingrs[0] = random.random() * 12.5 + 2.5
            
            
            for i in range(0, 14):
                ingrs[i] *= random.random() * ing_max[i] * 1.25
                if (ingrs[i]) < 0:
                    ingrs[i] = 0
                        
            quants.append(ingrs)
            
        
        return np.array(quants)
        

    def rank(self):
        ranked = np.zeros((self.quant.shape))
        argsort = np.argsort(self.quant)[:,::-1]
        
        for i in range(0, argsort.shape[0]):
            count = self.quant.shape[1] - 1
            ranked[i,argsort[i,0]] = count
            
            for j in range(1, argsort.shape[1]):
                ind1 = argsort[i,j-1]
                ind2 = argsort[i,j]

                count -= 1
                
                ranked[i,ind2] = count


        self.recipes = np.concatenate((self.recipes,ranked), axis = 1)