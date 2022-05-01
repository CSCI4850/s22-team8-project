import numpy as np
import csv
from sklearn.preprocessing import MinMaxScaler

class RealData:
    
    def __init__(self, recipepath, nutrpath):
        recipefile = open(recipepath)
        recipe_quant = list(csv.reader(recipefile))
        recipe_quant = np.array(recipe_quant)
        recipe_quant = np.array(recipe_quant[1:13,1:-2],dtype=float)#remove headers and scaled recipes
        
        
        nutrfile = open(nutrpath)
        ingr_nutr = list(csv.reader(nutrfile))
        ingr_nutr = np.array(ingr_nutr)
        ingr_nutr = np.array(ingr_nutr[1:,1:],dtype=float)
        ingr_nutr /= 100 #scale by 1g instead of 100g
        
        self.scalers = {}
        self.quant = recipe_quant
        self.recipes = self._build_recipe_nutr(recipe_quant,ingr_nutr)
        
    def _build_recipe_nutr(self,recipe_ingr,ingr_nutr):
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
        
        #print(recipes.shape)
        
        #print(recipes.shape)
        
        return recipe_nutrients

    def normalize(self):
        
        self.scalers['recipes'] = []
        for ind, recipe in enumerate(self.recipes):
            self.scalers['recipes'].append(MinMaxScaler())
            self.scalers['recipes'][ind].fit(recipe)
            self.recipes[ind] = self.scalers['recipes'][ind].transform(recipe)

        self.scalers['quant'] = MinMaxScaler()
        self.scalers['quant'].fit(self.quant.T)
        self.quant = (self.scalers['quant'].transform(self.quant.T)).T
        

    def inv_normalize(self, quant=None):
        if quant is None:
            for ind, recipe in enumerate(self.recipes):
                self.recipes[ind] = self.scalers['recipes'][ind].inverse_transform(recipe)

            self.quant = (self.scaler.inverse_transform(self.quant.T)).T

        else:
            quant = (self.scalers['quant'].inverse_transform(quant.T)).T
            return quant

        
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


        #ranked = ranked.reshape((self.recipes.shape[0], self.recipes.shape[1], 1))
        self.recipes = np.concatenate((self.recipes,ranked), axis = 1)