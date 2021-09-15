from translate import Translator

s = Translator(from_lang="Tamil",to_lang="english")

res= s.translate("ஹலோ வேர்ல்ட்")

print("In english, the hello world is: " ,res)