# Image Tone and Brightness Prediction

This project is a web-based application built using **Streamlit** that predicts the tone and brightness of an uploaded image. It uses OpenCV and NumPy for image processing and provides users with detailed insights into the image's tonal composition and brightness distribution.

## Features

- **Cool vs. Warm Prediction:** Determines whether the image tone is predominantly cool or warm.
- **Dull vs. Bright Prediction:** Analyzes the brightness of the image to classify it as dull or bright.
- Displays the percentage of warm, cool, dull, and bright pixels for better understanding.

## Technologies Used

- **Streamlit:** For creating the web application.
- **OpenCV:** For image processing.
- **NumPy:** For numerical computations.
- **Pillow:** For image file handling.

## Setup and Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/image-tone-brightness.git
   ```

2. Navigate to the project directory:
   ```bash
   cd image-tone-brightness
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the app in your browser (usually at [https://image-tone-and-brightness-prediction-cv-eq9yjsvufirfru4udt39rq.streamlit.app/](https://image-tone-and-brightness-prediction-cv-eq9yjsvufirfru4udt39rq.streamlit.app/)).

## How It Works

1. Upload an image using the file uploader. Supported formats: `.jpg`, `.png`, `.jpeg`.
2. The app analyzes the image using OpenCV and NumPy:
   - For tone prediction, it calculates the percentage of cool and warm tones based on the hue values in the HSV color space.
   - For brightness prediction, it identifies dull and bright regions based on saturation and value thresholds.
3. Results are displayed, including warm/cool tone percentages and dull/bright percentages.

## Example Output

Upon uploading an image, the app will display:

- **Cool vs. Warm Prediction:** Warm or Cool tone with percentages.
- **Dull vs. Bright Prediction:** Dull or Bright classification with percentages.

## File Structure

```plaintext
image-tone-brightness/
|-- app.py                # Main application file
|-- requirements.txt      # List of dependencies
|-- README.md             # This README file
```

## Requirements

- Python 3.8 or higher
- Streamlit
- OpenCV
- NumPy
- Pillow

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it as per the license terms.

## Contact

For any questions or feedback, please reach out to [krishnanr1771@gmail.com](krishnanr1771@gmail.com).

