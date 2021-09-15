import json

# key:value mapping

programming_lang={
    "Python" :"1",
    "JavaScript":"2",
    "Java":"3",
    "Kotlin":"4",
    "PHP":"5",
    "Perl":"6",
    "C#":"7",
    "C":"8",
    "C++":"9",
    "Julia":"10"

    }

b= json.dumps(programming_lang)
print(b)
