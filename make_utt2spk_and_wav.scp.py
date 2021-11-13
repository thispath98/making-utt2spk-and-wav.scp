import os
import argparse

TYPE = ["train", "test"]
FILES = ["wav.scp", "utt2spk"]


def main():
    # Required parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", default=None, type=str,
                        required=True, help="directory containing sample data")
    args = parser.parse_args()

    for type in TYPE:
        PATH = os.path.join(args.data_dir, type)
        dir_list = os.listdir(PATH)

        print("Making {} in {} directory...".format(FILES[0], type))
        with open(os.path.join(PATH, FILES[0]), 'w') as f:
            for directory in dir_list:
                target = os.path.join(PATH, directory)
                if not os.path.isdir(target):
                    continue

                wav_list = os.listdir(target + "/")
                for wav in wav_list:
                    if wav.endswith(".wav"):
                        utterance_id = directory + "_" + wav.rstrip(".wav")
                        wav_path = target + "/" + wav
                        f.write(" ".join([utterance_id, wav_path]) + "\n")
        print("done")

        print("Making {} in {} directory...".format(FILES[1], type))
        with open(os.path.join(PATH, FILES[1]), 'w') as f:
            for directory in dir_list:
                target = os.path.join(PATH, directory)
                if not os.path.isdir(target):
                    continue

                wav_list = os.listdir(target)
                for wav in wav_list:
                    if wav.endswith(".wav"):
                        utterance_id = directory + "_" + wav.rstrip(".wav")
                        speaker_id = directory
                        f.write(" ".join([utterance_id, speaker_id]) + "\n")
        print("done")


if __name__ == "__main__":
    main()
