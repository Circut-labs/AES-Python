import AES_Python.AES as AES

def test_aes_key_expantion_128bit():
    round_keys, nr = AES.keyExpansion("00000000000000000000000000000000")

    assert round_keys == [
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (98, 99, 99, 99, 98, 99, 99, 99, 98, 99, 99, 99, 98, 99, 99, 99),
        (155, 152, 152, 201, 249, 251, 251, 170, 155, 152, 152, 201, 249, 251, 251, 170),
        (144, 151, 52, 80, 105, 108, 207, 250, 242, 244, 87, 51, 11, 15, 172, 153),
        (238, 6, 218, 123, 135, 106, 21, 129, 117, 158, 66, 178, 126, 145, 238, 43),
        (127, 46, 43, 136, 248, 68, 62, 9, 141, 218, 124, 187, 243, 75, 146, 144),
        (236, 97, 75, 133, 20, 37, 117, 140, 153, 255, 9, 55, 106, 180, 155, 167),
        (33, 117, 23, 135, 53, 80, 98, 11, 172, 175, 107, 60, 198, 27, 240, 155),
        (14, 249, 3, 51, 59, 169, 97, 56, 151, 6, 10, 4, 81, 29, 250, 159),
        (177, 212, 216, 226, 138, 125, 185, 218, 29, 123, 179, 222, 76, 102, 73, 65),
        (180, 239, 91, 203, 62, 146, 226, 17, 35, 233, 81, 207, 111, 143, 24, 142)
        ]
    assert nr == 11

def test_aes_key_expantion_192bit():
    round_keys, nr = AES.keyExpansion("000000000000000000000000000000000000000000000000")

    assert round_keys == [
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 98, 99, 99, 99, 98, 99, 99, 99),
        (98, 99, 99, 99, 98, 99, 99, 99, 98, 99, 99, 99, 98, 99, 99, 99),
        (155, 152, 152, 201, 249, 251, 251, 170, 155, 152, 152, 201, 249, 251, 251, 170),
        (155, 152, 152, 201, 249, 251, 251, 170, 144, 151, 52, 80, 105, 108, 207, 250),
        (242, 244, 87, 51, 11, 15, 172, 153, 144, 151, 52, 80, 105, 108, 207, 250),
        (200, 29, 25, 169, 161, 113, 214, 83, 83, 133, 129, 96, 88, 138, 45, 249),
        (200, 29, 25, 169, 161, 113, 214, 83, 123, 235, 244, 155, 218, 154, 34, 200),
        (137, 31, 163, 168, 209, 149, 142, 81, 25, 136, 151, 248, 184, 249, 65, 171),
        (194, 104, 150, 247, 24, 242, 180, 63, 145, 237, 23, 151, 64, 120, 153, 198),
        (89, 240, 14, 62, 225, 9, 79, 149, 131, 236, 188, 15, 155, 30, 8, 48),
        (10, 243, 31, 167, 74, 139, 134, 97, 19, 123, 136, 95, 242, 114, 199, 202),
        (67, 42, 200, 134, 216, 52, 192, 182, 210, 199, 223, 17, 152, 76, 89, 112)
        ]
    assert nr == 13

def test_aes_key_expansion_256bit():
    round_keys, nr = AES.keyExpansion("0000000000000000000000000000000000000000000000000000000000000000")

    assert round_keys == [
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (98, 99, 99, 99, 98, 99, 99, 99, 98, 99, 99, 99, 98, 99, 99, 99),
        (170, 251, 251, 251, 170, 251, 251, 251, 170, 251, 251, 251, 170, 251, 251, 251),
        (111, 108, 108, 207, 13, 15, 15, 172, 111, 108, 108, 207, 13, 15, 15, 172),
        (125, 141, 141, 106, 215, 118, 118, 145, 125, 141, 141, 106, 215, 118, 118, 145),
        (83, 84, 237, 193, 94, 91, 226, 109, 49, 55, 142, 162, 60, 56, 129, 14),
        (150, 138, 129, 193, 65, 252, 247, 80, 60, 113, 122, 58, 235, 7, 12, 171),
        (158, 170, 143, 40, 192, 241, 109, 69, 241, 198, 227, 231, 205, 254, 98, 233),
        (43, 49, 43, 223, 106, 205, 220, 143, 86, 188, 166, 181, 189, 187, 170, 30),
        (100, 6, 253, 82, 164, 247, 144, 23, 85, 49, 115, 240, 152, 207, 17, 25),
        (109, 187, 169, 11, 7, 118, 117, 132, 81, 202, 211, 49, 236, 113, 121, 47),
        (231, 176, 232, 156, 67, 71, 120, 139, 22, 118, 11, 123, 142, 185, 26, 98),
        (116, 237, 11, 161, 115, 155, 126, 37, 34, 81, 173, 20, 206, 32, 212, 59),
        (16, 248, 10, 23, 83, 191, 114, 156, 69, 201, 121, 231, 203, 112, 99, 133)
        ]
    assert nr == 15
