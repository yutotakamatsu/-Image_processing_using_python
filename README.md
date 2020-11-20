[Qiita](https://qiita.com/YutoTakamatsu/private/b68971d66c940029bb38)

# Shellとは
pythonを動かすためには、Shellを用いてPCに処理をさせるように命令をしなければいけない。
実行したいpythonのファイルが置いてあるフォルダの中で命令を行わないとエラーを発生するため、pythonを勉強する前に、まずは、Shellを勉強しなければならない。
シェルはOSの中核であるカーネルと対話するためソフトウェアのことです。表現を変えれば、人間とPC(カーネル)は直接やりとりができないのでシェルがやり取りの仲介役となってくれているというもの。

#Shell　覚えておいた方が良い

###指定したフォルダに移動する
```terminal:terminal
$ cd 相対パス/絶対パス
```

###現在操作している絶対パスを取得する
```terminal:terminal
$ pwd or @cd 
```

###現在操作しているフォルダ内を確認する
```terminal:terminal
$ Mac : ls, Windows : dir
```

###指定したファイル名の空ファイルを作成する
```terminal:terminal
$ touch ファイル名
```

###指定したファイル・フォルダを削除する
```terminal:terminal
$ rm ファイル名/フォルダ名
$ rm -r ファイル名/フォルダ名
#フォルダーを削除する際には-rを付ける必要がある
```

###ファイル名の変更
```terminal:terminal
$ mv 変更するファイル名　変更後のファイル名
```

###ファイルの移動
```terminal:terminal
$ mv 移動したいファイル名　移動先のフォルダ名
```

###フォルダを作成する
```terminal:terminal
$ mkdir フォルダ名
```

###pythonを実行する
```terminal:terminal
python/python3
#pythonを実行する
python/python3 ファイル名
#指定したpythonfileをpythonで実行する
```


#覚えておくと便利
###ファイル内の確認
```terminal:terminal
$ cat ファイル名
```

###ターミナル内でテキストエディタを開く
```terminal:terminal
$ nano ファイル名
```

###ファイルの場所を検索する
```terminal:terminal
$ find ファイル名
```

#pythonをインストールしよう
https://www.python.org/downloads/
![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/f92fbb4a-2a90-a8e5-23e2-a7321ec227bf.png)

#Opencvのインストールをしよう

```terminal:terminal
#pythonと実行してpython3が動く場合
$ pip install opencv-python 
#python3と実行してpython3が動く場合
$ pip3 install opencv-python
```
##インストールできるか確認しよう
```terminal:terminal
$ python3
Python 3.8.2 (default, Sep 24 2020, 19:37:08)
[Clang 12.0.0 (clang-1200.0.32.21)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
>>> 
```
インストールが完了していればエラーがでない

###[github](https://github.com/yutotakamatsu/Image_processing_using_python)
ここからpythonファイルをダウンロードしてください。

#画像を表示してみよう
```python:list1.py
#open cvを読み込んでいる
import cv2

#img_pathに画像のパスを通している
img_path = 'img/lena.jpg'

#imgにcv2を用いてimg_pathで指定したパスの画像を読み込んでいる
img = cv2.imread(img_path, 1)

#imgに挿入した画像を表示している
cv2.imshow('img', img)

#何も書かないとすぐに表示ウィンドウが消えてしまうため消えないように処理している
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

```
<img src = 'https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/abec3f88-1263-bd01-c8f8-ae9ad8568f51.png' width=200>

このように画像が表示されれば成功

#画像はどのような形になっているのか
![スクリーンショット 2020-11-20 14.25.06.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/669d8993-cf4f-ea2c-0e52-2e051f5b4130.png)
この画像がどのような形で作られているのかを確認してみよう

```python:list2.py
import cv2

img_path = 'img/img.png'

img = cv2.imread(img_path, 1)

print(f'img : {img}')
```
```terminal:terminal
 [[[255   0   0]
  [  0 255   0]
  [  0   0 255]]

 [[255 255 255]
  [192 192 192]
  [  0   0   0]]

 [[255 255   0]
  [255   0 255]
  [  0 255 255]]]
```
このように1ピクセル毎にRGBの値で形作られていることがわかる

#動画を再生してみよう
```python:list3.py
import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture("movie/uchiage.mp4")

    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow("Flame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

<img src='https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/517357/bad69d3c-6740-a033-2420-77a9bdce9532.gif' width=400>

このように表示されれば成功

#カメラを使って動画を撮影してみよう
```python:list4.py
import cv2

cap = cv2.VideoCapture(0)
fps = 30

size = (640, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output.avi', fourcc, fps, size)

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    video.write(frame)
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cap.release()
        video.release()
        cv2.destroyAllWindows()
```

カメラが立ち上がって動画が再生され、'output.avi'が保存されれば成功。

