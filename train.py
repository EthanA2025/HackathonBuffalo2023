import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd
from sequencer import SequencePredictor


def train(model, criterion, optimizer, dataloader, device):
    model.train()
    for batch in dataloader:
        # Unpack batch
        sequences, lengths, targets = batch

        # Move to device
        sequences = sequences.to(device)
        lengths = lengths.to(device)
        targets = targets.to(device)

        # Clear gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(sequences, lengths)

        # Compute loss
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()


def evaluate(model, criterion, dataloader, device):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for batch in dataloader:
            # Unpack batch
            sequences, lengths, targets = batch

            # Move to device
            sequences = sequences.to(device)
            lengths = lengths.to(device)
            targets = targets.to(device)

            # Forward pass
            outputs = model(sequences, lengths)

            # Compute loss
            loss = criterion(outputs, targets)
            total_loss += loss.item()
    return total_loss / len(dataloader)


class SequenceDataset(Dataset):
    def __init__(self, csv_file):
        # Load the data
        self.dataframe = pd.read_csv(csv_file)

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        row = self.dataframe.iloc[idx]

        # Ignore the identifier column
        sequence = torch.tensor(row[1:].values, dtype=torch.float32)

        # The target is the last value in the sequence
        target = sequence[-1]

        # The input sequence is all but the last value
        sequence = sequence[:-1]

        # Compute the sequence length
        length = torch.tensor(len(sequence), dtype=torch.long)

        return sequence, length, target


def collate_fn(batch):
    sequences, lengths, targets = zip(*batch)

    # Pad the sequences
    sequences = torch.nn.utils.rnn.pad_sequence(sequences, batch_first=True)

    # Stack the lengths and targets into tensors
    lengths = torch.stack(lengths)
    targets = torch.stack(targets)

    return sequences, lengths, targets


def get_dataloader(csv_file, batch_size=32):
    dataset = SequenceDataset(csv_file)

    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,  # Shuffle for training
        collate_fn=collate_fn,  # Use a custom collate function to handle variable-length sequences
    )

    return dataloader


if __name__ == "__main__":
    # Create the model
    model = SequencePredictor(input_size=1, hidden_size=50, num_layers=1, output_size=1)

    # Define loss function and optimizer
    criterion = nn.MSELoss()  # Mean squared error for regression task
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    dataloader = get_dataloader('student_data.csv')

    train(model, criterion, optimizer, dataloader, device)

    print(evaluate(model, criterion, dataloader, device))
