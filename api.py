from fee_tracker import *

@app.route('/fee_tracker', methods = ['GET'])
def get_all_records():
    
    return jsonify({'Records': Fee_Tracker.get_all_records()})

@app.route('/fee_tracker/<int:id>', methods = ['GET'])
def get_recordby_id(id):
    
    record = Fee_Tracker.get_recordby_id(id)
    return jsonify(record)

@app.route('/fee_tracker', methods = ['POST'])
def add_record():
    
    user_input = request.get_json()
    Fee_Tracker.add_record(user_input["First Name"], 
                           user_input['Last Name'], 
                           user_input['Date of Birth'],
                           user_input['Amount Due'])
    response = Response("Record Added!", 201, mimetype = 'application/json')
    return response

@app.route('/fee_tracker/<int:id>', methods = ['PUT'])
def update_record():
    
    user_input = request.get_json()
    Fee_Tracker.update_record(id,
                              user_input['First Name'],
                              user_input['Last Name'],
                              user_input['Date of Birth'],
                              user_input['Amount Due'])
    response = Response("Record Updated!", status = 200, mimetype = 'application/json')
    return response

@app.route('/fee_tracker/<int:id>', methods = ['DELETE'])
def delete_record():
    
    Fee_Tracker.delete_record(id)
    response = Response("Record Deleted!", status = 200, mimetype = 'application/json')
    return response

if __name__ == '__main__':
    app.run(port = 6497, debug = True)