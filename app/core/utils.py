import uuid
import os

def regularizacao_file_path(instance, filename):
    """Generates file name """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/documentos', filename)