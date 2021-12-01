

def play(data, maxval=9, times=100):
    current, link_in, link_middle, link_out, new_current = data[:5]
    data = {data[i]: data[(i + 1) % maxval] for i in range(maxval)}

    def find_link(new):
        return [(new - x if new - x > 0 else new - x + maxval) for x in range(1, 4) if
                (new - x if new - x > 0 else new - x + maxval) not in [link_in, link_middle, link_out]][0]

    for x in range(times):
        data[current], data[find_link(current)], data[link_out], current = new_current, link_in, data[
            find_link(current)], new_current
        link_in, link_middle, link_out, new_current = data[new_current], data[data[new_current]], data[
            data[data[new_current]]], data[data[data[data[new_current]]]]
    return data


with open("input.txt", 'r') as file:
    data = [int(x) for x in file.read()]
    data_p1, x, p1 = play(data), 1, []
    for i in range(1, len(data)):
        x = data_p1[x]
        p1.append(x)
    print('Part 1: {}'.format(''.join([str(x) for x in p1])))
    data = play(data + [x for x in range(len(data) + 1, 1000001)], maxval=1000000, times=10000000)
    print('Part 2: {}'.format(data[1] * data[data[1]]))
