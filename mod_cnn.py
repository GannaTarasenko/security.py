import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, vocab_size, embed_size, num_classes, kernel_sizes, num_filters):
        super(SimpleCNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.conv_layers = nn.ModuleList([
            nn.Conv1d(in_channels=embed_size, out_channels=num_filters, kernel_size=ks)
            for ks in kernel_sizes
        ])
        self.fc = nn.Linear(num_filters * len(kernel_sizes), num_classes)

    def forward(self, x):
        x = self.embedding(x)
        x = x.permute(0, 2, 1)  # Change the dimension for Conv1d
        conv_outputs = [conv(x) for conv in self.conv_layers]
        pooled_outputs = [nn.functional.max_pool1d(output, output.size(2)).squeeze(2) for output in conv_outputs]
        x = torch.cat(pooled_outputs, 1)
        x = self.fc(x)
        return x
