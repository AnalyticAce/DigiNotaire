
---

# Digital Notary System

The Digital Notary System is a simple web application that allows users to notarize digital documents and verify their authenticity using hash functions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/DigiNotaire.git
   ```
2. Navigate to the project directory:

   ```bash
   cd DigiNotaire
   ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```
2. Access the application in your web browser at [http://localhost:8501](http://localhost:8501).
3. **Document Uploading**:

   - Upload a document for notarization by clicking the "Choose a file" button on the first page.
   - After uploading the document, its hash will be displayed on the same page.
4. **Digital Document Checking**:

   - Navigate to the second page by clicking the "Digital Document Checking" header.
   - Enter the document hash (obtained from the first page) into the text input field and click "Enter Document Hash to Verify".
   - The system will verify the authenticity of the document based on the entered hash and display the result.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any bugs or have suggestions for improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---

Make sure to replace `yourusername` with your actual GitHub username in the clone URL. This README provides instructions on how to install, use, contribute to, and license the project.
