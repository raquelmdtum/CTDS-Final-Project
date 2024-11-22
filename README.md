# Product Recommendation System: README

## Introduction

This repository contains code for a **similar items** search based on **Jaccard Similarity**, as part of a project to identify product recommendations in the [Sephora Skincare Dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data). By leveraging product attributes, we aim to find alternative options for any given product in the dataset.

---

## Project Overview

This project combines sentiment analysis, association rule mining, and similarity search techniques to develop a hybrid recommendation system. The system helps identify related products and suggests alternatives for skincare items.

---

## Key Components

### 1. **Sentiment Analysis to Refine Data**
- **Goal**: Filter out products users didn’t like, focusing on items they enjoyed.  
- **Steps**:
  1. Remove all one- and two-star reviews (negative sentiment).
  2. Perform sentiment analysis on three-star reviews to classify them as positive or negative.  
- **Purpose**: Refine the data to generate association rules that reflect *"if you liked this, you might also like this"* instead of *"if you bought this, you might also buy this."*

### 2. **Association Rule Mining with the A-Priori Algorithm**
- **Goal**: Identify patterns of co-purchased or co-liked products.  
- **Method**: Use the A-Priori algorithm to generate association rules that recommend related products.
- **Challenge**: Balancing dataset size to ensure rules are both meaningful and representative.

### 3. **Similar Items Search Using Jaccard Similarity**
- **Goal**: Recommend "dupes" based on similarity in product attributes, even when association rules are unavailable.
- **Steps**:
  1. Clean the dataset using the `data.ipynb` notebook, producing a refined `data/skincare.csv` file with only skincare products.
  2. Run the `similar_items.py` script and input the `product_id` of the desired item:
     ```bash
     python similar_items.py
     ```
  3. For the selected product:
     - Retrieve its details.
     - Filter products within the same category (clustering).
     - Compute **Jaccard Similarity** using the `highlights` column.
     - Rank and display the most similar products within the same `secondary_category`.

---

## Applications
1. **E-Commerce Recommendations**:
   - Suggest related products or dupes based on association rules and similarity measures.
2. **Product Discovery**:
   - Help users find affordable or similar alternatives to popular products.

---

## Example Workflow

1. **Sentiment Filtering**:  
   Input: A dataset of products and reviews.  
   Output: A refined dataset containing only positively rated products for each user.  

2. **Association Rules**:  
   Input: Refined dataset of liked products.  
   Output: Rules like *"If you liked Product A, you might also like Product B."*  

3. **Similar Items Search**:  
   Input: A `product_id` of interest.  
   Output: Ranked list of similar products within the same category.  

---

## Challenges and Considerations
- **Sentiment Analysis**:
  - Challenges with nuanced language (e.g., *"not bad"* vs. *"I didn’t love this"*).
  - Tendency for less extreme reviews, making classification more ambiguous.
- **Association Rules**:
  - Balancing data volume for meaningful yet representative rules.
- **Similarity Search**:
  - Ensuring "similar items" align with user expectations in both functionality and attributes.

---

## Future Work
- Enhance sentiment analysis for greater contextual understanding.
- Experiment with additional similarity measures or clustering techniques.
- Integrate hybrid models to improve recommendation quality.
