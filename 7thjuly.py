from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
y_true = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5,  0.0, 2.0, 8.0]
mse = mean_squared_error(y_true, y_pred)
print("MSE:", mse)
rmse = np.sqrt(mse)
print("RMSE:", rmse)
mae = mean_absolute_error(y_true, y_pred)
print("MAE:", mae)