from sklearn.linear_model import LinearRegression

# Create a new DataFrame with just the math and reading scores
X = df[['reading_score']]
y = df['math_score']

# Fit a linear regression model to the data
model = LinearRegression()
model.fit(X, y)

# Display the coefficients of the model
print('Coefficients:', model.coef_)

# Make predictions on new data
X_new = [[70], [80], [90]]
y_pred = model.predict(X_new)
print('Predictions:', y_pred)
