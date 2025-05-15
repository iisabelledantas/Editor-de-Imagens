import cv2
import numpy as np
import os
from PIL import Image
import io

class ImageProcessor:
    
    @staticmethod
    def convert_to_bytes(img, max_size=800):
        
        if img is None:
            return None
        try:
            img_pil = Image.fromarray(img)
            bio = io.BytesIO()
            img_pil.save(bio, format="PNG")
            return bio.getvalue()
        except Exception as e:
            print(f"Erro ao converter imagem: {e}")
            return None
    
    @staticmethod
    def load_image(file_path):

        if not file_path or not os.path.exists(file_path):
            return None
            
        img = cv2.imread(file_path)
        
        return img
    
    @staticmethod
    def apply_grayscale(img):
        return cv2.cvtColor(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)

    @staticmethod
    def apply_invert(img):
        return cv2.bitwise_not(img)

    @staticmethod
    def apply_contrast(img, alpha=1.5):
        return cv2.convertScaleAbs(img, alpha=alpha, beta=0)

    @staticmethod
    def apply_blur(img, kernel_size=5):
        return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    @staticmethod
    def apply_sharpen(img):
        kernel = np.array([[-1, -1, -1],
                          [-1, 9, -1],
                          [-1, -1, -1]])
        return cv2.filter2D(img, -1, kernel)

    @staticmethod
    def apply_edge_detection(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) if len(img.shape) > 2 else img
        edges = cv2.Canny(gray, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def apply_rotation(img, angle=90):
        height, width = img.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
        return cv2.warpAffine(img, rotation_matrix, (width, height))

    @staticmethod
    def apply_resize(img, scale=0.5):
        height, width = img.shape[:2]
        return cv2.resize(img, (int(width * scale), int(height * scale)))
