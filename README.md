# s22-team8-project

## Team #8 - Inverse Nutrition Mapping


This neural network is designed to take in bread recipies and their macro and micronutrients, such as those off of a nutritional facts label, and the network will return the masses of each ingredient (in grams) in descending order. For example:

Taking in these nutrients:

| Calories | Total Fat         | Saturated Fat | Cholesterol | Sodium | Total Carbs | Fiber  | Sugar | Protein | Vitamin D | Calcium | Iron     | Potassium |       |       |
|----------|-------------------|---------------|-------------|--------|-------------|--------|-------|---------|-----------|---------|----------|-----------|-------|-------|
| 1        | Active Dry Yeast  | 295           | 4.6         | 0.6    | 0           | 0.05   | 38.2  | 21      | 0         | 38.3    | 0        | 0.064     | 0.017 | 2     |
| 2        | Water             | 0             | 0           | 0      | 0           | 0.003  | 0     | 0       | 0         | 0       | 0        | 0.003     | 0     | 0.001 |
| 3        | Salt              | 0             | 0           | 0      | 0           | 38.758 | 0     | 0       | 0         | 0       | 0        | 0.024     | 0     | 0.008 |
| 4        | Bread Flour       | 361           | 1.7         | 0.2    | 0           | 0.002  | 72.5  | 2.4     | 0.3       | 12      | 0        | 0.015     | 0.004 | 0.1   |
| 5        | Butter            | 717           | 81.1        | 51.4   | 0.215       | 0.576  | 0.1   | 0       | 0.1       | 0.9     | 0.000056 | 0.024     | 0     | 0.024 |
| 6        | Sugar             | 375           | 0           | 0      | 0           | 0      | 100   | 0       | 100       | 0       | 0        | 0         | 0     | 0     |
| 7        | Egg               | 143           | 9.9         | 3.1    | 0.372       | 0.14   | 0.8   | 0       | 0.8       | 12.6    | 0.000035 | 0.053     | 0.002 | 0.134 |
| 8        | Dry Milk          | 496           | 26.7        | 16.7   | 0.097       | 0.371  | 38.4  | 0       | 38.4      | 26.3    | 0.000312 | 0.912     | 0     | 1.33  |
| 9        | Wheat Flour       | 364           | 1           | 0.2    | 0           | 0.002  | 76.3  | 2.7     | 0.3       | 10.3    | 0        | 0.015     | 0.005 | 0.107 |
| 10       | Vegetable Oil     | 884           | 100         | 7.4    | 0           | 0      | 0     | 0       | 0         | 0       | 0        | 0         | 0     | 0     |
| 11       | Olive Oil         | 800           | 93.3        | 13.3   | 0           | 0      | 0     | 0       | 0         | 0       | 0        | 0         | 0     | 0     |
| 12       | Honey             | 304           | 0           | 0      | 0           | 0.004  | 82.4  | 0.2     | 82.1      | 0.3     | 0        | 0.006     | 0     | 0.052 |
| 13       | Brown Sugar       | 380           | 0           | 0      | 0           | 0.028  | 98.1  | 0       | 97        | 0.1     | 0        | 0.083     | 0.001 | 0.133 |
| 14       | All-Purpose Flour | 364           | 1           | 0.2    | 0           | 0.002  | 76.3  | 2.7     | 0.3       | 10.3    | 0        | 0.015     | 0.005 | 0.107 |
| 15       | Milk              | 50            | 2.1         | 1.2    | 0.008       | 0.047  | 4.9   | 0       | 4.5       | 3.3     | 0.000001 | 0.119     | 0     | 0.057 |

When processed through our network, would be able to replicate a recipe such as this:


|   | Recipe                    | Bread flour | Water | Butter | Sugar | Salt | Dry milk | Active dry yeast | Egg | Whole wheat flour | Vegetable oil | Olive oil | Honey | Brown sugar | All-purpose flour | Milk |
|---|---------------------------|-------------|-------|--------|-------|------|----------|------------------|-----|-------------------|---------------|-----------|-------|-------------|-------------------|------|
| 1 | "Traditional White Bread" | 408         | 236   | 14     | 12.6  | 8.6  | 8.48     | 5.6              | 0   | 0                 | 0             | 0         | 0     | 0           | 0                 | 0    |

![Nutrients](/Project_Demo_Folder/images/breadnutrients.png)

# 🢃

![Ingredients](/Project_Demo_Folder/images/breadingredients.png)

## Running our Demo

1. You will need Python 3.0 or higher. This can be found on the Python website [here](https://www.python.org/downloads/)
2. Our project is written in .ipynb files that require Jupyter Notebook [(Install here)](https://jupyter.org/install) to run.
3. Once inside Jupyter Notebook, a few tools will need to be imported to run a demo:

```
import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import matplotlib.pyplot as plt
import csv

from Generator import Generator
from RealData import RealData

from IPython.display import Image
```

## Companion Files

We used a website to convert our ingredients to their relative nutrient values which yielded these results [here](main/nutrients.csv).

We wrote a generator to generate random recipes for testing, but we also used a small list of [real recipes](main/Recipe_Data.csv) as well

## Let's Run the Demo!

[Run the demo in Jupyter hub](Project_Demo_Folder/Project%20Demo.ipynb)
