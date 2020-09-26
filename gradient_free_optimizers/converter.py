# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np


class Converter:
    def __init__(self, search_space):
        self.search_space = search_space
        self.dim_sizes = np.array([len(array) - 1 for array in search_space.values()])

    def position2value(self, position):
        value = []
        for n, space_dim in enumerate(self.search_space.values()):
            value.append(space_dim[position[n]])

        return value

    def value2position(self, value):
        position = []
        for n, space_dim in enumerate(self.search_space.values()):
            pos = np.abs(value[n] - space_dim).argmin()
            position.append(pos)

        return np.array(position)

    def value2para(self, value):
        para = {}
        for key, p_ in zip(self.search_space.keys(), value):
            para[key] = p_

        return para

    def para2value(self, para):
        value = list(para.values())
        return value

    def values2positions(self, values):
        positions_temp = []
        values_np = np.array(values)

        for n, space_dim in enumerate(self.search_space.values()):
            values_1d = values_np[:, n]
            m_conv = np.abs(values_1d - space_dim[:, np.newaxis])
            pos_list = m_conv.argmin(0)

            positions_temp.append(pos_list)

        positions = list(np.array(positions_temp).T)

        return positions

    def positions2values(self, positions):
        values_temp = []
        positions_np = np.array(positions)

        for n, space_dim in enumerate(self.search_space.values()):
            pos_1d = positions_np[:, n]
            value_ = np.take(space_dim, pos_1d, axis=0)
            values_temp.append(value_)

        values = list(np.array(values_temp).T)
        return values

    def positions_scores2memory_dict(self, positions, scores):
        value_tuple_list = list(map(tuple, positions))
        memory_dict = dict(zip(value_tuple_list, scores))

        return memory_dict

    def memory_dict2positions_scores(self, memory_dict):
        positions = [np.array(pos) for pos in list(memory_dict.keys())]
        scores = list(memory_dict.values())

        return positions, scores
