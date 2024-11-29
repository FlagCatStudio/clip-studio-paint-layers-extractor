import sqlite3
import io
from PIL import Image

class ClipStudio:
    def __init__(self, db_path):
        """
        Initialize a ClipStudio instance with an SQLite database.
        """
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    @staticmethod
    def load(file_path):
        """
        Load a .clip file and extract the SQLite database.
        """
        with open(file_path, 'rb') as f:
            data = f.read()

        # Find the SQLite signature in the file
        index = data.find(b"SQLite")
        if index == -1:
            raise ValueError("SQLite database not found in the .clip file")

        sqlite_data = data[index:]
        db_path = "extracted_clip.sqlite"
        with open(db_path, 'wb') as db_file:
            db_file.write(sqlite_data)

        return ClipStudio(db_path)

    def get_thumbnail(self):
        """
        Extract a thumbnail from the SQLite database.
        """
        query = "SELECT ImageData FROM CanvasPreview"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        if result:
            thumbnail_data = result[0]
            image = Image.open(io.BytesIO(thumbnail_data))
            return image
        else:
            raise ValueError("No thumbnail found in the SQLite database.")

    def get_layers(self):
        """
        Extract layers from the SQLite database.
        """
        query = """
        SELECT LayerUuid, _PW_ID, LayerName, LayerOpacity, LayerVisibility, LayerFolder
        FROM Layer
        """
        self.cursor.execute(query)
        layers = [
            {
                "id": row[0],
                "index": row[1],
                "name": row[2],
                "opacity": row[3],
                "visibility": row[4],
                "folder": row[5],
            }
            for row in self.cursor.fetchall()
        ]
        return layers

    def close(self):
        """
        Close the SQLite connection.
        """
        self.connection.close()
