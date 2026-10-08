from database.mongodb import get_database


class ChunkRepository:

    def __init__(self):
        db = get_database()
        self.collection = db["document_chunks"]

    def create_chunks(self, chunks: list):

        if not chunks:
            return

        self.collection.insert_many(chunks)