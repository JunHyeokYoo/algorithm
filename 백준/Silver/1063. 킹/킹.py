def chess_game(king_pos, stone_pos, moves):
    directions = {
        "R": (0, 1), "L": (0, -1), "B": (-1, 0), "T": (1, 0),
        "RT": (1, 1), "LT": (1, -1), "RB": (-1, 1), "LB": (-1, -1)
    }

    def pos_to_index(pos):
        return int(pos[1]) - 1, ord(pos[0]) - ord('A')

    def index_to_pos(index):
        return chr(index[1] + ord('A')) + str(index[0] + 1)

    def is_valid(index):
        return 0 <= index[0] < 8 and 0 <= index[1] < 8

    king = pos_to_index(king_pos)
    stone = pos_to_index(stone_pos)

    for move in moves:
        d = directions[move]
        new_king = (king[0] + d[0], king[1] + d[1])

        if new_king == stone:
            new_stone = (stone[0] + d[0], stone[1] + d[1])
            if not is_valid(new_stone):
                continue
            stone = new_stone

        if is_valid(new_king):
            king = new_king

    return index_to_pos(king), index_to_pos(stone)

king_pos, stone_pos, n = input().split()
n = int(n)
moves = [input().strip() for _ in range(n)]

final_king, final_stone = chess_game(king_pos, stone_pos, moves)
print(final_king)
print(final_stone)
