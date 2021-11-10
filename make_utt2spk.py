import os
USER_NAME = ""
TYPE = ""

url = f"/home/{USER_NAME}/sample/{TYPE}/"
dir_list = os.listdir(url)

with open(url + "utt2spk", 'w') as f:
    for _dir in dir_list:
        if not os.path.isdir(url + _dir):
            continue
        wav_list = os.listdir(url + _dir + "/")
        for wav in wav_list:
            if wav.endswith(".wav"):
                name = wav.rstrip(".wav")
                utterance_id = _dir + "_" + name
                speaker_id = _dir
                f.write(" ".join([utterance_id, speaker_id]) + "\n")