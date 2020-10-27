import json

file_patch = 'raw_lessions.json'

def parser(file_patch):

    with open(file_patch, encoding='utf8') as file:
        json_data = json.load(file)
        
    return json_data

if __name__ == "__main__":
    
    json_data = parser(file_patch)

    lessions = [
        {
            'id': lession['id'],
            'group': lession['group'],
            'teacher': lession['teacher'],
            'lecture': lession['lecture'],
            'date': lession['date'],
            'time': lession['time'],
            } 
        for lession in json_data 
        if lession.get('id', 0)]

    with open('lessions.json', 'w', encoding='utf8') as file:
        json.dumps(lessions, file)