from models import Review, DoesNotExist
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

# ==============================
# 					BLUEPRINT
# ==============================

reviews = Blueprint('reviews', 'reviews')

# ==============================
# 						ROUTES
# ==============================

# Index
@reviews.route('/', methods=['GET'])
def reviews_index():
	reviews_dicts = [model_to_dict(review) for review in Review]
	return jsonify(
			data=reviews_dicts,
			message=f'Successfully retrieved {len(reviews_dicts)} reviews',
			status=200
		), 200