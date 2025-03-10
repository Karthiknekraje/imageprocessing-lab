import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Could not load image")
        exit()
    return image

def apply_sobel(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    return sobel_combined

def apply_laplacian(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    return laplacian

def apply_canny(image, threshold1, threshold2):
    canny_edges = cv2.Canny(image, threshold1, threshold2)
    return canny_edges

def main():
    image_path = input("Enter the image path: ")
    image = load_image(image_path)
    
    sobel_edges = apply_sobel(image)
    laplacian_edges = apply_laplacian(image)
    canny_edges = apply_canny(image, 100, 200)  # Adjust thresholds as needed
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Sobel Edges', np.uint8(sobel_edges))
    cv2.imshow('Laplacian Edges', np.uint8(laplacian_edges))
    cv2.imshow('Canny Edges', canny_edges)
    
    save_option = input("Do you want to save the processed images? (yes/no): ").strip().lower()
    
    if save_option == "yes":
        cv2.imwrite("sobel_edges.jpg", np.uint8(sobel_edges))
        cv2.imwrite("Laplacian_edges.jpg", np.uint8(laplacian_edges))
        cv2.imwrite("canny_edges.jpg", canny_edges)
        print("Processed images saved successfully!")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
