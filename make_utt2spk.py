import os
TYPE = ["train", "test"]
DATA_DIR = ""

for type in TYPE:
    PATH = f"{DATA_DIR}/{type}/"
    dir_list = os.listdir(PATH)

    with open(PATH + "utt2spk", 'w') as f:
        for _dir in dir_list:
            if not os.path.isdir(PATH + _dir):
                continue
            wav_list = os.listdir(PATH + _dir + "/")
            for wav in wav_list:
                if wav.endswith(".wav"):
                    name = wav.rstrip(".wav")
                    utterance_id = _dir + "_" + name
                    speaker_id = _dir
                    f.write(" ".join([utterance_id, speaker_id]) + "\n")