from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from crawler import fetch_review_data

def process_judge_data_with_threads(judge_ids: list, num_threads=100):
    print(f'In progress of handling judge data with {num_threads} threads')
    src_list = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_judge = {executor.submit(fetch_review_data, judge['judgeId'], judge['status']): judge for judge in judge_ids}
        for future in as_completed(future_to_judge):
            judge = future_to_judge[future]
            try:
                data = future.result()
                if data:
                    src_list.append(data)
            except Exception as exc:
                print(f'Judge ID {judge["judgeId"]} generated an exception: {exc}')
    print(f'Handling judge data: Done!')
    return src_list

def save_to_json(src_list, file_name='raw_data.json'):
    print('In progress of saving into raw_data.json file')
    with open(file_name, 'w') as f:
        json.dump(src_list, f, indent=2)
    print('Done')
    
