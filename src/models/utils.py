import torch.nn as nn
from modules import Cell


def make_model(model):
    if isinstance(model, dict):
        if 'cell' in model:
            return Cell(model)
        else:
            cell = nn.ModuleDict({})
            for k in model:
                cell[k] = make_model(model[k])
            return cell
    elif isinstance(model, list):
        cell = nn.ModuleList([])
        for i in range(len(model)):
            cell.append(make_model(model[i]))
        return cell
    elif isinstance(model, tuple):
        container = []
        for i in range(len(model)):
            container.append(make_model(model[i]))
        cell = nn.Sequential(*container)
        return cell
    else:
        raise ValueError('wrong model info format')
    return