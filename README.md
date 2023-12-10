# SummarizeTube

This repository contains the code for a web application that generates summaries of YouTube videos using the Llama 2
LLM.

### Installation

1. Clone this repository:

```
git clone https://github.com/mrashutoshnigam/Youtube_Summary_Generator.git
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Set up environment variables:

* ```LAMA_2_API_KEY```: Your API Key for Llama 2 LLM
* ```DATABASE_URL```: URL of your database

4. Start the application:

```
python app.py
```

### Features

* Generates summaries of YouTube videos using the Llama 2 LLM.
* Saves summaries to a database for future reference.
* User-friendly interface for searching for videos and viewing summaries.
* Hosted on AWS for global accessibility.

### Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* Llama 2 LLM
* AWS

### Usage

Open the application in your web browser: http://localhost:5000 (or your deployed URL)
Enter a YouTube video URL in the search bar.
Click the "Generate Summary" button.
The application will display a summary of the video.

### License

This project is licensed under the MIT License. See the LICENSE file for more information.
