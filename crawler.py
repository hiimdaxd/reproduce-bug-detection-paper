import requests
from constants import *

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f'Failed to fetch data from {api_url}\nStatus code: {response.status_code}')

def get_solutions(problem_id=None):
    if problem_id: 
        solutions_url = f'{BASE_URL}{SOLUTIONS_PATH}/{problem_id}'
    else: 
        solutions_url = DEFAULT_SOLUTION_URL
    return fetch_data(solutions_url)

def get_review(judge_id):
    review_url = f'{BASE_URL}{REVIEWS_PATH}/{judge_id}'
    return fetch_data(review_url)

def fetch_review_data(judge_id, status):
    review = get_review(judge_id)
    if review.get('policy') != 'private':
        if review.get('sourceCode'):
            review_object = {
                'judge_id': judge_id,
                'sourceCode': review.get('sourceCode'),
                'status': status
            }
            return review_object
        else:
            raise TypeError(f'Can\'t find value of sourceCode field in object of judge_id = {judge_id}')
    return None