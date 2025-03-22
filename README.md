# Portfolio Website

My portfolio website which currently has technologies, projects, and a contact me section.

## Features

- Dynamic project display
- Responsive design
- Clean layout with hover effects on each project
- On-click redirection to individual project pages

## Requirements

- Python 3.x
- Flask
- HTML/CSS

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Create a `static` folder in your project directory and place your image files (e.g., `rust.png`) inside.
2. In the `templates` folder, create an `index.html` file and paste the provided HTML structure for the projects.
3. Run the Flask app:

```bash
flask run
```

4. Visit the app in your browser at `http://127.0.0.1:5000/`.

## Directory Structure

```
/project-root
  /static
  /templates
    index.html
  app.py
  requirements.txt
  README.md
```

## Make sure to install Requirements File (requirements.txt)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` gives a basic overview of how to set up, use, and structure your Flask application. It also includes instructions for running the app, adding project boxes, and details on the required files.