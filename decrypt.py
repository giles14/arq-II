from cryptography.fernet import Fernet
key = 'UM_Xip80dCSWhVkGRsxiNwf21ceCjWiWK8JT1OSTiPA='
token1 = 'gAAAAABiJ6CPVOphNbdsTHUr3nIL3Qigv8d8Zevf8Zh7suhlXBEjgWdfzh7R2XZXI0MoC2MnHf8OWT72QKDPXdakG0ON6JVDjCyz4p_Lj0bP15wZdwvEFA53hqVFr_dbfxXBwVo4-WG8'
token1 = token1.encode()
token2 = 'gAAAAABiJ6CP1U4FyroAioxHWN8o7XGChTw57D3GFyvtXvxoF-tJ3grWGA2n4c_moau3ZKTheGfwsCrk1XicysiwhwA0j6EhZ5dVNMkR9sqXFJudd61cu_2x88VXUxgI-b1ivJ-XPTC8'
token2 = token2.encode()
toker3 = 'gAAAAABiJ-x1GNpfwuX6YZ7xOtp8Bk-Ca39uhdB2DhMETRi3b7cIML-q6Er7s_LTt1w8ZWrPSR-J2RU7dNnwPLIB5CSWE4-TWyZWDr4JPSPPfaM5IK7GtM8tXRkgoQ6YvkUlPLZ8dQPV'
def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

print(decrypt(token1, key).decode())
print(decrypt(token2, key).decode())