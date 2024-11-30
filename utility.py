def preprocess_rules(rules):
   """
   Preprocess the rules DataFrame to ensure 'antecedents' and 'consequents' are sets.
   """
   rules['antecedents'] = rules['antecedents'].apply(lambda x: set(x.split()) if isinstance(x, str) else x)
   rules['consequents'] = rules['consequents'].apply(lambda x: set(x.split()) if isinstance(x, str) else x)
   return rules

# Function to find items associated with an input item
def find_associated_items(input_item, rules):
   """
   Find all items associated with an input item based on association rules.

   Parameters:
      input_item (str): The item to find associations for.
      rules (pd.DataFrame): A DataFrame of association rules with columns 'antecedents' and 'consequents'.

   Returns:
      list: A list of items associated with the input item, preserving the order of rules.
   """
   # Sort rules by confidence in descending order
   rules = rules.sort_values(by='confidence', ascending=False).reset_index(drop=True)

   associated_items = []  # Use a list to preserve order

   # Iterate through the rules
   for _, rule in rules.iterrows():
      antecedents = rule['antecedents']
      consequents = rule['consequents']

      # Check if the input item is in the antecedents
      if input_item in antecedents:
         # Add consequents to the associated items if not already present
         for item in consequents:
               if item not in associated_items:
                  associated_items.append(item)
                  
   return associated_items

