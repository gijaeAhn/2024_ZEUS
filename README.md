# 2024_ZEUS


## Setup


1. Install Ros Noetic (Ubuntu 20.04)  & cuda??
2. Install Anaconda 

3. install webots 2022b
    -- Webots 깃헙에서 Release가서 2022b debian pkg 다운 받아서 설치
    -- Dependeies 설치하기 

4. build catkin(Ros Packages )
```bash
bash ./build_catkin.sh 
```
5. install pybind Lib
```bash
bash ./install_pybind.sh
```

6. Webots 실험용 
    -- Webots 실행후, 
    -- webot_client.py 실행
    -- Tools/positionLogger.py 실행
    -- Frame은 로봇 베이스 기준 FLU( Front , Left ,UP)
    -- i : 누르면 이니셜 포지션
    -- w,s : x 방향 전진 후진
    -- a,d : y 방향 전진 후진
    -- q,e : z 방향 상승 하강