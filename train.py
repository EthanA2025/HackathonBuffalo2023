import torch
import torch.nn as nn
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


if __name__ == "__main__":
    # Create the model
    model = SequencePredictor(input_size=1, hidden_size=50, num_layers=1, output_size=1)

    # Define loss function and optimizer
    criterion = nn.MSELoss()  # Mean squared error for regression task
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    train(model, criterion, optimizer, dataloader, device)

    print(evaluate(model, criterion, dataloader, device))