from surprise import Dataset, Reader
from surprise.model_selection import cross_validate

# Load the data
data = [
    {'user_id': '1', 'item_id': '101', 'rating': 5},
    {'user_id': '1', 'item_id': '102', 'rating': 4},
    {'user_id': '2', 'item_id': '101', 'rating': 4},
    {'user_id': '2', 'item_id': '103', 'rating': 5},
    {'user_id': '3', 'item_id': '104', 'rating': 3},
]

reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_folds([data], reader)

# Evaluate the algorithm
algo = KNNBasic()
cross_validate(algo, dataset, measures=['RMSE', 'MAE'], cv=3, verbose=True)

# Generate recommendations
trainset = dataset.build_full_trainset()
algo.fit(trainset)
for user_id in trainset.global_uiids:
    predictions = algo.predict(user_id, trainset.global_iids)
    for prediction in predictions:
        print(f"User {user_id} would rate item {prediction.iid} {prediction.est} with a {prediction.details['rating_scale']} confidence")
