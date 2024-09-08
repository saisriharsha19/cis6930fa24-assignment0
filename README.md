# Name: Sai Sri Harsha Guddati

# Assignment Description 

1. Downloading non-empty data from a URL
2. Extrating title field from FBI API
3. Extrating subjects field from FBI API
4. Extrating field_offices field from FBI API
5. Printing the full thorn separated file.

The assignment task is to fetch non-empty data from an FBI API using the link https://api.fbi.gov/wanted/v1/list?page={2} where the page specifies the page number in the FBI file which the data needs to be fetched. After fetching the data, we need to process(Clean) it to show only the required fileds such as title, subjects and filed_offices seperated by thorn character and print them to the standard output. We need to make sure that if there are multiple strings in a filed, we need to seperate them using commas. After printing the desired output, we need to test our files(functions) if they are working as expected. For testing these functions, we need to use pytest module in Python. The code should be clean and easy to read, for this we need to chunk or seperate our code into functions for better readability, understandability and security of the developed code. There is another aspect in this assignment which is creating a README file, which helps new users or people who will be working on this code to be better understandable.

# How to install
pipenv install -e .

## How to run

## To run the Code with file or page arguments

### page argument is for fetching the data using the page number.

    pipenv run python main.py --page <integer>

### file argument is for directly using the file which we already have.
    
    pipenv run python main.py --file <file-location>
   
## pipenv is used to run the python code in a seperate environment, which is dofferent from the local one. (Running the code in an isolated environment).


## For testing the code

### To run the test files in the /tests/ folder

    pipenv run python -m pytest -v
   
## Here pytest is a module in python which can be used for testing the python code in different scenarios.

## Example Output(optional)

NAJI SHARIFI ZINDASHTI † Counterintelligence, Iran † elpaso, minneapolis
REZA HAMIDI RAVARI † Seeking Information - Terrorism, Iran † elpaso, minneapolis
BORIS YAKOVLEVICH LIVSHITS † Counterintelligence † newyork
JESUS DE LA CRUZ - LYNN, MASSACHUSETTS † ViCAP Missing Persons † N/A
AARON PAUL VICTORY † Additional Violent Crimes † oklahomacity
IDA DEAN (RICHARDSON) ANDERSON - ANN ARBOR, MICHIGAN † ViCAP Missing Persons † N/A
HUYEN TRANG TEMPLE - ARSON † Seeking Information † houston
BRYAN MATTHEW MCGEHRIN - TANEYTOWN, MARYLAND † ViCAP Missing Persons † N/A
MITCHELL TODD HEIN - INDIO, CALIFORNIA † ViCAP Missing Persons † N/A
ELSIE ELDORA LUSCIER † Kidnappings and Missing Persons, Indian Country † seattle
JOHN DOE - WATERLOO TOWNSHIP, MICHIGAN † ViCAP Unidentified Persons † N/A
ATRAYA BERARDI - ROCKLEDGE, FLORIDA †  † N/A
KOA KAI BERNSTEIN † Kidnappings and Missing Persons † honolulu
RODOLFO MANTILLA † Criminal Enterprise Investigations † miami
RANDY STEWART DORAN - NEW ORLEANS, LOUISIANA † ViCAP Missing Persons † N/A
DHULFIQAR KAREEM MSEER † Seeking Information † portland
FREDERICK ARIAS † White-Collar Crime † phoenix
DARASY S. CHHIM † Criminal Enterprise Investigations † boston
JAMES S. RULAND - NORTH FOND du LAC, WISCONSIN † ViCAP Missing Persons † N/A
MARY JOHNSON (DAVIS) † Kidnappings and Missing Persons, Indian Country † seattle
KEVIN BRAME † Seeking Information † cincinnati
BRANDON LEE WAGONER † Seeking Information † charlotte
EDWIN ERNESTO CEDILLOS-RODRIGUEZ † Criminal Enterprise Investigations † N/A
ISIAH TERRELL BILLY † Seeking Information, Indian Country, Navajo † albuquerque
SALOME FLORES APODACA † Criminal Enterprise Investigations † washingtondc


# Functions

## main.py
main.py
Essentially the main.py file contains three functions namely the main function, fetch_data_from_api() and process_data().

fetch_data_from_api(page):

### The below function fetches data from the FBI API for the specified page number. This function makes an API call to FBI API using requests package in python and it receives a JSON output in return.

    def fetch_data_from_api(page):
        pass

### The below function processes and formats the data retrieved from the API or a JSON file. Before processing it checks the type of data it is receiving because for the page argument data, the data is in JSON format and for the file location argument data, the data is in list format since we already have a JSON file and we are passing it's contents in a list format. Then the output of this function is a thorn seperated fields for title, subjects and field_offices items and comma's(if there are more than one string for each filed) for each record. Each record's output is then seperated by a newline character and made into a list.

    def process_data(data):
        pass


### The Main function is to handle fetching and processing data based on provided parameters. If the parameter is a integer value with argument named page, then the flow goes to fetch the data from the API based on the page number and if the argument is a string value (File name) then the flow goes to fetch the {JSON} file and parses it to make into a list format. After all this, the data is then sent into the respective function (fetch_data_from_api/process_data) or both the functions based on the argument(page/file) and prints the three fileds such as title, subjects and field_offices to the standard output.

    def main(page=None, file=None):
        pass 

# Tests Folder (Contains two files for testing)

## test_fetch_data_from_api.py

### This below test function make sure that the fetch_data_from_api() function works correctly when the API call is successful. It simulates a successful API response using mock data, which is given in an example JSON format with keys and values (only one Item), and then verifying that the function correctly handles and returns the data when the API returns a status code of 200(Success Code).

    def test_fetch_data_from_api_success():
        pass

### This below test function checks how the fetch_data_from_api() function behaves when the API call fails. It mocks an API error by setting the status code to 404 and simulates an HTTPError. The test ensures that the function raises the appropriate exception when the API response indicates an error.

    def test_fetch_data_from_api_failure():
        pass

## test_process_data.py

### This below test function verifies that the process_data() function correctly processes and handles an empty data set. By providing an empty list of items, it confirms that the function returns an empty string as expected, reflecting the absence of data.

    def test_process_data_empty():
        pass

### This below test function evaluates the process_data() function's ability to format and process a non-empty data set. It uses sample data with multiple items, including titles, subjects, and field offices, in an JSON format with key value pairs(Contains two records), to ensure that the function formats the data into a thorn-separated string, with each record correctly displayed on a new line.

    def test_process_data_non_empty():
        pass

## Bugs and Assumptions

### As per the bugs, there are few things I want to mention about the code I have written,

1. I am not checking the type of data that the fetch_data_from_api() function explicitly, because I am alraedy checking the type of the argument in the main function, if there is a data type mismatch then,  while running the code in cmd will throw an error with the respective helper Text to the user, so that the user can correct.
2. As for the file name, if the user doesn't have any expected JSON file then the code might break because I am not handling any situation where the file provided by the user should match the required JSON file.