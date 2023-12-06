#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os
from flask import Flask, jsonify

import rt.regis
rt.regis.module_registry(".modules.sqlx")

from route.user import user_bp
from route.admin import admin_bp

# # just for testing
from utils import run_query
from schema.schema import *

def create_app():
    app = Flask(__name__)

    blueprints = [ user_bp , admin_bp]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app

app = create_app()

@app.after_request
def apply_caching(request):

    request.headers["Access-Control-Allow-Origin"] = "*"
    request.headers["Access-Control-Allow-Headers"] = "Authentication, Content-Type, Content-Length, Content-Encoding, Content-Language, Content-Location"
    # request.headers["Access-Control-Allow-Headers"] = "Content-Type, Content-Length, Content-Encoding, Content-Language, Content-Location, Content-Range, Content-Security-Policy, Content-Security-Policy-Report-Only"
    request.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, UPDATE, DELETE"
    request.headers["Access-Control-Max-Age"] = "86400"
    return request

@app.route("/")
def test():
    try:
        """ RECREATE TABLES """
        # all_table = ["orders", "carts", "products", "categories", "users", "banners"]
        # all_table = ["orders", "carts", "products", "categories", "users"]
        # drop_table(all_table)

        # recreate_table_users(call_engine())
        # print("FINISHED USERS")
        # recreate_table_categories(call_engine())
        # print("FINISHED CATEGORIES")
        # recreate_table_products(call_engine())
        # print("FINISHED PRODUCTS")
        # recreate_table_carts(call_engine())
        # print("FINISHED CARTS")
        # recreate_table_orders(call_engine())
        # print("FINISHED ORDERS")
        # recreate_table_banners(call_engine())
        # print("FINISHED BANNER")

        if run_query("SELECT * FROM test")[0]['name'] == "CONNECTED":
            return jsonify({"message": "Server Online"}), 200
    except:
        return jsonify({"message": "Server Offline"}), 404
