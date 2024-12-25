training_data = [
    {"item": "Pepper","category":"vegetables"},
    {"item":"broccoli","category":"vegetables"},
    {"item":"cabbage","category":"vegetables"},
    {"item":"carrot","category":"vegetables"},
    {"item":"eggs","category":"groceries"},
    {"item":"milk","category":"groceries"},
    {"item":"bread","category":"groceries"},
    {"item":"cereal","category":"groceries"}
]

#Step 2 : Define a function to train model

def train_model(data):
    categories={}
    for entity in data:
        item = entity["item"].lower()
        category = entity["category"]
        categories[item] = category
    return categories

#Step 3 : Train the model

model = train_model(training_data)

#Step 4 : test the model with new data

test_data = ["pepper","milk","carrot","bread","unknown_item"]
print("\nClassifiation Results")
for test_item in test_data:
    category = model.get(test_item.lower(),"unknown")
    print(f"Item: {test_item}, classified as :{category}")