import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from playhouse.shortcuts import model_to_dict

users = Blueprint('users','users')

# REGISTER
@users.route('/register', methods=['POST'])
def register():
    payload = request.get_json()

    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()
    print(payload)

    try:
        models.Users.get(models.Users.email == payload['email'])
        #try for username
        # models.Users.get(models.Users.username == payload['username'])

        return jsonify(
            data={},
            message=f"A user with the email {payload['email']} already exists",
            status=401
        ), 401
    
    except models.DoesNotExist:
        pw_hash = generate_password_hash(payload['password'])

        created_user = models.Users.create(
            username=payload['username'],
            email=payload['email'],
            password=pw_hash
        )
        print(created_user)
        login_user(created_user)

        created_user_dict = model_to_dict(created_user)
        print(created_user_dict)

        created_user_dict.pop('password')

        return jsonify(
            data=created_user_dict,
            message=f"Successfully registered user {created_user_dict['email']}",
            status=201
        ), 201


#LOGIN
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()

    try:
        user = models.Users.get(models.Users.email == payload['email'])

        user_dict = model_to_dict(user)

        password_is_good = check_password_hash(user_dict['password'], payload['password'])
        if (password_is_good):
            login_user(user)

            user_dict.pop('password')

            return jsonify(
                data=user_dict,
                message=f"Successfully logged in {user_dict['email']}",
                status=200
            ), 200

        else:
            print('pw is no good')
            return jsonify(
                data={},
                message="Email or password is incorrect",
                status=401
            ), 401

    except models.DoesNotExist:
        print('username is no good')
        return jsonify(
            data={},
            message="Email or password is incorrect", 
            status=401
        ), 401


# LOGOUT
@users.route('/logout', methods=['GET'])
def logout():
    logout_user()

    return jsonify(
        data={},
        message='User Successfully logout',
        status=200,
    ), 200