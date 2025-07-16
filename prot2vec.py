import pandas as pd
import numpy as np

# Load ProtVec embeddings safely
protvec_df = pd.read_csv('protVec_100d_3grams.csv', header=0, sep=r'\s+')

# Create lookup dictionary
protvec_dict = {}
for _, row in protvec_df.iterrows():
    try:
        trigram = row['words']
        vec = row.iloc[1:].to_numpy(dtype=np.float32)
        protvec_dict[trigram] = vec
    except ValueError:
        print(f"Skipping trigram {trigram} due to conversion error")

# Function to get ProtVec embedding for a sequence
def get_protvec_embedding(seq):
    vecs = []
    for i in range(len(seq)-2):
        tri = seq[i:i+3]
        if tri in protvec_dict:
            vecs.append(protvec_dict[tri])
    if vecs:
        return np.mean(vecs, axis=0)
    else:
        return np.zeros(100, dtype=np.float32)

# # Test
# trigram = 'AAA'
# print(type(protvec_dict[trigram]))
