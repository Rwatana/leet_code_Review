sentence = input("問題を入力してください")
bra_sentence = sentence.replace(' ', '_')
branch_sentence = bra_sentence.replace('.', '')
branch_lower_sentence = branch_sentence.lower()
print("git checkout -b feature/#", branch_lower_sentence, sep='')

print("git add ", branch_sentence, ".py", sep='')
print('git commit -m "', branch_sentence, '"', sep='')
print("git push origin feature/#", branch_lower_sentence, sep='')
