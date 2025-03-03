import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Error: Could not load image")
        exit()
    return image

def translate_image(image, tx, ty):
    rows, cols = image.shape[:2]
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])  # Correct the matrix
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))  # Pass the image
    return translated_image

def rotate_image(image, angle):
    rows, cols = image.shape[:2]
    center = (cols // 2, rows // 2)  # Set the center for rotation
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)  # Use angle and center
    
    # Calculate the new size after rotation to avoid cropping
    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])

    # Compute the new bounding dimensions
    new_width = int(rows * abs_sin + cols * abs_cos)
    new_height = int(rows * abs_cos + cols * abs_sin)

    # Adjust the rotation matrix to account for the translation due to the new size
    rotation_matrix[0, 2] += (new_width / 2) - center[0]
    rotation_matrix[1, 2] += (new_height / 2) - center[1]

    # Perform the actual rotation with the new dimensions
    rotated_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))  # Pass the image
    return rotated_image

def scale_image(image, scale_x, scale_y):
    scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y)  # Pass image and scaling factors
    return scaled_image

def main():
    image_path = input("Enter the image path: ")
    image = load_image(image_path)
    
    tx = int(input("Enter the translation in x direction: "))
    ty = int(input("Enter the translation in y direction: "))
    angle = float(input("Enter the rotation angle: "))
    scale_x = float(input("Enter scaling factor for x: "))
    scale_y = float(input("Enter scaling factor for y: "))
    
    # Pass arguments when calling the functions
    translated = translate_image(image, tx, ty)
    rotated = rotate_image(image, angle)
    scaled = scale_image(image, scale_x, scale_y)
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated)
    cv2.imshow('Rotated Image', rotated)
    cv2.imshow('Scaled Image', scaled)
    
    save_option = input("Do you want to save the transformed images? (yes/no): ").strip().lower()

    if save_option == "yes":
        cv2.imwrite("Translated_image.jpg", translated)
        cv2.imwrite("Rotated_image.jpg", rotated)  # Corrected typo 'inwrite' to 'imwrite'
        cv2.imwrite("Scaled_image.jpg", scaled)
        print("Images saved successfully!")
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
