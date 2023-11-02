import rgb_yuv
import cv2 
import time
import os


#main
if __name__ == '__main__':
    # Exercise 1 rgb2yuv and yuv2rgb
    print('Exercise 1: rgb2yuv and yuv2rgb')
    # RGB to YUV
    r, g, b = 255, 0, 0  # Example RGB values
    y, u, v = rgb_yuv.rgb_to_yuv(r, g, b)
    print(f"RGB to YUV: R={r}, G={g}, B={b} -> Y={y}, U={u}, V={v}")

    # YUV to RGB
    y, u, v = 255, 0, 0  # Example YUV values
    r, g, b = rgb_yuv.yuv_to_rgb(y, u, v)
    print(f"YUV to RGB: Y={y}, U={u}, V={v} -> R={r}, G={g}, B={b}")
    

    #Wait for key press
    print("\t Results of exercise 1 are shown in the terminal.")
    print('---------------Press Enter to continue-------------------')
    input()
    



    # Exercise 2 resize_image
    print('Exercise 2: resize_image')
    # Resize image
    rgb_yuv.resize_image('lena.jpeg', 'lena_small.jpeg', width=100, height=100)
    # Resize image
    rgb_yuv.resize_image('lena.jpeg', 'lena_large.jpeg', width=400, height=400)
    # Resize image
    rgb_yuv.resize_image('lena.jpeg', 'lena_high_quality.jpeg', quality=1)
    # Resize image
    rgb_yuv.resize_image('lena.jpeg', 'lena_low_quality.jpeg', quality=31)

    # # Wait for 5 seconds
    # print('---------------Sleeping for 5 seconds-------------------')
    # time.sleep(5)  # Sleep for 5 seconds

    # Show images
    img_small = cv2.imread('lena_small.jpeg')
    img_large = cv2.imread('lena_large.jpeg')
    img_high_quality = cv2.imread('lena_high_quality.jpeg')
    img_low_quality = cv2.imread('lena_low_quality.jpeg')
    cv2.imshow('img_small', img_small)
    cv2.imshow('img_large', img_large)
    cv2.imshow('img_high_quality', img_high_quality)
    cv2.imshow('img_low_quality', img_low_quality)

    print("\t Results of exercise 2 are shown in the images.")
    print('---------------Press any key to continue-------------------')
    cv2.waitKey()
    cv2.destroyAllWindows()

    #  Delete new images
    os.remove('lena_small.jpeg')
    os.remove('lena_large.jpeg')
    os.remove('lena_high_quality.jpeg')
    os.remove('lena_low_quality.jpeg')

    #Exercise 3:  Serpentine
    print('Exercise 3: Serpentine')
    # Read image
    rgb_yuv.serpentine('lena.jpeg','lena_serpentine.jpeg')
    # Show images
    img = cv2.imread('lena_serpentine.jpeg')
    cv2.imshow('img_serpentine', img)

    print("\t Results of exercise 3 are shown in the image.")
    print('---------------Press any key to continue-------------------')
    cv2.waitKey()
    cv2.destroyAllWindows()
    # Delete new image
    os.remove('lena_serpentine.jpeg')

    # Exercise 4:   Use ffmpeg to transform the previous image into b/w. Do the hardest compression you can.
    #First resize image to 300x300 in order to divide by 2
    rgb_yuv.resize_image('lena.jpeg', 'lena_large.jpeg', width=300, height=300)

    rgb_yuv.convert_to_bw_and_compress('lena_large.jpeg','lena_bw.jpeg')
    
    # # Sleep for 5 seconds
    # print('---------------Sleeping for 5 seconds-------------------')
    # time.sleep(5)  # Sleep for 5 seconds
    
    # Show images
    img = cv2.imread('lena_bw.jpeg')
    cv2.imshow('img_bw', img)

    print("\t Results of exercise 4 are shown in the image.")
    print('---------------Press any key to continue-------------------')
    cv2.waitKey()
    cv2.destroyAllWindows()
    # Delete new image
    os.remove('lena_bw.jpeg')
    os.remove('lena_large.jpeg')

    # Exercise 5:  RLE
    print("Exercise 5: RLE")
    # Example usage:
    input_bytes = b'AAAABBBCCDAA'
    print(f"Input bytes: {input_bytes}")
    encoded_bytes = rgb_yuv.rle_encode(input_bytes)
    print(f"Encoded bytes: {encoded_bytes}")

    print("\t Results of exercise 5 are shown in the terminal.")
    print('---------------Press Enter to exit -------------------')
    input()
    





