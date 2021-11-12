import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    
    # Required parameter
    parser.add_argument(
            "--data_dir",
            default=None,
            type=str,
            required=True,
            help="directory containing sample data"
        )

    args = parser.parse_args()
    
    TYPE = ["train", "test"]
    FILES = ["wav.scp", "utt2spk"]

    for type in TYPE:
        PATH = "{}/{}/".format(args.data_dir, type)
        dir_list = os.listdir(PATH)

        print("Making {} in {} directory...".format(FILES[0], type))
        with open(PATH + FILES[0], 'w') as f:
            for _dir in dir_list:
                if not os.path.isdir(PATH + _dir):
                    continue
                wav_list = os.listdir(PATH + _dir + "/")
                for wav in wav_list:
                    if wav.endswith(".wav"):
                        name = wav.rstrip(".wav")
                        utterance_id = _dir + "_" + name + " "
                        wav_path = PATH + _dir + "/" + wav
                        f.write(" ".join([utterance_id + wav_path]) + "\n")
        print("done")

        print("Making {} in {} directory...".format(FILES[1], type))
        with open(PATH + FILES[1], 'w') as f:
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
        print("done")


if __name__=="__main__":
    main()