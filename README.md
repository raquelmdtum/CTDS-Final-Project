## Introduction

This is code for **similar items** based on the **Jaccard Similarity** for the project where we are using [Sephora dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data) to find *dupes* for an item. 

## Idea

First we clean the dataset using the **data.ipynb** notebook. The result of that will be *data/skincare.cvs* file that only contains skincare products.

Now we perform ***similar items search*** based on the **Jaccard Similarity** by simply running in console:

```
python similar_items.py
```

We are then asked to input the *produc_id* for desired dupe. Based on that we do following steps:

1. Get the product info based on the *produc_id*
2. Find the products that have the same category as that products (clusstering?)
3. Perform ***similar items search*** based on the **Jaccard Similarity** using highlights column
4. Print names and the ranking of the most simlar product that have the same secondary_category
