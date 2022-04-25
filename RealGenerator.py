import numpy as np
import csv
import random
from sklearn.preprocessing import MinMaxScaler

class RealGenerator:
    
    def __init__(self, nutrpath):
        recipe_quant = self._build_quantity(100)
        nutrfile = open(nutrpath)
        ingr_nutr = list(csv.reader(nutrfile))
        ingr_nutr = np.array(ingr_nutr)
        
        
        self.ingr_nutr = np.array(ingr_nutr[1:,1:],dtype=float)
        self.ingr_nutr /= 100 #scale by 1g instead of 100g
        
        self.scalers = {}
        self.quant = None
        self.recipes = None
        
    def generate(self,num):
        self.quant = self._build_quantity(num)
        self.recipes = self._build_recipe_nutr(self.quant,self.ingr_nutr)
        
    def _build_recipe_nutr(self,recipe_ingr,ingr_nutr):
        recipes = []
        
        print(recipe_ingr.shape)
        for i in range(recipe_ingr.shape[0]): # for each recipes
            recipe = recipe_ingr[i]

            for j in range(recipe_ingr.shape[1]): # for ingr quantity in recipe
                quant = recipe[j]
                recipes.append(quant * ingr_nutr[j])
                
        
    
        recipes = np.array(recipes)
        recipes = recipes.reshape((-1,ingr_nutr.shape[0],ingr_nutr.shape[1]))
        return recipes

    
    def _build_quantity(self, num_of_recipes):
        
        quants = []
        ing_averages = [1,59.5,2.1,73.3,3.8,2.3,9.8,1.3,75,6.4,3.5,2.5,7.9,100.6,37.5]
        ing_stdev = [0,35,9,1.0,21.8,1.0,1.3,1.4,0.3,0.5,0.5,0.5,56.7,5.4]
        
        for i in range(num_of_recipes):
        
            ingrs = np.zeros((15))
            ingrs[0] = 1

            r = random.random()
            # Liquids
            if r < 0.2: #1/5 chance of Milk
                ingrs[14] = 1
            if r >= 0.1:#9/10 chance of Water
                ingrs[1] = 1

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

            for i in range(1, 14):
                if (ingrs[i] > 0):
                    ingrs[i] = np.random.normal(ing_averages[i], ing_stdev[i])
                    if (ingrs[i]) < 0:
                        ingrs[i] = 0
                        
            quants.append(ingrs)
            
        return np.array(quants)
            
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
                self.recipes[ind] = self.scalers[ind].inverse_transform(recipe)

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

            
            
        ranked = ranked.reshape((self.recipes.shape[0], self.recipes.shape[1], 1))
        self.recipes = np.concatenate((self.recipes,ranked), axis = 2)