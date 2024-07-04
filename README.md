# Book Recommender System

This project involves creating a book recommendation system using machine learning approaches and making it interactive and visual with a web interface.

## Features

- **Content-Based Filtering**
- **Collaborative Filtering**
- **Interactive Web Interface**

## Tech Stack

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS
- **Machine Learning**: scikit-learn, pandas, NumPy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rsrajahnsa/Book-Reccomendation-System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Book-Reccomendation-System
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:
    ```bash
    python app.py
    ```
2. Open your browser and go to `http://127.0.0.1:5000/`.

## Files

- `app.py`: Flask application
- `Book_Recommender_System.ipynb`: Jupyter notebook for model development
- `index.html`: Homepage
- `recommend.html`: Recommendation page
- `popular.pkl`, `pt.pkl`, `similarity_scores.pkl`: Pre-trained model files

## Dataset

The dataset contains information on 1 million books and user interactions, used for generating recommendations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

Thanks to all the contributors and the open-source community.

---

For more details, visit the [GitHub repository](https://github.com/rsrajahnsa/Book-Reccomendation-System).
