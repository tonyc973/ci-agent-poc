# AI Civil Servant Agent (POC)

A Proof of Concept (POC) demonstrating a simple workflow for public administration that may be integrated in more complicated Agentic AI workflows. This application acts as a "Civil Servant" chatbot that interviews a user to collect data and automatically generates a filled, good-looking PDF application for a 14-year-old's Identity Card.

> **Note:** The generated PDF is for demonstration purposes only.

## 🚀 Features

* **Agentic Interface:** A conversational UI (built with Streamlit) that replaces complex static forms.
* **Dynamic PDF Generation:** Creates a fillable PDF template from scratch using Python (`reportlab`).
* **Auto-Filling:** Maps user data into the PDF form fields programmatically (`PyPDFForm`).

<img width="1470" height="936" alt="Screenshot 2025-12-02 215807" src="https://github.com/user-attachments/assets/bf9ed404-0286-41ac-a620-15e032c2aa9f" />

<img width="996" height="939" alt="image" src="https://github.com/user-attachments/assets/ae6796a7-ec79-46c2-8db8-f2b538ee62c2" />


## 🛠️ Tech Stack

* **Python 3.8+**
* **Streamlit:** For the web interface.
* **ReportLab:** To draw the PDF template and form fields.
* **PyPDFForm:** To fill the interactive PDF fields.

## 📦 Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/tonyc973/ci-agent-poc.git](https://github.com/tonyc973/ci-agent-poc.git)
    cd ci-agent-poc
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ How to Run

1.  **Generate the Template:**
    Run the generator script once to create the blank PDF form in the `assets/` folder.
    ```bash
    python3 generator.py
    ```

2.  **Start the Agent:**
    Launch the Streamlit interface.
    ```bash
    streamlit run main.py
    ```

3.  **Interact:**
    Open your browser to `http://localhost:8501`, chat with the agent, and download your filled PDF at the end.

## 📂 Project Structure

```text
.
├── assets/                  # Stores the generated blank PDF
├── generator.py             # Script to draw the blank PDF template
├── main.py                  # The Streamlit application logic
├── requirements.txt         # Project dependencies
└── README.md                # Documentation
