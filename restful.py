from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

# A list of dictionaries that will be used as my json database for this project
languages = [{'name':'JavaScript'}, {'name':'Python'}, {'name':'Ruby'}, {'name':'Go'}]

# Test GET just to see if the application is running
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works!'})

# GET method to return all languages in our list
@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})

# GET method to get a single language in our list
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

# POST method to add a language to our list
@app.route('/lang', methods=['POST'])
def addOne():
    language = {'name' : request.json['name']}

    languages.append(language)
    return jsonify({'languages' : languages})

# PUT method to update the data on a language of our list
@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']

    return jsonify({'language': langs[0]})

# DELETE method to remove an entry from our languages list
@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])

    return jsonify({'languages' : languages})

if(__name__) == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode