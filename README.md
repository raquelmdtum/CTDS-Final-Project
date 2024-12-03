# Recommendation System for Sephora Skincare Products

## Project Overview

This repository contains the implementation of a Recommendation System for Sephora skincare products, leveraging data from the [Sephora dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews/data). The system focuses on recommending products based on customer reviews, frequent itemsets, and product similarity.

The recommendations are designed to suggest products that users are likely to enjoy, based on:
1. Products frequently reviewed together with positive sentiment.
2. Products similar to the recommended items, identified through ingredient and product similarity.

## Project Structure

### Folders

- **`data/`**: Contains raw, unprocessed data files.
    -  `product_info.csv`: Metadata for skincare products.
    - `reviews_0-250.csv`: Raw reviews directly from the Kaggle dataset.
    - Other similar raw review files (`reviews_250-500.csv`, etc.).
- **`processed_data/`**: Contains pre-processed files for use in the analysis.
    - `skincare.csv`: Cleaned dataset of skincare products.
    - `reviews_0-250.csv`: Processed reviews (split for scalability).
    - Other similar processed review files (`reviews_250-500.csv`, etc.).
    - `combined_reviews.csv`: Includes all reviews already processed.
    - `3_star_positive_reviews.csv`: Contains positive reviews identified through sentiment analysis on 3-star product reviews.
    - `association_rules.csv`: Contains product relationship rules generated using the Apriori algorithm, which identifies frequently bought together products by linking antecedents (input products) to consequents (recommended products).

### Files

1. Data Cleaning, Preprocessing and Exploratory Data Analysis (EDA)
- **`data_processing_eda.ipynb`**: Notebook for cleaning and preprocessing the dataset. Includes exploratory data analysis (EDA).
2. **Sentiment Analysis**
- **`sentiment_analysis.ipynb`**: Identifies the sentiment of 3-star reviews to ensure only positive ones are used in recommendation logic.
3. **Frequent Items**
- **`frequent_itemsets.ipynb`**: Implements Apriori algorithm to mine frequent itemsets from positively-rated reviews and generate association rules.
4. **Similar Items**
- **`similar_items.ipynb`**: Recommends similar skincare products based on highlights and ingredients using similarity measures and Reciprocal Rank Fusion.
5. **Recommendation System**
- **`recommender.ipynb`** and **`utility.py`**: Simulate the entire recommendation process using association rules and similarity searches to recommend skincare products.

## How to Use

1. **Run Data Cleaning and Preprocessing:**
- Use `data_processing_eda.ipynb` to clean the dataset and preprocess reviews.
2. **Perform Sentiment Analysis:**
- Run `sentiment_analysis.ipynb` to filter 3-star positive reviews.
3. **Mine Frequent Items:**
- Execute `frequent_itemsets.ipynb` to generate association rules.
4. **Find Similar Items:**
- Use `similar_items.ipynb` to compute the similarity between products.
5. **Generate Recommendations:**
- Combine the frequent itemsets and similarity measures through the `recommender.ipynb` notebook to recommend products.

## Example Workflow

1. Sentiment Filtering: <br />
Input: A dataset of products and reviews. <br />
Output: A refined dataset containing only positively rated products for each user.

2. Association Rules: <br />
Input: Refined dataset of liked products. <br />
Output: Rules like "If you liked Product A, you might also like Product B."

3. Similar Items Search: <br />
Input: A product_id of interest. <br />
Output: Ranked list of similar products.

## Challenges and Considerations
- Sentiment Analysis:
    - Challenges with nuanced language (e.g., "not bad" vs. "I didn’t love this").
    - Tendency for less extreme reviews, making classification more ambiguous.
- Association Rules:
    - Balancing data volume for meaningful yet representative rules.
- Similarity Search:
    - Ensuring "similar items" align with user expectations in both functionality and attributes.

## Future Work
- Enhance sentiment analysis for greater contextual understanding.
- Experiment with additional similarity measures or clustering techniques.
- Integrate hybrid models to improve recommendation quality.
