
import argparse

def main():
    pass

def get_args():

    parser = argparse.ArgumentParser(description='DQN Pairs Trading')

    parser.add_argument("--topdir", type=str, help="Top directory for project", default="C:/Users/cwatts/BAM NLU/BAM-NLU")
    parser.add_argument("--model_name", type=str, help="Name of the model", default="BAM-NLU")

    args = parser.parse_args()

    # Wrapping training configuration into a dictionary
    training_config = dict()
    for arg in vars(args):
        training_config[arg] = getattr(args, arg)

    return training_config




if __name__ == '__main__':
    main(get_args())