# Licence_plate_text_detector
License Plate Number Detection using EasyOCR

This project performs automatic license plate number detection from images using the EasyOCR library for text detection. It processes a dataset of vehicle images, extracts license plate text, and stores the results in a CSV file.

## Dataset

The dataset used in this project was obtained from Kaggle:  
[License Plate Dataset by Ronak Gohil](https://www.kaggle.com/datasets/ronakgohil/license-plate-dataset)

## Technologies and Libraries Used

- **[EasyOCR](https://www.jaided.ai/easyocr/)**: For detecting and reading license plate text from images.
- **`glob`**: For handling and retrieving image file paths from the dataset directory.
- **`pandas`**: For saving the extracted license plate numbers and associated metadata to a CSV file.

## EasyOCR Resources Used for Learning

- [EasyOCR: A Comprehensive Guide](https://medium.com/@adityamahajan.work/easyocr-a-comprehensive-guide-5ff1cb850168)
- [EasyOCR Official Documentation](https://www.jaided.ai/easyocr/documentation/)

## Project Explanation

The goal of this project is to detect and extract license plate numbers from images using EasyOCR. Below is a step-by-step breakdown of how the project works:

1. **Read Image Paths:**
   - Use the `glob` module to fetch all image file paths from the specified directory.
   - Store the file paths in a list for iteration.

2. **Text Detection with EasyOCR:**
   - Initialize a `reader` object from the  `Reader` class of the EasyOCR library.
   - Loop through the list of image paths and call the `reader.readtext()` method of the reader object to each image.

3. **Process OCR Output:**
   - Extract the detected text from the OCR result.
   - Convert the output into a readable format (e.g., a string).
   - If no text is detected, store `NaN` (not a number) to represent missing data.

4. **Save to CSV:**
   - Store the filename and detected license plate number (or `NaN`) in a pandas DataFrame.
   - Export the DataFrame to a CSV file (`results.csv`) for future analysis or reference.

