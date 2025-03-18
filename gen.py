#inputting part

name= input("Enter the form Name\n")
print("Enter sequence")
lines = []
c=0
while True :
    line =input()
    if line=='done' or line=='d' or line=='do' or line =='don' or line=='' :
        break
    lines.append(line)
    c+=1
count = 0
co =0
i=0 
ind = []
en = []
size=[]
i=0
k=0
r=0
totalEnum=0
while i < c:
    j=0
    while j <len(lines[i]) and not lines[i][j].isalpha():
        j+=1
    if j<len(lines[i]) and(lines[i][j].isalnum() or lines[i][j]=='(' or lines[i][j]==')'):
        s1=j
        j+=1
        while j<len(lines[i]) and lines[i][j].isalnum() :
            
            j+=1
        e1=j
    j+=1
    while j <len(lines[i]) and not lines[i][j].isalpha():
        j+=1
        
    if j<len(lines[i]) and ( lines[i][j].isalnum() or lines[i][j]=='(' or lines[i][j]==')'):
        s2=j
        j+=1
        while j<len(lines[i]) and lines[i][j].isalnum() :
            j+=1
        e2=j
    ind.append([s1,e1,s2,e2])
    if "enum" in lines[i] :
        r=1
        k=j
        while j <len(lines[i]):
            if(lines[i][j]==","):
                r+=1
            j+=1
        j=k
        size.append(r)
        for u in range(r):
            while j <len(lines[i]) and lines[i][j]!='\'':
                j+=1
            j+=1
            s1=j
            while j <len(lines[i]) and lines[i][j]!='\'':
                j+=1
            e1=j
            j+=1
            en.append(lines[i][s1:e1])
            totalEnum+=1
    j+=1
    i+=1


# i=0
# while i<c :
#     if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
#         i+=1
#         continue
#     print("?," , end=" ")
#     i+=1
# print("?" )
# i=0
# while i< (c):
#     if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
#         i+=1
#         continue
#     print(lines[i][ind[i][0]:ind[i][1]],end=",")
#     i+=1


#Frontend code
# Html Part


print(f"\n\n\n<!--Frontend code-->")

print(f"\n\n<!--views/{name}.html-->")

#form part

print(f"<script src=\"https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js\"></script>")

print(f"\n\n<!--Form submission part-->\n\n")
i=0
r=0
k=0
print(f"\n\n\n\n<form enctype=\"multipart/form-data\" id =\"{name}\">")
while i< c:
    print("\n")
    t=lines[i][ind[i][2]:ind[i][3]]
    if t == 'int' :
        t='number'
    elif t== 'varchar' :
      t='text'
    elif t=='enum' :
        print(f"\t<select id=\"{lines[i][ind[i][0]:ind[i][1]]}\" name=\"{lines[i][ind[i][0]:ind[i][1]]}\">")
        for t in range(size[r]):
            print(f"\t\t<option value=\"{en[k]}\">{en[k]}</option>")
            k+=1
        print(f"\t</select>")
        i+=1
        r+=1
        continue
    elif t=='timestamp':
        i+=1
        continue
    elif t=='datetime' :
        t='datetime-local'
    elif t =='decimal':
        print(f"\t<input type=\"decimalInput\" id=\"{lines[i][ind[i][0]:ind[i][1]]}\" placeholder=\"{lines[i][ind[i][0]:ind[i][1]]}\" step=\"0.01\"/> ", end = "")
        i+=1
        continue
    elif t=='tinyint':
        t='number'

    print(f"\t<input type=\"{t}\" id=\"{lines[i][ind[i][0]:ind[i][1]]}\" placeholder=\"{lines[i][ind[i][0]:ind[i][1]]}\"/> ", end = "")
    i+=1
print(f"\n\n<input type=\"submit\" id =\"{name}Sub\"/>\n\n</form>")
i=0
i=0 
k=0

#Filter Search HTml Part
#Radio button and search bar
print(f"\n\n<!--Radio button and search bar-->\n\n")
print(f"\n\n<form id =\"searchWindow\">\n  ")
print(f"\n\n<input type=\"text\" placeholder=\"Search\" id= \"searchBar\"/>")
print(f"\n\n<ul id=\"searchList\"></ul>")
print(f"\n\n<button id =\"searchBtn\"> &#x1F50D</button> ")
r=0
while i<c:
    if "enum" in lines[i] :
        for t in range(size[r]):
            print(f"\t\t<input type=\"radio\" name=\"{lines[i][ind[i][0]:ind[i][1]]}Choice\" value=\"{en[k]}\">{en[k]}</input>")
            k+=1
            print(f"\n")
        
        r+=1
    i+=1
