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
         
        self.recipes = None
        self.quant = None
        

    # Generates n number of training examples
    #    arg1 (datapoints): number of training examples to generate
    #    arg2 (min_ingr): minimum number of ingredients to include in each recipe
    #    arg3 (max_ingr): max number of ingredients to include in each recipe
    def generate(self, datapoints, min_ingr=1, max_ingr=None):
        
        recipes = []
        quant = []
        
        # max_ingr defaults to maximum number of possible ingredients in dataset
        if max_ingr is None:
            max_ingr = self.ingrs.shape[0]
        
        # generate datapoints number of training examples
        for i in range(datapoints):
        
            # randomize num of ingredients for each recipe between lower and upper bounds
            num_ingr = random.randint(min_ingr,max_ingr) 

            # get random sample of ingredients
            rows_ingr = random.sample(range(self.ingrs.shape[0]),num_ingr)
            rows_ingr.sort()

            recipe = np.array([])
            # generate recipe for each line
            for i in range(self.ingrs.shape[0]):
                if i in rows_ingr:
                    recipe = np.append(recipe,self.ingrs[i])
                    quant.append(1.0) # quantity default is 1.0 if ingr exists in recipe
                else:
                    recipe = np.append(recipe, np.zeros(self.ingrs.shape[1]))
                    quant.append(0.0) # quantity default is 0.0 if ingr doesnt exist in recipe
            
            # reshape recipe into 2D matrix
            recipe = np.reshape(recipe,self.ingrs.shape)
            recipes.append(recipe) # append makes recipes var a 3D matrix
        
        self.recipes = np.array(recipes)
        self.quant = np.array(quant).reshape((-1,self.recipes.shape[1]))

    # scales each ingredient randomly lower bound and upper bound
    #   arg1 (min_scale): lower bound scale value
    #   arg2 (max_scale): upper bound scale value
    # both args can be set to same value to scale the entire dataset equally
    def scale(self, min_scale, max_scale):
        
        for i, recipe in enumerate(self.recipes):
            for j, ingr in enumerate(recipe):
                scalefactor = round(random.uniform(min_scale,max_scale),2)
                
                self.recipes[i,j] *= scalefactor
                self.quant[i,j] *= scalefactor
                

    
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
        