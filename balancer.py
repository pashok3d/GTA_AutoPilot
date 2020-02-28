#libraries
import numpy as np
import pandas as pd
from collections import Counter

data = np.load('training_data.npy')
df = pd.DataFrame(data)
print(Counter(df[1].apply(str)))