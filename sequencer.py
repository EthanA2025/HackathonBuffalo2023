import torch
import torch.nn as nn


class SequencePredictor(nn.Module):
    def __init__(self, input_size=1, hidden_size=20, num_layers=2, output_size=1):
        super(SequencePredictor, self).__init__()

        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, lengths):
        # Pack the input sequences
        x = torch.nn.utils.rnn.pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)

        # Initialize hidden state and cell state
        h0 = torch.zeros(self.num_layers, x.batch_sizes[0], self.hidden_size).to(x.data.device)
        c0 = torch.zeros(self.num_layers, x.batch_sizes[0], self.hidden_size).to(x.data.device)

        out, _ = self.lstm(x, (h0, c0))

        # Unpack the output sequences
        out, _ = torch.nn.utils.rnn.pad_packed_sequence(out, batch_first=True)

        # Select the last valid time step output for each sequence
        out = out[range(out.shape[0]), lengths - 1, :]

        # Pass through output layer and return
        out = self.fc(out)
        return out
