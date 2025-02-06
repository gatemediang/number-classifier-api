# Number Classification API
This is a simple Flask-based API that classifies numbers and provides interesting mathematical properties and fun facts about them a given number. The API can determine if a number is prime, perfect, or an Armstrong number.

## Endpoints

Base URL: `https://number-classifier-api-nmkh.onrender.com/`

Endpoint: `/api/classify-number`

Query Parameter: `?number=n` (where n is an integer to classify)

## Request
**Method:** GET

**Responses:**
- `200 OK`: Returns a JSON object with the number and its properties.
- `400 Bad Request`: Returns an error if the input is not a valid number.

## Local Setup

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the Flask application:
    ```sh
    flask run
    ```
3. Fetch below url on browser or curl as below

```sh
curl -X GET "http://localhost:5000/api/classify-number?number=28"
```

## Deployment on Render

The API is deployed on Render and is publicly accessible on `https://number-classifier-api-nmkh.onrender.com.
You can test it by sending a GET request to the `https://number-classifier-api-nmkh.onrender.com/api/classify-number` endpoint.

### Example Request
To classify a number, make a GET request to `https://number-classifier-api-nmkh.onrender.com/api/classify-number` with the `number` query parameter:

```sh
GET https://number-classifier-api-nmkh.onrender.com/api/classify-number?number=371
```

### Example Response (200 OK)

```sh
json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Example Response (400 Bad Request):

```sh
json
{
    "number": "alphabet",
    "error": true
}
```

### Possible Properties:

prime: The number is prime.

perfect: The number is a perfect number.

armstrong: The number is an Armstrong number.

odd: The number is odd.

even: The number is even.

### Error Handling
400 Bad Request: Returned if the input is not a valid integer.

## License

This project is licensed under the MIT License.
```