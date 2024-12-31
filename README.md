<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Image Tone and Brightness Prediction</title>
</head>
<body>
    <h1 style="text-align: center;">Image Tone and Brightness Prediction</h1>

    <p>
        This project is a web-based application built using <strong>Streamlit</strong> that predicts the tone and brightness of an uploaded image. It uses OpenCV and NumPy for image processing and provides users with detailed insights into the image's tonal composition and brightness distribution.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Cool vs. Warm Prediction:</strong> Determines whether the image tone is predominantly cool or warm.</li>
        <li><strong>Dull vs. Bright Prediction:</strong> Analyzes the brightness of the image to classify it as dull or bright.</li>
        <li>Displays the percentage of warm, cool, dull, and bright pixels for better understanding.</li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Streamlit:</strong> For creating the web application.</li>
        <li><strong>OpenCV:</strong> For image processing.</li>
        <li><strong>NumPy:</strong> For numerical computations.</li>
        <li><strong>Pillow:</strong> For image file handling.</li>
    </ul>

    <h2>Setup and Installation</h2>
    <ol>
        <li>Clone this repository to your local machine:
            <pre><code>git clone https://github.com/yourusername/image-tone-brightness.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd image-tone-brightness</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Run the Streamlit app:
            <pre><code>streamlit run app.py</code></pre>
        </li>
        <li>Open the app in your browser (usually at <a href="http://localhost:8501">http://localhost:8501</a>).</li>
    </ol>

    <h2>How It Works</h2>
    <ol>
        <li>Upload an image using the file uploader. Supported formats: <code>.jpg</code>, <code>.png</code>, <code>.jpeg</code>.</li>
        <li>The app analyzes the image using OpenCV and NumPy:
            <ul>
                <li>For tone prediction, it calculates the percentage of cool and warm tones based on the hue values in the HSV color space.</li>
                <li>For brightness prediction, it identifies dull and bright regions based on saturation and value thresholds.</li>
            </ul>
        </li>
        <li>Results are displayed, including warm/cool tone percentages and dull/bright percentages.</li>
    </ol>

    <h2>Example Output</h2>
    <p>Upon uploading an image, the app will display:</p>
    <ul>
        <li><strong>Cool vs. Warm Prediction:</strong> Warm or Cool tone with percentages.</li>
        <li><strong>Dull vs. Bright Prediction:</strong> Dull or Bright classification with percentages.</li>
    </ul>

    <h2>File Structure</h2>
    <pre><code>
    image-tone-brightness/
    |-- app.py                # Main application file
    |-- requirements.txt      # List of dependencies
    |-- README.html           # This README file
    </code></pre>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>Streamlit</li>
        <li>OpenCV</li>
        <li>NumPy</li>
        <li>Pillow</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to fork the repository and submit pull requests.</p>

    <h2>License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>. You are free to use, modify, and distribute it as per the license terms.</p>

    <h2>Contact</h2>
    <p>For any questions or feedback, please reach out to <a href="mailto:yourname@example.com">yourname@example.com</a>.</p>
</body>
</html>
