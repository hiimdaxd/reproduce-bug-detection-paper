from crawler import *
from handler import *
from preprocess import *

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

# if __name__ == '__main__':
#     preprocess_and_encode()