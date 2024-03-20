# Carton_Convert

<br>

## **Introduction**

사진을 가우시안 블러(GaussianBlur)와 양방향 필터를 사용하여 카툰 느낌으로 변환시켜주는 기능을 구현하고자 한다.

## **Developer**
* 임민규(Lim Mingyu)


## **Set up & Prerequisites**

* Python >= 3.9
* Install python pip.
  * You may need to install first:`python -m pip install opencv-python`

## **Description**
**코드에 대한 내용은 주석을 참고**

* 동영상을 프레임 단위로 가져와 만화 스타일로 변환
  ```bash
  while True:.
   ret, frame = cap.read()

    if not ret:
      break

    cartoon_frame = cartoonize_image(frame)
    cv2.imshow('Cartoonized Video', cartoon_frame)

* Esc 키를 누르면 종료
  ```bash
  if cv2.waitKey(1) == 27:
    break

* 필터를 사용하지 않았을 때와 필터를 사용했을 때 차이
  * 필터를 사용하지 않았을 때
    ![View](https://github.com/limstinger/Carton_Convert/assets/113160281/2d91173c-d75f-4f9a-b1ac-4102b723750a)

  * 필터를 사용했을 때
    ![Carton_View](https://github.com/limstinger/Carton_Convert/assets/113160281/5d1a081c-b741-4e16-b2d4-70aa0396ed2d)

* 카툰 느낌이 나지 않도록 수치를 조정
  * 기존 필터에서 함수의 수치를 조정
    ```bash
    # kisze 수치를 기존보다 작게 조정 (5, 5) -> (3, 3)
    cv2.GaussianBlur(img_small, (3, 3), 0)
    
    # blocksize 수치를 작게 조정 11 -> 3
    cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=3,
                                     C=2)

  * 카툰 느낌이 나지 않는 필터를 사용할 때
    ![NotCarton_View](https://github.com/limstinger/Carton_Convert/assets/113160281/48513bf8-d171-49c9-b178-b2e9571524eb)

## **Limitation**
* 현 코드는 영상을 뽀얗게 만들거나 색의 경계를 나타내는 검은 선을 통해 만화 효과를 낼 수 있었지만, 실제 만화나 애니메이션에서 쓰는 선의 표현이나 채색 기법과는 다르다.<br>
* 특정 만화나 애니메이션의 독특한 스타일을 따라할 수 없다.<br>
* edge 감지 기법으로 윤곽이 두드러지는 기법만 사용했을 뿐, 색상이나 명암으로 만화 효과를 내지 못했다.
