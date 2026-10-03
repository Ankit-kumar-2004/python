nested_dict={
    "name":"Ankit kumar",
    "subjects":{
        "physics":85,
        "chemistry":89,
        "biology":92
    }
}
print(nested_dict)
print(type(nested_dict))
print(nested_dict["subjects"])
print(nested_dict["subjects"]["physics"])
nested_dict["subjects"]["physics"]=99
print(nested_dict)