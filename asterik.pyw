def censor(text,word):
  for i in text:
    for j in word:
      if i==j:
          new_word=text.replace(word,"*"*len(word))
  return new_word        
       
        


print(censor("hey hey hey","hey"))
