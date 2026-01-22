import pandas as pd
from sklearn.linear_model import LinearRegression
from menu_app.models import Orderrr

def train_model():
    # Fetch data from DB
    data = Orderrr.objects.all().values()
    df = pd.DataFrame(data)

    # Convert date to number
    df['date'] = pd.to_datetime(df['date'])
    df['day_number'] = df['date'].dt.dayofyear

    models = {}

    # Train model for each item
    for item in df['item_name'].unique():
        item_df = df[df['item_name'] == item]

        X = item_df[['day_number']]
        y = item_df['quantity']

        model = LinearRegression()
        model.fit(X, y)
        models[item] = model

    return models


def predict_tomorrow():
    models = train_model()

    # Predict for next day
    import datetime
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    next_day_no = tomorrow.timetuple().tm_yday

    predictions = {}

    for item, model in models.items():
        pred = model.predict([[next_day_no]])
        predictions[item] = int(pred[0])

    return predictions
