from crawler import *
from handler import *
from preprocess import *
from lexer import *

def get_raw_data():
    solutions_data = get_solutions()
    judge_ids = [
        { 
            'judgeId': solution.get('judgeId'), 
            'status': solution.get('status')
        }
        for solution in solutions_data 
        if solution.get('language') == 'C++'
    ]
    source_code_with_status_list = process_judge_data_with_threads(judge_ids)
    save_to_json(source_code_with_status_list)

if __name__ == '__main__':
    with open('preprocess_data.json', 'r') as file:
        data = json.load(file)
    
    for item in data:
        source_code = item['sourceCode']
        if (source_code):
            # tokens = 
        # else: 
        #     raise ValueError('Cannot get the value of sourceCode field at judgeId ', item['judgeId'])
        