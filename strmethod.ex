#Elixir string and its methods

#string concatenation

prog_name1="Elixir"
prog_lang="Programming Language"
z= prog_name1<> " "<> prog_lang
IO.puts("The String Concatenated is: #{z}")

#finding the length of the string
IO.puts("The String length of the prog1 is: ")
IO.puts(String.length(prog_name1))

#reversing the string
str1="Programming"
str_rev=String.reverse(str1)
IO.puts("The reversed string is: #{str_rev}")

#string comparision
var_1="Hello world"
var_2="Hello world"
_var_3="Hello Elixir"  #unused variable should  be prefix by underscore
if var_1 ===var_2 do
  IO.puts("#{var_1} is equal to #{var_2}")
else
  IO.puts("#{var_1} is not equal to #{var_2}")
end

#string matching
IO.puts(String.match?("Hello",~r/Hello/)) #returns true
IO.puts(String.match?("Elixir",~r/Hello/))  #returns false

#more string functions
var_3="elixir"
str_cap=String.upcase(var_3) #it changes the  string into uppercase

IO.puts("the String in uppercase: #{str_cap}")

var_4 = "PROGRAMMING"
str_low=String.downcase(var_4) # it changes the string into lowercase
IO.puts("the string in lowercase: #{str_low}")

 var_5="Elixir Programming"
 str_split=String.split(var_5) #it splits the string by whitespace
 IO.puts("The Split String is: #{str_split}")

 str_slice=String.slice(var_5,0,3) #it slices the  given string from 0 position to 3rd position
IO.puts("the Sliced String is: #{str_slice}")

str_first= String.first(var_5)  #returns the first character

IO.puts("the first character is: #{str_first}")

str_last=String.last(var_5) #returns the last character

IO.puts("The last character is: #{str_last}")

IO.puts(String.ends_with?(var_5,"Programming")) #returns true because the string is ended with Programming
IO.puts(String.ends_with?(var_5,"programming")) #returns false

var_6="elixir"
str_capi=String.capitalize(var_6)
IO.puts("the capatilise string is: #{str_capi}")

IO.puts(String.contains?(var_5,"Elixir")) #returns true if contents are there in the string
IO.puts(String.contains?(var_5,"language")) #returns false

str_pos=String.at(var_6,1)

IO.puts("the character at 1 :#{str_pos}") #returns the character at the first position

IO.puts("Thanks for using Elixir programming Language :)")
