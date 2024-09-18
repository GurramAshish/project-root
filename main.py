from input_handlers.csv_handler import load_csv
from input_handlers.api_handler import load_api_data
from input_handlers.mongo_handler import load_mongo_data
from input_handlers.mysql_handler import load_mysql_data
from output_handlers.csv_output import write_to_csv

def main():
    # Load data from different sources
    csv_data = load_csv('input.csv')
    api_data = load_api_data()
    mongo_data = load_mongo_data()
    mysql_data = load_mysql_data()

    # Combine the data (assuming same structure for simplicity)
    combined_data = csv_data + api_data + mongo_data + mysql_data

    # Output consolidated data to CSV
    write_to_csv(combined_data, 'consolidated_output.csv')

if __name__ == "__main__":
    main()
