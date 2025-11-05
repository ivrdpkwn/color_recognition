import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # 转换到 HSV 色彩空间
    hihgt, width, _ = frame.shape # 获取图像的高度、宽度
    cx, cy = width // 2, hihgt // 2 # 计算中心点
    
    pixel_center = hsv_frame[cy, cx]  # 获取中心点的 HSV 值
    h, s, v = int(pixel_center[0]), int(pixel_center[1]), int(pixel_center[2])
 
    # 默认颜色
    color = "Undefined"

    # 判断亮度优先：黑、灰、白
    if v < 40:
        color = "Black"
    elif s < 40:
        if v > 200:
            color = "White"
        else:
            color = "Gray"
    else:
        # 其他有色部分根据Hue判断
        if (h >= 0 and h <= 10) or (h >= 160 and h <= 179):
            color = "Red"
        elif h >= 11 and h <= 25:
            if v < 150:
                color = "Brown"
            else:
                color = "Orange"
        elif h >= 26 and h <= 34:
            color = "Yellow"
        elif h >= 35 and h <= 85:
            color = "Green"
        elif h >= 86 and h <= 100:
            color = "Cyan"
        elif h >= 101 and h <= 130:
            color = "Blue"
        elif h >= 131 and h <= 159:
            color = "Purple"

    # 绘制信息
    cv2.putText(frame, f"{color}  H:{h} S:{s} V:{v}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), 3)
   
   # 显示视频流
    cv2.imshow('Frame', frame)

    key = cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()
