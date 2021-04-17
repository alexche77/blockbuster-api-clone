class RequestFailedError(Exception):
    pass


class InvalidCredentialError(Exception):
    pass


class MovieNotFound(Exception):
    def __init__(self, imdb_id, message="IMDB ID does not corresponds to a movie"):
        self.imdb_id = imdb_id
        self.message = message
        super().__init__(self.message)
