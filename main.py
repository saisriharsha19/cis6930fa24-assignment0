import requests
import argparse
import sys

def fetch_data_from_api(page):
    """Fetch data from the FBI API with the given page number."""
    url = f"https://api.fbi.gov/wanted/v1/list?page={page}"
    resp = requests.get(url)
    resp.raise_for_status()  
    return resp.json()

def process_data(data):
    """Process the input data and return a thorn-separated output string."""
    lines = []
    for item in data.get('items', []):
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

def main(page=None):
    """Main function to fetch, process, and print the data in a specified format."""
    if page is not None:
        data = fetch_data_from_api(page)
    else:
        print("Error: No valid input source provided, please provide a valid page number", file=sys.stderr)
        sys.exit(1)

    formatted_data = process_data(data)
    print(formatted_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--page", type=int, help="Provide the page number you want to have output for!!")
    args = parser.parse_args()
    
    args = parser.parse_args()
    if args.page is not None:
        main(page=args.page)
    else:
        parser.print_help(sys.stderr)
        sys.exit(1)
