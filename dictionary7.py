nested_dict={
    "name":"Ankit kumar",
    "subjects":{
        "physics":85,
        "chemistry":89,
        "biology":92
    }
}
print(nested_dict.get("subjects").get("physics"))
print(nested_dict["name"])