# s22-team8-project

## Team #8 - Inverse Nutrition Mapping

![Nutrients](/Project_Demo_Folder/images/breadnutrients.png)

![Ingredients](/Project_Demo_Folder/images/breadingredients.png)

This neural network is designed to take in information from nutritional facts labels, such as the nutrient information and ingredient order, and the network will return the mass in grams of each ingredient. Specifically, this network was limited to focus on breads, so the selection of ingredients was limited to the fifteen ingredients most commonly found in bread. Similarly, the nutrient information was limited to only include nutrients that the Food and Drug Administration requires to be present on all nutritional facts labels.

The following table represents the ingredients and their respective nutrients:

|Ingredient | Calories | Total Fat         | Saturated Fat | Cholesterol | Sodium | Total Carbs | Fiber  | Sugar | Protein | Vitamin D | Calcium | Iron     | Potassium |
|-------------------|---------------|-------------|--------|-------------|--------|-------|---------|-----------|---------|----------|-----------|-------|-------|
| Active Dry Yeast  | 295           | 4.6         | 0.6    | 0           | 0.05   | 38.2  | 21      | 0         | 38.3    | 0        | 0.064     | 0.017 | 2     |
| Water             | 0             | 0           | 0      | 0           | 0.003  | 0     | 0       | 0         | 0       | 0        | 0.003     | 0     | 0.001 |
| Salt              | 0             | 0           | 0      | 0           | 38.758 | 0     | 0       | 0         | 0       | 0        | 0.024     | 0     | 0.008 |
| Bread Flour       | 361           | 1.7         | 0.2    | 0           | 0.002  | 72.5  | 2.4     | 0.3       | 12      | 0        | 0.015     | 0.004 | 0.1   |
| Butter            | 717           | 81.1        | 51.4   | 0.215       | 0.576  | 0.1   | 0       | 0.1       | 0.9     | 0.000056 | 0.024     | 0     | 0.024 |
| Sugar             | 375           | 0           | 0      | 0           | 0      | 100   | 0       | 100       | 0       | 0        | 0         | 0     | 0     |
| Egg               | 143           | 9.9         | 3.1    | 0.372       | 0.14   | 0.8   | 0       | 0.8       | 12.6    | 0.000035 | 0.053     | 0.002 | 0.134 |
| Dry Milk          | 496           | 26.7        | 16.7   | 0.097       | 0.371  | 38.4  | 0       | 38.4      | 26.3    | 0.000312 | 0.912     | 0     | 1.33  |
| Wheat Flour       | 364           | 1           | 0.2    | 0           | 0.002  | 76.3  | 2.7     | 0.3       | 10.3    | 0        | 0.015     | 0.005 | 0.107 |
| Vegetable Oil     | 884           | 100         | 7.4    | 0           | 0      | 0     | 0       | 0         | 0       | 0        | 0         | 0     | 0     |
| Olive Oil         | 800           | 93.3        | 13.3   | 0           | 0      | 0     | 0       | 0         | 0       | 0        | 0         | 0     | 0     |
| Honey             | 304           | 0           | 0      | 0           | 0.004  | 82.4  | 0.2     | 82.1      | 0.3     | 0        | 0.006     | 0     | 0.052 |
| Brown Sugar       | 380           | 0           | 0      | 0           | 0.028  | 98.1  | 0       | 97        | 0.1     | 0        | 0.083     | 0.001 | 0.133 |
| All-Purpose Flour | 364           | 1           | 0.2    | 0           | 0.002  | 76.3  | 2.7     | 0.3       | 10.3    | 0        | 0.015     | 0.005 | 0.107 |
| Milk              | 50            | 2.1         | 1.2    | 0.008       | 0.047  | 4.9   | 0       | 4.5       | 3.3     | 0.000001 | 0.119     | 0     | 0.057 |

A typical input is composed of two tensors. One represents the nutritional information and the other contains the ordinal ingredient information.

The nutritional information refers to the quantities of each micro- and macronutrient whose disclosure on nutritional facts labels is mandated by the FDA. An example of what the input for this tensor might look like appears in the table below. In that example, the recipe has 500 Calories, eight grams of total fat, and so on:

|Calories | Total Fat | Saturated Fat | Cholesterol | Sodium | Total Carbs | Fiber  | Sugar | Protein | Vitamin D | Calcium | Iron | Potassium 
|-|-|-|-|-|-|-|-|-|-|-|-|-
|500           | 8         | 4.5    | 0           | 0.05   | 30  | 18      | 2         | 38.3    | 0        | 0.1     | 0.02 | 2     |

The ordinal ingredient information simply represents the relative magnitude of each ingredient. Each of the fifteen ingredients has its own index in this tensor. The element's value is set to zero for any ingredients not present in the recipe. Then, ingredients are assigned integer values in ascending order, so that the ingredient(s) with the smallest non-zero mass in the recipe are given a value of one, the next largest mass is given a value of 2, and so on.

The output of the model will contain information structured like this, with the masses of each ingredient given in grams:

| Bread flour | Water | Butter | Sugar | Salt | Dry milk | Active dry yeast | Egg | Whole wheat flour | Vegetable oil | Olive oil | Honey | Brown sugar | All-purpose flour | Milk |
|-------------|-------|--------|-------|------|----------|------------------|-----|-------------------|---------------|-----------|-------|-------------|-------------------|------|
| 408         | 236   | 14     | 12.6  | 8.6  | 8.48     | 5.6              | 0   | 0                 | 0             | 0         | 0     | 0           | 0                 | 0    |

## Running the Demo

1. Python 3.0 or higher is needed. This can be found on [the Python website](https://www.python.org/downloads/)
2. The project is written in .ipynb files that require Jupyter Notebook, [which can be installed from here](https://jupyter.org/install)
3. Once the dependencies are installed, navigate to and open the "Project Demo.ipynb" file in the "Project_Demo_Folder" directory and run each cell by clicking on the ▶ button above the code/text.

Alternatively, the demo can be viewed (but not run) from GitHub through the [Project Demo notebook](Project_Demo_Folder/Project%20Demo.ipynb)

## Companion Files

The copy of the nutritional information table given above that is used by the project is saved in [the nutrients.csv](main/nutrients.csv) file.

Testing data was created by generating random bread-like recipes. These recipes all contained yeast, a liquid, and a flour, and optionally additionally contained a sweetener, lipid, salt, egg, and dry milk. A small number of [real recipes](main/Recipe_Data.csv) were used for validation as well.
