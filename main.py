import json
import csv

def jsonl_validator(f_jsonl) :
    first_line = f_jsonl.readline()
    
    if not first_line :
        raise ValueError("Json file is empty!")
    
    return first_line

def jsonl_to_csv(jsonl_file, csv_file) :
    with open(jsonl_file, 'r') as f_jsonl, open(csv_file, 'w', newline='') as f_csv:
        first_line = jsonl_validator(f_jsonl=f_jsonl)
        data = json.loads(first_line)
        fieldnames = data.keys()
        
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)
        
        for line in f_jsonl:
            data = json.loads(line)
            writer.writerow(data)

def csv_to_jsonl(csv_file, jsonl_file):
    with open(csv_file, 'r') as f_csv, open(jsonl_file, 'w') as f_jsonl:
        reader = csv.DictReader(f_csv)
        
        for row in reader:
            json_record = {}
            for key, value in row.items():
                json_record[key] = value
            
            f_jsonl.write(json.dumps(json_record) + '\n')

if __name__ == '__main__':

    jsonl_file = 'data.jsonl'
    csv_file = 'data.csv'

    # jsonl_to_csv(jsonl_file, csv_file)
    csv_to_jsonl(csv_file, jsonl_file)
        