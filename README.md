This is term project of Sejong 2021 OpenSource Introduction <br>
[by JeongJun.Bae](https://github.com/GalaxyOverMe) / [by DongYeok.Kim](https://github.com/Ameri-Kano)

# 동적 틀린그림찾기
<hr>
<h2> summary </h2>

python OpenCV를 이용하여 틀린그림찾기 이미지를 생성합니다.

틀린그림찾기를 하기위해서는 원본 이미지와, 틀린 그림 이미지가 1개씩 필요합니다. 

원본 이미지로부터 틀린 그림 이미지를 만들기 위해

객체 탐지(Object Detection) 와 객체 삭제(Image Inpainting 방법을 이용합니다)를 이용합니다.

객체 탐지 방법으로 Morphological Edge -> contour 방식을

객체 삭제 방법으로 cv2.contrib.xphoto.inpaint 함수를 사용하였습니다.


<img width="1200" alt="고흐" src="https://user-images.githubusercontent.com/80030558/120098399-ad203880-c170-11eb-9f31-b48e09145a3f.png">
<pre>               원본 그림                                  틀린 그림                                    정답 그림 </pre>
<hr>
<h2>  Introduction  </h2> <br>

![image](https://user-images.githubusercontent.com/80030558/113543977-699ec780-9622-11eb-8f4b-15628f6d28e7.png)
![image](https://user-images.githubusercontent.com/80030558/113543986-6dcae500-9622-11eb-9b9e-46d0a81c5e09.png)
<pre>                      &lt;<b>A</b>&gt;                                                    &lt;<b>B</b>&gt;</pre>
![image](https://user-images.githubusercontent.com/80030558/113543234-e7fa6a00-9620-11eb-89df-dc6fb069cc87.png)

![image](https://user-images.githubusercontent.com/80030558/113543428-5808f000-9621-11eb-9941-5e9a9ded49d5.png)
<pre>                                                    전통적인 방법</pre>
Traditional way to create FindTheDifference problem is first make 'A', then paint some object to make 'B' <br>
틀린그림찾기를 만드는 전통적인 방법은 원본그림 <b>A</b>에 몇가지 객체를 그려넣은 <b>B</b>를 만드는 것입니다.

![image](https://user-images.githubusercontent.com/80030558/113543738-f9904180-9621-11eb-8c1b-01de27dca12a.png)<br>
<pre>                                               컴퓨터를 이용한 방법</pre>
With Computer, it is much easier to start with 'B', and remove some obejct to make 'A' <br>
이 프로젝트에서는 이미지 <b>B</b>로 시작해 몇가지 객체를 지운 <b>A</b>를 만듭니다.
<hr>

<h2>  samples  </h2>
<pre>               원본 그림                                  틀린 그림                                    정답 그림 </pre>
<img width="1200" alt="sample1" src="https://user-images.githubusercontent.com/80030558/120098950-b068f380-c173-11eb-957f-82abfa61ae98.png">
<img width="1200" alt="sample2" src="https://user-images.githubusercontent.com/80030558/120098817-f6718780-c172-11eb-9e35-6e008d0e0004.png">
<img width="1200" alt="sample3" src="https://user-images.githubusercontent.com/80030558/120098896-6f70df00-c173-11eb-96b2-db1eaec1a60e.png">

