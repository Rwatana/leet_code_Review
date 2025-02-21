sentence = input("問題を入力してください")
bra_sentence = sentence.replace(' ', '_')
branch_sentence = bra_sentence.replace('.', '')
branch_lower_sentence = branch_sentence.lower()
# go file name
print("touch", branch_lower_sentence + ".go")
print("git add .")
print('git commit -m "', branch_sentence, '"', sep='')
print("git push origin main")
