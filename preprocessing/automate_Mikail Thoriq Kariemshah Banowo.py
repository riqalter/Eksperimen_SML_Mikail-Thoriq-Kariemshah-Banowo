import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import argparse

def preprocess_data(input_path: str, output_path: str):
    """
    Load raw dataset, apply preprocessing steps,
    and save processed dataset.
    """
    print(f"Loading data from {input_path}...")
    df = pd.read_csv(input_path)
    
    # --- Preprocessing Steps (Matching Notebook) ---
    
    # 1. Handling missing values
    print("Handling missing values...")
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].mean())
    if 'Embarked' in df.columns:
        df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
        
    # 2. Drop columns
    print("Dropping columns...")
    cols_to_drop = ['Cabin', 'Name', 'Ticket', 'PassengerId']
    existing_cols_to_drop = [c for c in cols_to_drop if c in df.columns]
    df = df.drop(columns=existing_cols_to_drop)
    
    # 3. Encoding categorical features
    print("Encoding categorical features...")
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)
    
    # 4. Feature Scaling AND Splitting Target (Logic from notebook)
    # Note: In the notebook we split X and y, then scaled X. 
    # For the automation script output, we usually want the full processed dataset ready for training.
    
    target_col = 'Survived'
    if target_col in df.columns:
        y = df[target_col]
        X = df.drop(target_col, axis=1)
        
        # Scaling numerical features
        print("Scaling numerical features...")
        scaler = StandardScaler()
        # Ensure Age and Fare exist before scaling
        scale_cols = ['Age', 'Fare']
        existing_scale_cols = [c for c in scale_cols if c in X.columns]
        
        if existing_scale_cols:
            X[existing_scale_cols] = scaler.fit_transform(X[existing_scale_cols])
            
        # Recombine for saving
        processed_df = pd.concat([y, X], axis=1)
    else:
        # If no target (e.g. inference), just scale
        print("Target column not found, preprocessing features only...")
        X = df
        scale_cols = ['Age', 'Fare']
        existing_scale_cols = [c for c in scale_cols if c in X.columns]
        if existing_scale_cols:
            X[existing_scale_cols] = scaler.fit_transform(X[existing_scale_cols])
        processed_df = X

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Saving processed data to {output_path}...")
    processed_df.to_csv(output_path, index=False)
    print("Done.")

if __name__ == "__main__":
    # Example usage or argument parsing
    # Default paths based on project structure
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, 'titanic_raw', 'titanic.csv')
    output_file = os.path.join(base_dir, 'preprocessing', 'titanic_preprocessing', 'train_processed.csv')
    
    preprocess_data(input_file, output_file)
