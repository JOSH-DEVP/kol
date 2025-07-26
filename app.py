from flask import Flask, request, render_template, render_template_string
import datetime

app = Flask(__name__)
locations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    lat = request.form.get('latitude')
    lon = request.form.get('longitude')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    locations.append({'lat': lat, 'lon': lon, 'time': timestamp})
    print(f"[{timestamp}] Location received: {lat}, {lon}")
    return "Location received. Thank you!"

@app.route('/view')
def view():
    html = """
    <h2>📍 Received Locations:</h2>
    {% for loc in locations %}
        <p>
            <strong>Time:</strong> {{ loc.time }}<br>
            <strong>Latitude:</strong> {{ loc.lat }}<br>
            <strong>Longitude:</strong> {{ loc.lon }}<br>
            <a href="https://www.google.com/maps?q={{ loc.lat }},{{ loc.lon }}" target="_blank">
                📍 View on Google Maps
            </a>
            <hr>
        </p>
    {% endfor %}
    """
    return render_template_string(html, locations=locations)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
