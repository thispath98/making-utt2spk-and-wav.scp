# Files making `utt2spk` & `wav.scp`

## 1. Requirements
* 디렉토리 `sample` 안에 `train` 디렉토리와 `test` 디렉토리가 존재함.
* Ubuntu==18.04.6

---

## 2. 실행 방법

```Shell
$ python make_utt2spk_and_wav.scp.py --data_dir /home/user/sample

Making wav.scp in train directory...
done
Making utt2spk in train directory...
done
Making wav.scp in test directory...
done
Making utt2spk in test directory...
done
```

---
## 3. 결과
sample 디렉토리 내의 train, test 디렉토리 안에 각각 `utt2spk`, `wav.scp`가 생성됨