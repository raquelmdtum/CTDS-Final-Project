# this file consists of the code used for similar items

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def jaccard_similarity(set_a, set_b):
   """
   Calculate the Jaccard Similarity between two sets.
   """
   intersection = len(set_a.intersection(set_b))
   union = len(set_a.union(set_b))
   return intersection / union if union != 0 else 0.0

def similarity_search_highlights(df, token_list):
   """
   Perform similarity search based on Jaccard similarity between df and a token list.
   
   :param df: A pandas DataFrame with columns ['product_id','product_name', 'highlights'].
   :param token_list: A list of tokens to compare against (highlights).
   :return: A DataFrame with IDs and their Jaccard similarity scores, sorted by similarity score.
   """
   # Convert the token list to a set
   token_set = set(token_list)
   
   # List to store the similarity scores
   similarity_scores = []
   
   # Iterate over the rows of the DataFrame
   for index, row in df.iterrows():
      product_id = row['product_id']
      title = row['product_name']
      # Convert the tokens for this ID to a set (assumed to be a string)
      id_token_set = set(row['highlights'].split(", "))
      
      # Calculate Jaccard similarity
      similarity_score = jaccard_similarity(id_token_set, token_set)
      
      # Append the result as a tuple (id, score)
      similarity_scores.append((product_id, title, similarity_score, (row['highlights'])))
   
   # Convert the list of similarity scores to a DataFrame
   similarity_df = pd.DataFrame(similarity_scores, columns=['product_id', 'product_name', 'similarity_score_highlights', 'highlights'])
   
   # Sort the DataFrame by the 'similarity_score' column in descending order
   similarity_df_sorted = similarity_df.sort_values(by='similarity_score_highlights', ascending=False).reset_index(drop=True)
   
   similarity_df_sorted['rank_highlights'] = range(1, len(similarity_df_sorted) + 1)
   
   return similarity_df_sorted

def custom_tokenizer(text):
   return text.split(", ")

def similarity_search_ingredients(query, df):
   """
   Perform a similarity search based on cosine similarity of TF-IDF vectors.

   Parameters:
   - query (str): The input query string.
   - df (pd.DataFrame): A DataFrame containing 'id' and 'ingredients' columns.

   Returns:
   - results_df (pd.DataFrame): Rows from the original DataFrame sorted by similarity.
   """
   # Initialize TfidfVectorizer with a custom tokenizer (adjust lowercase as needed)
   vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, lowercase=False)

   # Extract the 'ingredients' column
   ingredients = df['ingredients']

   # Fit and transform the ingredients
   tfidf_matrix = vectorizer.fit_transform(ingredients)

   # Transform the query into the TF-IDF space
   query_tfidf = vectorizer.transform([query])

   # Compute cosine similarity between the query and all documents
   similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

   # Add similarity scores to the DataFrame
   df['similarity_score_ingredients'] = similarities

   # Sort the DataFrame by similarity scores in descending order
   results_df = df.sort_values(by='similarity_score_ingredients', ascending=False).reset_index(drop=True)
   
   results_df['rank_ingredients'] = range(1, len(results_df) + 1)

   return results_df

def reciprocal_rank_fusion(df_highlights, df_ingredients, k=60):
   """
   Compute Reciprocal Rank Fusion (RRF) scores based on rank_highlights and rank_ingredients.

   Parameters:
   - df_highlights (pd.DataFrame): DataFrame containing 'product_id', 'rank_highlights', and other relevant columns.
   - df_ingredients (pd.DataFrame): DataFrame containing 'product_id', 'rank_ingredients', and other relevant columns.
   - k (int): A constant for RRF computation (default=60).

   Returns:
   - combined_df (pd.DataFrame): A new DataFrame with overall RRF scores and combined ranking.
   """
   # Merge the two DataFrames on 'product_id'
   merged_df = pd.merge(
      df_highlights[['product_id', 'rank_highlights']],
      df_ingredients[['product_id', 'rank_ingredients']],
      on='product_id',
      how='outer'
   )

   # Fill missing ranks with a large value (e.g., very low relevance)
   merged_df['rank_highlights'] = merged_df['rank_highlights'].fillna(float('inf'))
   merged_df['rank_ingredients'] = merged_df['rank_ingredients'].fillna(float('inf'))

   # Compute the RRF score
   merged_df['rrf_score'] = (
      1 / (k + merged_df['rank_highlights']) +
      1 / (k + merged_df['rank_ingredients'])
   )

   # Sort by the RRF score in descending order
   merged_df = merged_df.sort_values(by='rrf_score', ascending=False).reset_index(drop=True)

   # Add a new rank based on the RRF score
   merged_df['overall_rank'] = range(1, len(merged_df) + 1)

   return merged_df


if __name__ == "__main__":
   """
   Input the product_id to get the most similar items based on Jaccard Similarity between highlight column
   """
   
   product_id_input = input("Enter the product_id: ")

   # Code you want to run when the script is executed directly
   print("Running similarity search...")
   
   # load the data
   df = pd.read_csv("processed_data/skincare.csv")
   
   # get the selected product
   product = df[df['product_id'] == product_id_input]
   
   # get the product category and highlights
   product_category = product['secondary_category'].values[0]
   token_list = list(df[df['product_id'] == product_id_input]['highlights'])[0].split(", ")

   # get only the products that have the same secondary_category as the selected product, and remove the product I am searching for
   category_df = df[(df['secondary_category'] == product_category) & (df['product_id'] != product_id_input)][['product_id','product_name', 'highlights']]
   
   # perform similarity search using Jaccard Similarity
   similarity_results_sorted = similarity_search_highlights(category_df, token_list)
   
   print(similarity_results_sorted)
   