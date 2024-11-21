Project Overview

This project aims to automatically extract vowel space using formant data from speech samples. The code reads formant data (F1, F2) from CSV files for different vowels, calculates stable formant values, and visualizes the vowel triangle for both a participant and normal reference values.

Features

Automatic formant extraction: Extracts F1 and F2 formant values from CSV files.

Stable value selection: Uses median and mode to select stable formant values.

Vowel Space Area (VSA) Calculation: Computes the Vowel Space Area using Heron's formula.

Visualization: Draws vowel triangles for participant and normal reference values.

Interpretation: Provides an analysis of the participant's formant values compared to the normal range.

Installation

Clone the Repository

git clone <repository_url>

Install Required Packages
Ensure you have Python 3.8 or above. Install the required packages by running:

pip install -r requirements.txt

Usage

Prepare Input CSV Files: Ensure you have CSV files containing formant data for the vowels /a/, /i/, and /u/. The CSV files should have columns named f1 and f2 for formant values.

Run the Script: Execute the Python script to extract the vowel space and visualize it:

python extract_vowel_space.py

Output: The script will generate a plot showing the vowel triangle for both the participant and normal reference values, along with a table displaying the detailed F1, F2 values and VSA comparison.

Example Output

The output includes:

A vowel triangle plot that compares participant and normal vowel spaces.

A data table summarizing F1, F2 values for each vowel and the VSA.

An interpretation section that analyzes the differences between participant values and normal values, such as whether the tongue movement was more forward or backward.

License

This project is licensed under the MIT License. See the LICENSE file for more details.# vowel-space-extraction
Automatic vowel space extraction Python script
