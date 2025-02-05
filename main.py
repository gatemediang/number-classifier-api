from flask import Flask, jsonify, request
from flask_cors import CORS
import math


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d**num_digits for d in digits) == n


def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(n))


def get_fun_fact(n):
    """Generate a fun fact about the number."""
    if is_armstrong(n):
        return f"{n} is an Armstrong number because {' + '.join(f'{d}^{len(str(n))}' for d in str(n))} = {n}"
    elif is_prime(n):
        return f"{n} is a prime number."
    elif is_perfect(n):
        return f"{n} is a perfect number."
    else:
        return f"{n} is a fascinating number with unique properties."


@app.route("/api/classify-number", methods=["GET"])
def classify_number():
    """Endpoint to classify a number and return its properties."""
    number = request.args.get("number")

    # Input validation
    if not number or not number.lstrip("-").isdigit():
        return jsonify({"number": number if number else "None", "error": True}), 400

    n = int(number)
    properties = []
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 1:
        properties.append("odd")
    else:
        properties.append("even")

    return (
        jsonify(
            {
                "number": n,
                "is_prime": is_prime(n),
                "is_perfect": is_perfect(n),
                "properties": properties,
                "digit_sum": digit_sum(n),
                "fun_fact": get_fun_fact(n),
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
