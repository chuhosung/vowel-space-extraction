# Vowel Space Automatic Extraction

This project aims to automatically extract vowel space using formant data from speech samples. It reads formant data (F1, F2) from CSV files for different vowels, calculates stable formant values, and visualizes the vowel triangle for both a participant and normal reference values.

## Features
- **Automatic Formant Extraction**: Extracts F1 and F2 formant values from CSV files.
- **Stable Value Selection**: Uses median and mode to select stable formant values, providing reliable data for analysis.
- **Vowel Space Area (VSA) Calculation**: Computes the Vowel Space Area using Heron's formula, allowing a quantitative measure of the vowel space.
- **Visualization**: Draws vowel triangles for both participant and normal reference values to compare speech characteristics visually.
- **Analysis and Feedback**: Provides interpretation of how the participant's formant values differ from the normal range, which is useful for speech therapy and research.

## Installation
### Clone the Repository
First, clone the repository to your local machine:
```sh
git clone <repository_url>
```

### Install Required Packages
Ensure you have Python 3.8 or above. Install the necessary packages using the provided `requirements.txt` file:
```sh
pip install -r requirements.txt
```

## Usage
1. **Prepare Input CSV Files**: CSV files containing formant data for the vowels `/a/`, `/i/`, `/u/` are needed. The CSV files must contain columns named `f1` and `f2` for the formant values.
   - Example CSV format:
     ```csv
     f1,f2
     730,1090
     270,2290
     300,870
     ```

2. **Run the Script**: Execute the Python script to extract and visualize the vowel space:
   ```sh
   python extract_vowel_space.py
   ```

3. **Output**: The script will generate a plot showing the vowel triangle for both the participant and normal reference values, along with a table summarizing F1, F2 values, and VSA comparison.

## Example Output
- **Vowel Triangle Plot**: A graphical comparison between the participant's vowel space and the normal reference values.
- **Data Table**: Summarizes the F1, F2 values for each vowel and compares the Vowel Space Area (VSA).
- **Interpretation**: Analyzes whether the tongue movement was more forward or backward and its impact on speech clarity.

## FastTrack Integration
This project utilizes the FastTrack Praat script developed by Santiago Barreda. FastTrack generates Excel files with formant data at 0.002-second intervals. By analyzing these detailed formant data outputs, stable segments were identified to create a vowel triangle graph. This visual feedback is particularly useful for speech-language pathologists (SLPs), as it helps evaluate pronunciation accuracy and provide visual feedback to clients.

If you download the FastTrack technology developed by Santiago Barreda, you can automatically extract formant data in Praat. One of the features of FastTrack is that it extracts formant values every 0.02 seconds, and if you input the resulting Excel file into this Python code, it will extract stable segments and generate a vowel triangle graph.

Using the Excel files generated by FastTrack, you can easily extract formant data and visualize the vowel triangle, making this project valuable for speech therapy and phonetic research.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Portions of this project utilize the FastTrack script by Santiago Barreda, which is also licensed under the MIT License.

## Credits
Special thanks to Santiago Barreda for the development of the [FastTrack](https://github.com/santiagobarreda/FastTrack) Praat script, which made this project possible by providing detailed formant data extraction.

## Additional Information
### Add a License File
Ensure that others can use the project by including a `LICENSE` file, such as the MIT License.

### Provide Example and Test Files
Include example data to make it easier for others to test and use your project.

### Use GitHub Pages (Optional)
Share project results visually by using GitHub Pages to create a simple explanation or result page.

## Feedback and Promotion
1. **Use GitHub Issues**: Enable the Issues feature so people can easily report questions or bugs.
2. **Share the Project**: Share your project on social media or related communities to receive more feedback and contributions.

This preparation will help others easily run and provide feedback on your 'vowel space automatic extraction' project! Feel free to reach out if you have any questions or need further clarification.

