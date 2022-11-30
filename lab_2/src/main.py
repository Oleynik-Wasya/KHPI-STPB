import aes, os, utils

key = "Hi I am grooooot"
text = "And I Am Vasyyyl"

main_key = utils.translate_string_into_hex_str(key)
main_text = utils.translate_string_into_hex_str(text)
round_keys = utils.find_all_round_keys(main_key)
encrypt_text = aes.encrypt(main_text, round_keys)
print("Key : \'{}\'".format(key))
print("Message Text : \'{}\'".format(text))
print("Encrypted Text in HEX:", encrypt_text)
