import cv2
import numpy as np


def cartoonize_image(img, ds_factor=4, sketch_mode=False):
    # 이미지를 지정된 배율로 축소하여 노이즈를 줄인다.
    img_small = cv2.resize(img, None, fx=1.0 / ds_factor, fy=1.0 / ds_factor, interpolation=cv2.INTER_AREA)

    # 가우시안 블러를 적용하여 더 부드러운 이미지를 얻는다.
    img_small = cv2.GaussianBlur(img_small, (5, 5), 0)

    # 원본 이미지 크기로 다시 확대
    img_output = cv2.resize(img_small, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR)

    # 양방향 필터를 적용하여 에지를 유지하면서 색상을 단순화한다.
    img_output = cv2.bilateralFilter(img_output, 9, 75, 75)

    # 그레이스케일로 변환하고, 적응형 임계값을 적용하여 에지를 감지한다.
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=11,
                                     C=2)

    # 컬러 이미지에 에지 이미지를 합성한다.
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
    img_edge = cv2.resize(img_edge, (img_output.shape[1], img_output.shape[0]), interpolation=cv2.INTER_AREA) # img_output 크기로 조절

    img_cartoon = cv2.bitwise_and(img_output, img_edge)

    # 필요에 따라 스케치 모드를 적용한다.
    if sketch_mode:
        return cv2.cvtColor(img_edge, cv2.COLOR_BGR2GRAY)
    return img_cartoon


def cartoonize_video(video_path):
    # 동영상 파일을 불러온다.
    cap = cv2.VideoCapture(video_path)

    while True:
        # 프레임별로 동영상을 읽습니다.
        ret, frame = cap.read()

        # 동영상이 끝나면 루프를 종료합니다.
        if not ret:
            break

        # 읽은 프레임을 만화 스타일로 변환합니다.
        cartoon_frame = cartoonize_image(frame)

        # 변환된 프레임을 화면에 표시합니다.
        cv2.imshow('Cartoonized Video', cartoon_frame)

        # ESC 키를 누르면 루프를 종료합니다.
        if cv2.waitKey(1) == 27:
            break

    # 동영상 파일을 닫고 모든 창을 종료합니다.
    cap.release()
    cv2.destroyAllWindows()



video_path = 'View.mp4'
cartoonize_video(video_path)

# 이미지를 만화 스타일로 변환
cartoonize_video(video_path)

