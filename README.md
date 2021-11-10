# Files making `utt2spk` & `wav.scp`

## 1. 환경
디렉토리 `sample` 안에 `train` 디렉토리와 `test` 디렉토리가 존재함.

---

## 2. 실행 방법
`DATA_DIR`에 샘플에 대한 경로를 적어줌.
> e.g. DATA_DIR = "/home/thispath/sample/

```Shell
python3 make_utt2spk.py
python3 make_wav.scp.py
```

---
## 3. 결과
sample 디렉토리 내의 train, test 디렉토리 안에 각각 `utt2spk`, `wav.scp`가 생성됨