print(f"\n</form>\n\n")
print(f"\n<li id=\"{name}List\"></li>\n\n")
print(f"\n\n<script src=\"{name}.js\"></script>\n\n")
i=0


#Frontend code
#Javascript part

print(f"\n\n// views/{name}.js\n\n")

print(f"\nconst {name}=document.getElementById(\'{name}\') ;")
#add{name}

print(f"\n\nget{name}()// Do not delete this it must be called at the start")
print(f"\n\n //add{name}\n\n")
print(f"{name}.addEventListener(\'submit\' , (e)=>\n ")
print("{e.preventDefault();\n")
while i<c :
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print(f"const {lines[i][ind[i][0]:ind[i][1]]}= document.getElementById(\'{lines[i][ind[i][0]:ind[i][1]]}\').value.trim()\n")
    i+=1
print(f"const formData=new FormData()")
i=0
while i<c :
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print(f"formData.append(\'{lines[i][ind[i][0]:ind[i][1]]}\',{lines[i][ind[i][0]:ind[i][1]]})")
    i+=1
i=0
print(f"const {name}Data= {{")
while i<c -1:
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print(lines[i][ind[i][0]:ind[i][1]]," ,",end="")
    i+=1
if(lines[i][ind[i][2]:ind[i][3]]!='timestamp'):
    print(lines[i][ind[i][0]:ind[i][1]],"",end="")
print("};\n")
print(f"const res =fetch('/{name}',{{method:\'POST\',body:formData}}).then(data=>data.json()).catch(err => console.log(\"An error occured\" , err));")
print(f"const response =fetch('/{name}',{{method:\'POST\',headers :{{\'Content-Type\':\'application/json\'}},body:JSON.stringify({name}Data)}}).then(data=>data.json()).catch(err => console.log(\"An error occured\" , err));")
print(f"if(response.ok)\n get{name}();")
print(f"}});")

#get{name}Like
#unconventional method with body in get request

print(f"\n\n//get{name}Like")

print(f"\n\n let searchWindow= document.getElementById(\"searchWindow\");")
print(f"\n\n let searchBar = document.getElementById(\"searchBar\");")
print(f"\n\nconst searchBtn = document.getElementById(\"searchBtn\");")

i=0
r=0


print(f"searchWindow.addEventListener(\'input',async (e)=>{{")
print(f"e.preventDefault();\n")
print(f"\n\nlet choice =[];\n\n")
print(f"const searchList = document.getElementById(\"searchList\");\n\n")
print(f"searchList.innerHTML=``;\n")
print(f"let input=searchBar.value.trim();")
print(f"choice.push([\"id\",`${{input}}`]);")
while i<c:
    if "enum" in lines[i] :
        print(f"\n\nconst {lines[i][ind[i][0]:ind[i][1]]}Choice = document.querySelector(\'input[name=\"{lines[i][ind[i][0]:ind[i][1]]}Choice\"]:checked\');\n  ")
        print(f"if({lines[i][ind[i][0]:ind[i][1]]})")
        print(f"choice.push([\"{lines[i][ind[i][0]:ind[i][1]]}\",{lines[i][ind[i][0]:ind[i][1]]}Choice.value]);\n\n")
    i+=1
print(f"let obj=Object.fromEntries(choice);")
print(f"console.log(obj);")
print(f"let JSONstring=JSON.stringify(obj);")
print(f"console.log(JSONstring);")
print(f" const response = await axios(`/{name}Search`, {{params: obj}});",end="")
i=0

print(f"const data =await response.data;//axios automatically parses also .json() does not work here\n\n try{{ if(response.status==200) //response.ok does not work here\n {{;\ndata.forEach( item => {{")
print(f"const t= document.createElement('li');\n t.innerHTML=`${{item.{lines[1][ind[1][0]:ind[1][1]]}}}`;\n searchList.appendChild(t);\n ")
print(f"}});\n}}else \n console.error(\"An error occurred while searching\"); }} catch(err){{\nconsole.error(\"Error occured while searching\",err);\n}}\n}});")

# get{name}
print(f"\n\n//get{name}()\n\n")
print(f"async function get{name}(){{")

