from flask import Flask, request, jsonify
import csv




app = Flask(__name__)



# Load CSV data into a dictionary for quick lookups
csv_data = {}
with open('classification_results.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        
        csv_data[row[0]] = row[1]
        # keys = csv_data.keys()
        # print(csv_data)

@app.route('/', methods=['POST'])
def get_image_details():
    try:
        if 'inputFile' not in request.files:
            return jsonify({'error': 'No file provided'})
        # print("ajbdfj")
        # Get the uploaded file
        uploaded_file = request.files['inputFile']

        # Extract and return the filename
        image_name = uploaded_file.filename.split('.')[0]
        if image_name in csv_data:
            # print("Patel")  
            text = csv_data[image_name]
            return image_name + ":"+ text
        else:
            return jsonify({'error': 'Image not found in CSV'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
