import cv2

from find_object import FindObject

def main(args=None):

    find_object = FindObject()

    dist_x,dist_y = find_object.listener_callback("test_img5.jpg", 150)
    print("The gear is "+str(abs(dist_x))+"mm to the "+ ("right" if dist_x>0 else "left") +" of the center of the camera")
    print("The gear is "+str(abs(dist_y))+"mm "+("above" if dist_y < 0 else "below") + " the center of the camera")
    cv2.imshow("Blurred", find_object.blurred_image)
    cv2.imshow("Image", find_object.cv_image)
    cv2.imshow("Thresh", find_object.thresh_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()