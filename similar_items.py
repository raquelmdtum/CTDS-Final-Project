# this file consists of the code used for similar items

import pandas as pd

def jaccard_similarity(set_a, set_b):
   """
   Calculate the Jaccard Similarity between two sets.
   """
   intersection = len(set_a.intersection(set_b))
   union = len(set_a.union(set_b))
   return intersection / union if union != 0 else 0.0

def similarity_search(df, token_list):
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
   similarity_df = pd.DataFrame(similarity_scores, columns=['product_id', 'product_name', 'similarity_score', 'highlights'])
   
   # Sort the DataFrame by the 'similarity_score' column in descending order
   similarity_df_sorted = similarity_df.sort_values(by='similarity_score', ascending=False).reset_index(drop=True)
   
   return similarity_df_sorted

if __name__ == "__main__":
   """
   Input the product_id to get the most similar items based on Jaccard Similarity between highlight column
   """
   
   product_id_input = input("Enter the product_id: ")

   # Code you want to run when the script is executed directly
   print("Running similarity search...")
   
   # load the data
   df = pd.read_csv("data/skincare.csv")
   
   # get the selected product
   product = df[df['product_id'] == product_id_input]
   
   # get the product category and highlights
   product_category = product['secondary_category'].values[0]
   token_list = list(df[df['product_id'] == product_id_input]['highlights'])[0].split(", ")

   # get only the products that have the same secondary_category as the selected product, and remove the product I am searching for
   category_df = df[(df['secondary_category'] == product_category) & (df['product_id'] != product_id_input)][['product_id','product_name', 'highlights']]
   
   # perform similarity search using Jaccard Similarity
   similarity_results_sorted = similarity_search(category_df, token_list)
   
   print(similarity_results_sorted)
   