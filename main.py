import requests
import argparse
import sys
import json

def fetch_data_from_api(page):
    """Fetch data from the FBI API with the given page number."""
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    resp = requests.get(url)
    resp.raise_for_status()  
    return resp.json()

def process_data(data):
    """Process the input data and return a thorn-separated output string."""
    if isinstance(data, dict) and 'items' in data: #for page number argument output
        items = data['items']
    elif isinstance(data, list): #for file location argument output
        items = data  
    else:
        raise ValueError("Unsupported data format")

    lines = []
    for item in items:
        title = item.get('title', "N/A")
        subjects = item.get('subjects', [])
        if not isinstance(subjects, list):
            subjects = [subjects]
        subjects_str = ', '.join(str(subject) for subject in subjects if subject)
        field_offices = item.get('field_offices', [])
        if not isinstance(field_offices, list):
            field_offices = [field_offices]
        field_offices_str = ', '.join(str(office) for office in field_offices if office)
        
        line = f"{title}þ{subjects_str}þ{field_offices_str}"
        lines.append(line)
    
    return "\n".join(lines)

def main(page=None, file=None):
    """Main function to fetch, process, and print the data in a specified format."""
    if page is not None:
        data = fetch_data_from_api(page)
        formatted_data = process_data(data)
        print(formatted_data)
    elif file is not None:
        with open(file, "r", encoding="UTF-8") as data_:
            data = json.load(data_)
        formatted_data = process_data(data)
        print(formatted_data)
    else:
        print("Error: No valid input source provided, please provide a valid page number or a file location", file=sys.stderr)
        sys.exit(1)

    
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--page", type=int, help="Provide the page number you want to have output for!!")
    parser.add_argument("--file", type=str, help="Provide the file location containing the data")
    args = parser.parse_args()
    
    args = parser.parse_args()
    if args.page is not None:
        main(page=args.page)
    elif args.file is not None:
        main(file=args.file)
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)
