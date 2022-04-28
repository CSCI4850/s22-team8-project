# s22-team8-project

## Team #8 - (Insert Our Name here when we think of a good one)


This neural network is designed to take in bread recipies and their macro and micronutrients, such as those off of a nutritional facts label, and the network will return the masses of each ingredient (in grams) in descending order. For example:

![Nutrients](/Project_Demo_Folder/images/breadnutrients.png)

# 🢃

![Ingredients](/Project_Demo_Folder/images/breadingredients.png)

## Running our Demo

1. You will need Python 3.0 or higher. This can be found on the Python website [here](https://www.python.org/downloads/)
2. Our project is written in .ipynb files that require Jupyter Notebook [(Install here)](https://jupyter.org/install) to run.
3. A few tools will need to be imported to run a demo:

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

Using a website to convert our ingredients to their relative nutrient values yielded these results [here](main/nutrients.csv).

We wrote a generator to generate random recipes for testing, but we also used a small list of [real recipes](main/Recipe_Data.csv) as well
