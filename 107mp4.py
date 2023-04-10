import cv2
import  os
import  sys

# 動画ファイルのパスを指定
video_path = "C:\ywork\qtpy\dualHA_BSH2.mp4"

# 動画ファイルを開く
cap = cv2.VideoCapture(video_path)

# 動画ファイルが開けなかった場合はエラーを出力して終了
if not cap.isOpened():
    print("Error opening video file")
    exit()

# 動画ファイルからフレームを取得して処理する
while True:
    # フレームを取得
    ret, frame = cap.read()

    # フレームの取得に失敗した場合はループを抜ける
    if not ret:
        break

    # フレームの処理を行う
    # ...

    # フレームを表示する
    cv2.imshow('Frame', frame)

    # キー入力を待つ
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# メモリを解放してウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
