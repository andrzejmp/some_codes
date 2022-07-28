from flask import Flask, jsonify, request, render_template
app = Flask(__name__)

stores = [

{
    'name'  : 'Alfa',
    'items' : [
        {
            'name': 'this item',
            'price': 99.99
        },
        {
            'name': 'the old item',
            'price': 12.01
        }
    ]
},
{
    'name'  : 'Beta',
    'items' : [
        {
            'name': 'toto',
            'price': 23.50
        },
        {
            'name': 'nico',
            'price': 100.00
        }
    ]
}
    
]



@app.route('/')
def hello():
    #return render_template('index.html')
    return render_template('index.html')

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)



#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item  {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request_data.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})
   


app.run(debug=True)
