input_string = input("Enter a number words from 1 to 10 seperate with a space: ")

lst = input_string.split(" ")

print("Your words", lst)
#print(len(lst))
if len(lst) < 2: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" "\nYou only filled in", len(lst), "word(s)")
  
elif len(lst) < 3: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became" "\nYou only filled in", len(lst), "word(s)")
  
elif len(lst) < 4: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2],". As if That wasn't bad enough there was a" "\nYou only filled in", len(lst), "word(s)")
  
elif len(lst) < 5: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2], ". As if That wasn't bad enough there was a", lst[3], "apple that looked like a" "\nYou only filled in", len(lst), "word(s)")
  
elif len(lst) < 6: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2], ". As if That wasn't bad enough there was a", lst[3], "apple that looked like a", lst[4], ". I didn't ask for this and I have no idea how fix this!" "\nYou only filled in", len(lst), "word(s)")

elif len(lst) < 7: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2], ". As if That wasn't bad enough there was a", lst[3], "apple that looked like a", lst[4], ". I didn't ask for this and I have no idea how fix this!", "My only choice might be to ", lst[5], "Yea, thats it I'll just do it" "\nYou only filled in", len(lst), "word(s)")

elif len(lst) < 8: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2], ". As if That wasn't bad enough there was a", lst[3], "apple that looked like a", lst[4], ". I didn't ask for this and I have no idea how fix this!", "My only choice might be to ", lst[5], "Yea, thats it I'll just do it. I'll do ", lst[6], "\nYou only filled in", len(lst), "word(s)")

elif len(lst) < 9: print("How could this happen?! how could ", lst[0],"happen!?. I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2], ". As if That wasn't bad enough there was a", lst[3], "apple that looked like a", lst[4], ". I didn't ask for this and I have no idea how fix this!", "My only choice might be to ", lst[5], "Yea, thats it I'll just do it. I'll do",lst[6], "Yes! Yes! But...if this doesn't work", lst[7], " might happen"  "\nYou only filled in", len(lst), "word(s)")
  
else: print("How could this happen?! how could ", lst[0],"happen!? I had no idea it would be this bad" " I ate", lst[1], "and suddenly the entire world became", lst[2], ". As if That wasn't bad enough there was a", lst[3], "apple that looked like a", lst[4], ". I didn't ask for this and I have no idea how fix this!", "My only choice might be to ", lst[5], "Yea, thats it I'll just do it. I'll do",lst[6], "Yes! Yes! But...if this doesn't work", lst[7], " might happen", " Hmm..Theres also",lst[8], " and ", lst[9], "oh no...PIES!")
