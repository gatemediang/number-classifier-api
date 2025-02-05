# Number Classification API

This API provides interesting mathematical properties and a fun fact about a given number.

## Deployment

The API is deployed using Flask and is publicly accessible. 
You can test it by sending a GET request to the `/api/classify-number` endpoint.

API Documentation
Base URL: `https://<your-domain.com>/api`

Endpoint: GET /classify-number
Description:
Returns interesting mathematical properties and a fun fact about a given number.

Parameters:

number (required): An integer to analyze

### Example Request

```Bash
GET /api/classify-number?number=371

### Example Response (200 OK)

json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}`

### Example Response (400 Bad Request):
json
{
    "number": "alphabet",
    "error": true
}

### Possible Properties:

prime: The number is prime.

perfect: The number is a perfect number.

armstrong: The number is an Armstrong number.

odd: The number is odd.

even: The number is even.

Error Handling
400 Bad Request: Returned if the input is not a valid integer.