print(f"const {name}List= document.getElementById(\'{name}List\');")
print(f"{name}List.innerHTML=\'\';")
print(f"let data;")
print(f"const response = await fetch(\'{name}\' , {{method:\'GET\'}});")
print(f"if(response.ok)")
print(f"{{")
print(f"data = await response.json();")
print(f"data.forEach(item =>{{")

i=0
while i<c :
    if lines[i][ind[i][0]:ind[i][1]] =='timestamp':
        i+=1
        continue
    print(f"const t{i} = document.createElement(\'p\');")
    print(f"t{i}.innerHTML=`${{item.{lines[i][ind[i][0]:ind[i][1]]}}}`;")
    print(f"{name}List.appendChild(t{i});")
    i+=1
print(f"const del = document.createElement(\'button\');")
print(f"del.innerHTML=`DELETE`")
print(f"del.onclick= () =>{{")
print(f"console.log(\"delete{name} called\");")
print(f"delete{name}(item.{lines[0][ind[0][0]:ind[0][1]]});")
print(f"}}")
print(f"{name}List.appendChild(del)")
print(f"}});")
print(f"}}")
print(f"else")
print(f"console.error(\"An error occured\",response)")
print(f"}}")


#delete{name}()
print(f"\n\n// delete{name}()")
print(f"\n\nasync function delete{name}(id){{")
print(f"const response = await fetch(`/{name}/${{id}}`, {{method:'DELETE'}});")
print(f"let res;")
print(f"if(response.ok)\n {{res=response.json();\n console.log(\"{name} deleted successfully \",res);\n get{name}()}}")
print(f"else\n console.error(\"Failed to delete {name}\");\n}}")

#backendGen
#controllers/{name}.js

print(f"\n\n// controllers/{name}.js\n\n")

