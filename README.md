# Lux Commute Planner

This project aims to develop an Alexa skill to facilitate daily commute planning for individuals in Luxembourg, utilizing the Mobiliteit.lu API to provide real-time route and distance information.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` using pip.
3. Set up a virtual environment and activate it.
4. Load the environment variables from `.env` file.
5. Run the `lambda_function.py` script to start the application.

## Project Structure

- `src/`: Source code directory
  - `api/`: Directory containing API interaction code
    - `mobiliteit_lu.py`: Main classes and methods for interacting with the Mobiliteit.lu API.
  - `lambda_function.py`: The AWS Lambda handler file.

## Environment Variables

- `MOBILITEIT_API_KEY`: Your personal API key for accessing the Mobiliteit.lu API.

## Notes

- In the API `rt` means Real Time

## License

This project is open source and available under the [MIT License](LICENSE).

