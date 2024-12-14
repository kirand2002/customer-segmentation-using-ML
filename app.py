from python.config import app
from routes.home import index
from routes.home import usergallery
from routes.file import file
from routes.segmentation import dashboard 
# run the app.

if __name__ == "__main__":
    app.run(debug=True)