print(f"\n\n\nconst {{conn}} = require(\'../db.js\');\nconst mysql = require(\'mysql2\');\n")
print(f"\nconst axios=require(\'axios\');")
print(f"\n//IMP :Recheck if Id matches once again from table")
print(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem")

#get{name}
print(f"// get{name}\n\n")
print(f"const get{name} = (req,res)=> {{\n")
print(f"console.log(\"get{name}() called\")")
print(f" try{{\n conn.query(\"Select * from {name}\" ,(err , results) =>    {{ ")
print(f"if(err)\n console.error(\"Failed to get {name}\",err);\nelse\n res.status(200).json(results);");
print(f" }});\n}} catch(err)\n{{\n")
print(f"console.error(\"Cannot send the {name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};")


#get{name}By
print(f"// get{name}By\n\n")
print(f"// get{name}By\n\n")
print(f"const get{name}By = (req,res)=> {{\n")
print(f"console.log(\"get{name}() called\")")
print(f" try{{\n conn.query(\"Select * from {name} where {name}Id = ?\" ,[req.params.id] ,(err , results) =>    {{ \n//IMP :Recheck if Id matches once again from table")
print(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem")
print(f"if(err)\n console.error(\"Failed to get {name}\",err);\nelse\n res.status(200).json(results);");
print(f" }});\n}} catch(err)\n{{\n")
print(f"console.error(\"Cannot send the {name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};")


#get{name}Like
print(f"// get{name}Like\n\n")

print(f"const get{name}Like = (req,res)=> {{\n")
print(f"console.log(\"get{name}() called\")")
print(f" try{{\n conn.query(\"Select * from {name} where ", end=" ")
r=0
i=0
while i< c:
    t=lines[i][ind[i][2]:ind[i][3]]
    if t=='varchar' :
        print(f" {lines[i][ind[i][0]:ind[i][1]]} like ? " , end= " ")
        r+=1
        i+=1
        break
    i+=1
        
while i< c-1:
    t=lines[i][ind[i][2]:ind[i][3]]
    if t=='varchar' :
        print(f"or {lines[i][ind[i][0]:ind[i][1]]} like ? " , end= " ")
        r+=1
    i+=1
if i<c:
    t=lines[i][ind[i][2]:ind[i][3]]
if t=='varchar':
    print(f"{lines[i][ind[i][0]:ind[i][1]]} like ?\",[" , end= " ")
else :
    print(f"\",[",end="")
i=0
for i in range(r-1):
    print(f"`${{req.params.id}}%`,",end="")
print(f"`${{req.params.id}}%`],",end="")
print(f"(err , results) =>    {{ ")
print(f"if(err)\n console.error(\"Failed to get {name}\",err);\nelse\n res.status(200).json(results);");
print(f" }});\n}} catch(err)\n{{\n")
print(f"console.error(\"Cannot send the {name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};")


#applyFilterSearch{name}

print(f"// applyFilterSearch{name}\n\n")

print(f"const applyFilterSearch{name} = (req,res)=> {{\n")
print(f"console.log(\"applyFilterSearch{name}() called\");")
print(f"console.log(\"params received is\",req.query);")
print(f"\nconst {{ id ",end=" ")
r=0

i=0
while i <c-1 :
    if "enum" in lines[i][ind[i][2]:ind[i][3]] or "Id" in lines[i][ind[i][0]:ind[i][1]] or "id" in lines[i][ind[i][0]:ind[i][1]] or "ID" in lines[i][ind[i][0]:ind[i][1]] :
        if r==0:
            print(f",",end="")
            r+=1
        print(lines[i][ind[i][0]:ind[i][1]],end=",")
    i+=1
print(lines[i][ind[i][0]:ind[i][1]],end=" ")
print(f"}}= req.query;\n")
print(f"let checkFields =[];\nlet checkValues=[];\n")
print(f"checkFields.push(\"true\");\n ")
i=0
while i< c:
    t=lines[i][ind[i][2]:ind[i][3]]
    if t=='enum' :
        print(f"if({lines[i][ind[i][0]:ind[i][1]]})")
        print(f"{{checkFields.push(`{lines[i][ind[i][0]:ind[i][1]]} = ?`);\n checkValues.push(`${{{lines[i][ind[i][0]:ind[i][1]]}}}` );\n}}")
    i+=1
#print(f"{{checkFields.push(`\"true\"= \'?\'`);\n checkValues.push(true );\n}}")
print(f"const query =`Select * from {name} where ${{checkFields.join(\" and \")}} ",end=" ")
r=0
i=0
u=0
while i< c:
    t=lines[i][ind[i][2]:ind[i][3]]
    if t=='varchar' and 'id' not in lines[i][ind[i][0]:ind[i][1]] and 'Id' not in lines[i][ind[i][0]:ind[i][1]] and 'ID' not in lines[i][ind[i][0]:ind[i][1]] and 'Image' not in lines[i][ind[i][0]:ind[i][1]] :
        print(f"and (" ,end=" ")
        u+=1
        print(f"{ lines[i][ind[i][0]:ind[i][1]]} like ? " , end= " ")
        i+=1
        r+=1
        break
    i+=1
while i< c-1:
    t=lines[i][ind[i][2]:ind[i][3]]
    if t=='varchar' and 'id' not in lines[i][ind[i][0]:ind[i][1]] and 'Id' not in lines[i][ind[i][0]:ind[i][1]] and 'ID' not in lines[i][ind[i][0]:ind[i][1]] and 'Image' not in lines[i][ind[i][0]:ind[i][1]] :
        print(f" or {lines[i][ind[i][0]:ind[i][1]]} like ? " , end= " ")
        u+=1
        r+=1
    i+=1

if(i<c):
    t=lines[i][ind[i][2]:ind[i][3]]
if t=='varchar' and 'id' not in lines[i][ind[i][0]:ind[i][1]] and 'Id' not in lines[i][ind[i][0]:ind[i][1]] and 'ID' not in lines[i][ind[i][0]:ind[i][1]] and 'Image' not in lines[i][ind[i][0]:ind[i][1]]:
    print(f"{lines[i][ind[i][0]:ind[i][1]]} like ?\n" )
    r+=1
if u >1:
    print(f")`",end="")
else :
    print(f"`",end="")
i=0
for i in range(r):
    #print(f"req.params.id,",end="")
    print(f"\ncheckValues.push(`${{req.query.id}}%`);")
print(f" try{{\n conn.query(query, ",end=" ")

print(f"checkValues,",end="")
print(f"(err , results) =>    {{ ")
print(f"if(err)\n console.error(\"Failed to applyFilterSearch{name}\",err);\nelse\n res.status(200).json(results);")
print(f" }});\n}} catch(err)\n{{\n")
print(f"console.error(\"Cannot send the applyFilterSearch{name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};\n\n")


#add{name}
print(f"// add{name}\n\n")
print(f"const add{name}= (req ,res) => {{\nif(!conn)\n console.log(\"conn not properly linked to routes\");")
print(f" console.log(\"add{name} Called\");")
print("const {" ,end="")
i=0
while i< c-1:
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print(lines[i][ind[i][0]:ind[i][1]],end=",")
    i+=1  
print(lines[i][ind[i][0]:ind[i][1]],end="")
print("}=req.body;",end="")
print(f"console.log(req.body);\n    conn.query(\"Insert into {name}(", end="")
i=0
while i< c-1:
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print(lines[i][ind[i][0]:ind[i][1]],end=",")
    i+=1
print(lines[i][ind[i][0]:ind[i][1]],end="")
print(") values (" , end="")
i=0
while i<c-1 :
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print("?," , end=" ")
    i+=1
print("?",end="" )
print(")\", [",end="")
i=0
while i< c-1:
    if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
        i+=1
        continue
    print(lines[i][ind[i][0]:ind[i][1]],end=",")
    i+=1
print(lines[i][ind[i][0]:ind[i][1]],end="")
print(f"], (err , result) =>\n {{\n if(err)\n console.error(\"Failed to add {name}\");")
print(f"else\n{{console.log(\"Successfully created {name}\");\n")
print(f"res.status(201).json(result);\n }}\n}});\n}};\n")



#delete{name}

print(f"// delete{name}\n\n")
print(f"const delete{name}= async (req , res)=>{{\nconsole.log(\"delete{name}() called\");\nif(!conn)")
print(f"console.error(\"conn was not routed properly\");\n console.log(\"delete{name} called\");")
print(f"\n//IMP :Recheck if Id matches once again from table")
print(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem")
print(f"conn.query(\"Delete from {name} where {name}Id =?\",[req.params.id], (err, result)=>\n{{")
print(f"if(!err)\nres.status(200).send(\"User deleted successfully\");\nelse\n{{\n")
print(f"console.error(\"An error occured\", err);\n}}\n}});\n}};\n")





#update{name}

print(f"// update{name}\n\n")
print(f"\n\nconst update{name} =async (req , res) => {{ \nconsole.log(\"update{name}() called\");\nif(!conn)\n console.error(\"conn not linked to routes\"); ")
print(f"\nconst {name}Id= req.params.id")
print(f"\nconst {{")
i=0
while i <c-1 :
    print(lines[i][ind[i][0]:ind[i][1]],end=",")
    i+=1
print(lines[i][ind[i][0]:ind[i][1]],end=" ")
print(f"}}= req.body;\n")
print(f"if(!{name}Id||isNaN({name}Id))")
print(f"{{\nconsole.error(\"Invalid {name}Id sent\");\n res.status(404).send(\"Invalid {name}Id\");\n}}")
print(f"let updateFields= [];\n let updateValues=[];\n")
i=1
while i< c:
    print(f"if({lines[i][ind[i][0]:ind[i][1]]}){{\n")
    print(f"updateFields.push(\'{lines[i][ind[i][0]:ind[i][1]]}=?\');")
    print(f"updateValues.push({lines[i][ind[i][0]:ind[i][1]]});\n}}")
    i+=1
print(f"updateValues.push({lines[0][ind[0][0]:ind[0][1]]})")
print(f"if(updateFields.length==0)\n console.error(\"NO field value specified for update\")\n")
print(f"const query  = `update {name} set ${{userFields.join(\',\')}} where {name.capitalize()}Id= \'?\'`;")
print(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem")
print(f"conn.query( query , updateValues, (err , result)=>{{")
print(f"if(err)\n {{console.error(\"Failed to update {name}\");\n res.status(400).send(\"An error occured\", err);\n}}")
print(f"res.status(200).send(result);\n }});\n }} \n")
print(f"module.exports={{get{name} ,add{name} ,delete{name} , update{name} ,get{name}By, get{name}Like ,applyFilterSearch{name}}};\n\n")

#RouteGen


print(f"\n\n// routes/routes.js\n\n\n")
#print(f"\n\n {name} routes")
print(f"const {{add{name},get{name},delete{name} , update{name},applyFilterSearch{name},get{name}Like,get{name}By}}= require('../controllers/{name}.js');")
print(f"Route.get(\'/{name}Page\',(req , res)=>{{\n res.sendFile(path.join(__dirname , \'../views\',\'{name}.html\'));\n}});\n")
print(f"Route.get(\'/{name}\' , get{name});\n\nRoute.post(\'/{name}\' ,add{name});\n\nRoute.delete(\'/{name}/:id\',delete{name});\n\nRoute.put(\'/{name}/:id\',update{name});")
print(f"\n\nRoute.get(\'/{name}By\',get{name}By)\n\nRoute.get(\'/{name}Like\',get{name}Like)\n\n Route.get(\'/{name}Search\',applyFilterSearch{name})")
print(f"\n\n")