from settings import *
import json

db = SQLAlchemy(app)

class Fee_Tracker(db.Model):
    
    __tablename__= 'tracker'
    id = db.Column(db.Integer, primary_key = True)
    First_Name = db.Column(db.String(20), nullable = False)
    Last_Name = db.Column(db.String(20), nullable = False)
    DOB = db.Column(db.String(), nullable = False)
    Amount_Due = db.Column(db.Integer(), nullable = False)
    
    def json(self):
        
        return {'Student ID': self.id, 
                'First Name': self.First_Name, 
                'Last Name': self.Last_Name, 
                'Date of Birth': self.DOB,
                'Amount Due': self.Amount_Due}
        
    def add_record(_firstname, _lastname, _dob, _amountdue):
        
        new_record = Fee_Tracker(First_Name = _firstname, 
                                 Last_Name = _lastname, 
                                 DOB = _dob, 
                                 Amount_Due = _amountdue)
        db.session.add(new_record)
        db.session.commit()
        
    def get_all_records():
        
        return [Fee_Tracker.json(record) for record in Fee_Tracker.query.all()]

    def get_recordby_id(_byid):
        
        return [Fee_Tracker.json(Fee_Tracker.query.filter_by(id = _byid).first())]

    def update_record(_id, _firstname, _lastname, _dob, _amountdue):
        
        record_to_update = Fee_Tracker.query.filter_by(id = _id).first()
        record_to_update.First_Name = _firstname
        record_to_update.Last_Name = _lastname
        record_to_update.DOB = _dob
        record_to_update.Amount_Due = _amountdue
        db.session.commit()
        
    def delete_record(_id):
        
        Fee_Tracker.query.filter_by(id = _id).delete()
        db.session.commit()