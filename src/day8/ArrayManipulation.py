import numpy as np

data = np.arange(24)

reshaped_data = data.reshape(4, 3, 2)

final_data = reshaped_data.transpose(0, 2, 1)

print("Final shape:", final_data.shape)
print("Final array:\n", final_data)
