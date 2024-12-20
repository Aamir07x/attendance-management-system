import face_recognition
from datetime import datetime

def detect_face(image_path):
    known_faces = {
        'Aamir': '/path_to_aamir_image.jpg',
        'OtherPerson': 'path_to_other_image.jpg'
    }
    img = face_recognition.load_image_file(image_path)
    img_encoding = face_recognition.face_encodings(img)[0]

    for name, face_path in known_faces.items():
        known_image = face_recognition.load_image_file(face_path)
        known_encoding = face_recognition.face_encodings(known_image)[0]
        match = face_recognition.compare_faces([known_encoding], img_encoding)
        if match[0]:
            return name
    return None

def mark_attendance(db_path, name):
    from utils.db_operations import log_attendance
    log_attendance(db_path, name, datetime.now())
