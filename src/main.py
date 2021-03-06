import argparse

from torch_geometric.transforms import NormalizeFeatures

from dataset_loader import get_dataset
from model_loader import get_model_by_name
from model_tester import ModelTester

parser = argparse.ArgumentParser(
    description="A small utility to train a given GNN model on a given dataset."
)
parser.add_argument(
    "--dataset",
    type=str,
    required=True,
    help="Dataset name (for example, KarateClub or Planetoid/Cora)",
)
parser.add_argument(
    "--model",
    type=str,
    required=True,
    help="Model name (for example, GCNConv)",
)
parser.add_argument(
    "--epochs",
    type=int,
    required=True,
    help="Number of epochs",
)
parser.add_argument(
    "--learning_rate",
    type=float,
    required=True,
    help="Learning rate",
)


def main():
    args = parser.parse_args()

    dataset_name = args.dataset
    model_name: str = args.model
    epochs_num: int = args.epochs
    learning_rate: float = args.learning_rate

    dataset = get_dataset(
        name=dataset_name,
        transform=NormalizeFeatures,
    )

    Model = get_model_by_name(model_name)

    print(dataset[0])
    print(dataset.num_node_features)

    model = Model(
        num_node_features=dataset.num_node_features,
        num_classes=dataset.num_classes,
    )

    

    tester = ModelTester(
        dataset_name,
        model_name,
        model,
        epochs_num,
        learning_rate,
        dataset[0],
    )
    tester.train_and_test()
    tester.to_numpy_file()


if __name__ == "__main__":
    main()
