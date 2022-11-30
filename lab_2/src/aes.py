import utils

def encrypt(text_hex, all_round_keys):
    state_matrix = utils.generate_4x4_matrix(text_hex)
    round_N_matrix = utils.generate_4x4_matrix(all_round_keys[0])
    current_matrix = utils.add_round_key(state_matrix, round_N_matrix)

    for i in range(1, utils.ROUND):
        utils.substitute_bytes(current_matrix, True)
        utils.shift_row(current_matrix)
        utils.mix_columns(current_matrix, True)
        current_matrix = utils.add_round_key(current_matrix, utils.generate_4x4_matrix(all_round_keys[i]))

    utils.substitute_bytes(current_matrix, True)
    utils.shift_row(current_matrix)
    cipher_text_matrix = utils.add_round_key(current_matrix, utils.generate_4x4_matrix(all_round_keys[10]))

    cipher_text = []
    for i in range(utils.WORD_LENGTH):
        for j in range(utils.WORD_LENGTH):
            cipher_text.append(cipher_text_matrix[j][i])

    return cipher_text
