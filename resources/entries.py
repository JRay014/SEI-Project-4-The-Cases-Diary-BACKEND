import schema

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

entries = Blueprint('entries', 'entries')

# GET ROUTE
@entries.route('/home', methods=['GET'])
def entries_index():
    entry_dicts = [model_to_dict(entry) for entry in schema.Entries.select()]

    return jsonify({
        'data': entry_dicts,
        'message': f"Successfully found {len(entry_dicts)} entries",
        'status': 200,
    }), 200 


# POST ROUTE
@entries.route('/home', methods=['POST'])
def create_entry():
    payload = request.get_json()
    new_entry = schema.Entries.create(title=payload['title'], date=payload['date'], description=payload['description'], decision=payload['decision'], keywords=payload['keywords'])
    print(new_entry)

    entry_dict = model_to_dict(new_entry)

    return jsonify(
        data=entry_dict,
        message='Successfully created entry!',
        status=201,
    ), 201


# SHOW ROUTE
@entries.route('/<id>', methods=["GET"])
def get_one_entry(id):
    entry = schema.Entries.get_by_id(id)

    return jsonify(
        data = model_to_dict(entry),
        message = 'Successful Show!',
        status = 200,
        # seconds = 465465465254
    ), 200


# UPDATE ROUTE
@entries.route('/<id>', methods=["PUT"])
def update_entry(id):
    payload = request.get_json()

    schema.Entries.update(**payload).where(schema.Entries.id==id).execute()

    return jsonify(
        data = model_to_dict(schema.Entries.get_by_id(id)),
        message = 'Entry updated successfully',
        status = 200,
    ), 200


# DELETE ROUTE
@entries.route('/<id>', methods=["DELETE"])
def delete_entry(id):
    schema.Entries.delete().where(schema.Entries.id==id).execute()

    return jsonify(
        data = None,
        message = 'Entry deleted successfully',
        status = 200,
    ), 200