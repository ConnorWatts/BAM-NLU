from configue import Config

import json


def main():

    topdir = "C:/Users/cwatts/BAM NLU/BAM-NLU"
    model_name = "BAM-NLU"
    hparams = '{}'

    config = Config(topdir,model_name,**json.loads(hparams))

    pass

if __name__ == "__main__":
    main()