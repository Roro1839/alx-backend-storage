#!/usr/bin/env python3
""" 101-students """

def top_students(mongo_collection):
    average_score = calculate_average_score(score)
    return (mongo_collection.find().sort({score:1}), average_score)
