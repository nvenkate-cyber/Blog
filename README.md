# Flask-Blog

Minimal Flask template to get started on your blog application for MLH Fellowship Production Engineering track.
 

## Installation

Make sure you have python3 and pip installed


Create and activate virtual environment using virtualenv

1. Add `FLASK_ENV=development` to .env
2. 
    ```bash
    $ docker-compose up
    ```

3. Access it at `http://127.0.0.1:5000`

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage


Create a .env file using the example.env template


Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
