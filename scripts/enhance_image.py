import cv2
import sys
import os

def enhance_image(input_path):
    image = cv2.imread(input_path)
    if image is None:
        print("Image not found.")
        return

    # Convert to YUV and enhance brightness
    yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
    enhanced = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

    # Save result
    output_path = os.path.join("results", "enhanced_" + os.path.basename(input_path))
    cv2.imwrite(output_path, enhanced)
    print(f"Enhanced image saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python enhance_image.py <image_path>")
    else:
        enhance_image(sys.argv[1])
