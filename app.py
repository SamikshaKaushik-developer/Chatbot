# Import the necessary libraries for our Flask application.
from flask import Flask, jsonify
from flask_cors import CORS # This is crucial for connecting to our frontend
import requests # We'll use this to make API calls if a real API is found
import os

# Create a new Flask application instance.
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for all routes.
# This allows the frontend (served from a different origin) to
# make requests to this backend.
CORS(app)

# This is a sample dataset of hackathons.
# In a real-world application, this would be replaced with a call to an
# external API or a database query.
SAMPLE_HACKATHONS = [
    {
        "id": 1,
        "title": "Innovate India Hackathon",
        "location": "Bengaluru",
        "date": "2025-10-20",
        "description": "A national-level hackathon focused on solving social challenges in India using technology. Topics include sustainable energy and smart cities."
    },
    {
        "id": 2,
        "title": "Code for a Cause",
        "location": "Online",
        "date": "2025-11-15",
        "description": "A virtual hackathon dedicated to building solutions for non-profit organizations. Open to all skill levels."
    },
    {
        "id": 3,
        "title": "Tech Titans India",
        "location": "Hyderabad",
        "date": "2025-12-05",
        "description": "An in-person event for seasoned developers to tackle advanced problems in AI and blockchain. Huge prizes await the top teams."
    },
    {
        "id": 4,
        "title": "Startup Weekend",
        "location": "Mumbai",
        "date": "2025-12-10",
        "description": "A 54-hour event where participants build a complete business idea from scratch. Focus is on business and product development."
    }
]

@app.route('/')
def home():
    """A simple root route to confirm the server is running."""
    return "Hello from the Hackathon API backend!"

@app.route('/api/hackathons', methods=['GET'])
def get_hackathons():
    """
    API endpoint to get a list of hackathons.
    This function demonstrates where you would make a real API call.
    For this example, we're returning our static list of hackathons.
    """
    try:
        # Example of how to fetch data from an external API if you had one.
        # This part is commented out as we don't have a specific API URL.
        # api_url = "https://example.com/api/hackathons-india"
        # response = requests.get(api_url)
        # response.raise_for_status() # Raise an exception for bad status codes
        # hackathons = response.json()

        # For now, we return the sample data.
        hackathons = SAMPLE_HACKATHONS

        # Return the hackathon data as a JSON response.
        return jsonify(hackathons)

    except requests.exceptions.RequestException as e:
        # Handle errors if the external API call fails.
        return jsonify({"error": "Failed to fetch data from external API"}), 500
    except Exception as e:
        # Handle other potential errors.
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Get the port from the environment, defaulting to 5000 for local development.
    port = int(os.environ.get("PORT", 5000))
    # Run the Flask app in debug mode.
    app.run(debug=True, host='0.0.0.0', port=port)