#inputting part
import os
dbname=input("Enter the database name\t")
name= input("Enter the form table Name\t")
print("Enter sequence")
print(f"The sequence must be of the form\n\n\n select COLUMN_NAME , COLUMN_TYPE FROM information_schema.columns where table_name = \'{name}\' and table_schema= \'{dbname}\';\n\n")

print(f"Paste the query into mysql to generate the WebTemplate\n")
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


#Handling files



viewsdirectory='views'
viewsfilehtml= f"{name}.html"
viewsfilejs=f"{name}.js"
os.makedirs(viewsdirectory,exist_ok=True)


viewshtml = os.path.join(viewsdirectory,viewsfilehtml)
viewsjs   = os.path.join(viewsdirectory,viewsfilejs)


#os.makedirs(viewsdirectory,exist_ok=True)
controllersdirectory='controllers'
controllersfilejs=f"{name}.js"
os.makedirs(controllersdirectory,exist_ok=True)
controllersjs=os.path.join(controllersdirectory,controllersfilejs)

routesdirectory= 'Routes'
routesfilejs= 'routes.js'
os.makedirs(routesdirectory,exist_ok=True)
routesjs =os.path.join(routesdirectory,routesfilejs)


with open(viewshtml,'w') as vh:
    vh.write(f"<!DOCTYPE html>\n")
    vh.write(f"<html lang=\"en\">\n")
    vh.write(f"<head>\n")
    vh.write(f"    <meta charset=\"UTF-8\">\n")
    vh.write(f"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    vh.write(f"    <title>{name.capitalize()}</title>\n")
    vh.write(f"</head>\n")
    vh.write(f"<body>\n")
    #Frontend code
    # Html Part


    vh.write(f"\n\n\n<!--Frontend code-->")

    vh.write(f"\n\n<!--{viewsdirectory}/{name}.html-->")

    #form part

    vh.write(f"<script src=\"https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js\"></script>")

    vh.write(f"\n\n<!--Form submission part-->\n\n")
    i=0
    r=0
    k=0
    vh.write(f"\n\n\n\n<form enctype=\"multipart/form-data\" id =\"{name}\">")
    while i< c:
        vh.write("\n")
        t=lines[i][ind[i][2]:ind[i][3]]
        if t == 'int' :
            t='number'
        elif t== 'varchar' :
            t='text'
        elif t=='enum' :
            vh.write(f"\t<select id=\"{lines[i][ind[i][0]:ind[i][1]]}\" name=\"{lines[i][ind[i][0]:ind[i][1]]}\">")
            for t in range(size[r]):
                vh.write(f"\t\t<option value=\"{en[k]}\">{en[k]}</option>")
                k+=1
            vh.write(f"\t</select>")
            i+=1
            r+=1
            continue
        elif t=='timestamp':
            i+=1
            continue
        elif t=='datetime' :
            t='datetime-local'
        elif t =='decimal':
            vh.write(f"\t<input type=\"decimalInput\" id=\"{lines[i][ind[i][0]:ind[i][1]]}\" placeholder=\"{lines[i][ind[i][0]:ind[i][1]]}\" step=\"0.01\"/> ")
            i+=1
            continue
        elif t=='tinyint':
            t='number'

        vh.write(f"\t<input type=\"{t}\" id=\"{lines[i][ind[i][0]:ind[i][1]]}\" placeholder=\"{lines[i][ind[i][0]:ind[i][1]]}\"/> ")
        i+=1
    vh.write(f"\n\n<input type=\"submit\" id =\"{name}Sub\"/>\n\n</form>")
    i=0
    i=0 
    k=0

    #Filter Search HTml Part
    #Radio button and search bar
    vh.write(f"\n\n<!--Radio button and search bar-->\n\n")
    vh.write(f"\n\n<form id =\"searchWindow\">\n  ")
    vh.write(f"\n\n<input type=\"text\" placeholder=\"Search\" id= \"searchBar\"/>")
    vh.write(f"\n\n<ul id=\"searchList\"></ul>")
    vh.write(f"\n\n<button id =\"searchBtn\"> &#x1F50D</button> ")
    r=0
    while i<c:
        if "enum" in lines[i] :
            for t in range(size[r]):
                vh.write(f"\t\t<input type=\"radio\" name=\"{lines[i][ind[i][0]:ind[i][1]]}Choice\" value=\"{en[k]}\">{en[k]}</input>")
                k+=1
                vh.write(f"\n")
            
            r+=1
        i+=1
    vh.write(f"\n</form>\n\n")
    vh.write(f"\n<li id=\"{name}List\"></li>\n\n")
    vh.write(f"\n\n<script src=\"{name}.js\"></script>\n\n")
    i=0
    vh.write(f"</body>\n")
    vh.write(f"</html>\n")

print(f"Frontend generated at {viewshtml}")

with open(viewsjs,'w') as vj :
    
    #Frontend code
    #Javascript part

    vj.write(f"\n\n// views/{name}.js\n\n\n")

    vj.write(f"\nconst {name}=document.getElementById(\'{name}\') ;\n")
    #add{name}

    vj.write(f"\n\nget{name}()// Do not delete this it must be called at the start\n")
    vj.write(f"\n\n //add{name}\n\n\n")
    vj.write(f"{name}.addEventListener(\'submit\' , (e)=>\n \n")
    vj.write("{e.preventDefault();\n\n")
    while i<c :
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        vj.write(f"const {lines[i][ind[i][0]:ind[i][1]]}= document.getElementById(\'{lines[i][ind[i][0]:ind[i][1]]}\').value.trim()\n\n")
        i+=1
    vj.write(f"const formData=new FormData()\n")
    i=0
    while i<c :
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        vj.write(f"formData.append(\'{lines[i][ind[i][0]:ind[i][1]]}\',{lines[i][ind[i][0]:ind[i][1]]})\n")
        i+=1
    i=0
    vj.write(f"const {name}Data= {{\n")
    while i<c -1:
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        vj.write(f"{lines[i][ind[i][0]:ind[i][1]]} ,")
        i+=1
    if(lines[i][ind[i][2]:ind[i][3]]!='timestamp'):
        vj.write(f"{lines[i][ind[i][0]:ind[i][1]]}")
    vj.write("};\n\n")
    vj.write(f"const res =fetch('/{name}',{{method:\'POST\',body:formData}}).then(data=>data.json()).catch(err => console.log(\"An error occured\" , err));\n")
    vj.write(f"const response =fetch('/{name}',{{method:\'POST\',headers :{{\'Content-Type\':\'application/json\'}},body:JSON.stringify({name}Data)}}).then(data=>data.json()).catch(err => console.log(\"An error occured\" , err));\n")
    vj.write(f"if(response.ok)\n get{name}();\n")
    vj.write(f"}});\n")

    #get{name}Like
    #unconventional method with body in get request

    vj.write(f"\n\n//get{name}Like\n")

    vj.write(f"\n\n let searchWindow= document.getElementById(\"searchWindow\");\n")
    vj.write(f"\n\n let searchBar = document.getElementById(\"searchBar\");\n")
    vj.write(f"\n\nconst searchBtn = document.getElementById(\"searchBtn\");\n")

    i=0
    r=0


    vj.write(f"searchWindow.addEventListener(\'input',async (e)=>{{\n")
    vj.write(f"e.preventDefault();\n\n")
    vj.write(f"\n\nlet choice =[];\n\n\n")
    vj.write(f"const searchList = document.getElementById(\"searchList\");\n\n\n")
    vj.write(f"searchList.innerHTML=``;\n\n")
    vj.write(f"let input=searchBar.value.trim();\n")
    vj.write(f"choice.push([\"id\",`${{input}}`]);\n")
    while i<c:
        if "enum" in lines[i] :
            vj.write(f"\n\nconst {lines[i][ind[i][0]:ind[i][1]]}Choice = document.querySelector(\'input[name=\"{lines[i][ind[i][0]:ind[i][1]]}Choice\"]:checked\');\n  \n")
            vj.write(f"if({lines[i][ind[i][0]:ind[i][1]]})\n")
            vj.write(f"choice.push([\"{lines[i][ind[i][0]:ind[i][1]]}\",{lines[i][ind[i][0]:ind[i][1]]}Choice.value]);\n\n\n")
        i+=1
    vj.write(f"let obj=Object.fromEntries(choice);\n")
    vj.write(f"console.log(obj);\n")
    vj.write(f"let JSONstring=JSON.stringify(obj);\n")
    vj.write(f"console.log(JSONstring);\n")
    vj.write(f" const response = await axios(`/{name}Search`, {{params: obj}});\n")
    i=0

    vj.write(f"const data =await response.data;//axios automatically parses also .json() does not work here\n\n try{{ if(response.status==200) //response.ok does not work here\n {{;\ndata.forEach( item => {{\n")
    vj.write(f"const t= document.createElement('li');\n t.innerHTML=`${{item.{lines[1][ind[1][0]:ind[1][1]]}}}`;\n searchList.appendChild(t);\n \n")
    vj.write(f"}});\n}}else \n console.error(\"An error occurred while searching\"); }} catch(err){{\nconsole.error(\"Error occured while searching\",err);\n}}\n}});\n")

    # get{name}
    vj.write(f"\n\n//get{name}()\n\n\n")
    vj.write(f"async function get{name}(){{\n")

    vj.write(f"const {name}List= document.getElementById(\'{name}List\');\n")
    vj.write(f"{name}List.innerHTML=\'\';\n")
    vj.write(f"let data;\n")
    vj.write(f"const response = await fetch(\'{name}\' , {{method:\'GET\'}});\n")
    vj.write(f"if(response.ok)\n")
    vj.write(f"{{\n")
    vj.write(f"data = await response.json();\n")
    vj.write(f"data.forEach(item =>{{\n")

    i=0
    while i<c :
        if lines[i][ind[i][0]:ind[i][1]] =='timestamp':
            i+=1
            continue
        vj.write(f"const t{i} = document.createElement(\'p\');\n")
        vj.write(f"t{i}.innerHTML=`${{item.{lines[i][ind[i][0]:ind[i][1]]}}}`;\n")
        vj.write(f"{name}List.appendChild(t{i});\n")
        i+=1
    vj.write(f"const del = document.createElement(\'button\');\n")
    vj.write(f"del.innerHTML=`DELETE`\n")
    vj.write(f"del.onclick= () =>{{\n")
    vj.write(f"console.log(\"delete{name} called\");\n")
    vj.write(f"delete{name}(item.{lines[0][ind[0][0]:ind[0][1]]});\n")
    vj.write(f"}}\n")
    vj.write(f"{name}List.appendChild(del)\n")
    vj.write(f"}});\n")
    vj.write(f"}}\n")
    vj.write(f"else\n")
    vj.write(f"console.error(\"An error occured\",response)\n")
    vj.write(f"}}\n")


    #delete{name}()
    vj.write(f"\n\n// delete{name}()\n")
    vj.write(f"\n\nasync function delete{name}(id){{\n")
    vj.write(f"const response = await fetch(`/{name}/${{id}}`, {{method:'DELETE'}});\n")
    vj.write(f"let res;\n")
    vj.write(f"if(response.ok)\n {{res=response.json();\n console.log(\"{name} deleted successfully \",res);\n get{name}()}}\n")
    vj.write(f"else\n console.error(\"Failed to delete {name}\");\n}}\n")



print(f"Frontend generated at /{viewsdirectory}/{name}.js\n")


with open(controllersjs,'w') as cj :
        #backendGen
    #controllers/{name}.js

    cj.write(f"\n\n// controllers/{name}.js\n\n\n")

    cj.write(f"\n\n\nconst {{conn}} = require(\'../db.js\');\nconst mysql = require(\'mysql2\');\n\n")
    cj.write(f"\nconst axios=require(\'axios\');\n")
    cj.write(f"\n//IMP :Recheck if Id matches once again from table\n")
    cj.write(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem\n")

    #get{name}
    cj.write(f"// get{name}\n\n\n")
    cj.write(f"const get{name} = (req,res)=> {{\n\n")
    cj.write(f"console.log(\"get{name}() called\");\n")
    cj.write(f" try{{\n conn.query(\"Select * from {name}\" ,(err , results) =>    {{ \n")
    cj.write(f"if(err)\n console.error(\"Failed to get {name}\",err);\nelse\n res.status(200).json(results);\n")
    cj.write(f" }});\n}} catch(err)\n{{\n\n")
    cj.write(f"console.error(\"Cannot send the {name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};\n")


    #get{name}By
    cj.write(f"// get{name}By\n\n\n")
    cj.write(f"// get{name}By\n\n\n")
    cj.write(f"const get{name}By = (req,res)=> {{\n\n")
    cj.write(f"console.log(\"get{name}() called\");\n")
    cj.write(f" try{{\n conn.query(\"Select * from {name} where {name}Id = ?\" ,[req.params.id] ,(err , results) =>    {{ \n//IMP :Recheck if Id matches once again from table\n")
    cj.write(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem\n")
    cj.write(f"if(err)\n console.error(\"Failed to get {name}\",err);\nelse\n res.status(200).json(results);\n")
    cj.write(f" }});\n}} catch(err)\n{{\n\n")
    cj.write(f"console.error(\"Cannot send the {name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};\n")


    #get{name}Like
    cj.write(f"// get{name}Like\n\n\n")

    cj.write(f"const get{name}Like = (req,res)=> {{\n\n")
    cj.write(f"console.log(\"get{name}() called\");\n")
    cj.write(f" try{{\n conn.query(\"Select * from {name} where ")
    r=0
    i=0
    while i< c:
        t=lines[i][ind[i][2]:ind[i][3]]
        if t=='varchar' :
            cj.write(f" {lines[i][ind[i][0]:ind[i][1]]} like ? " )
            r+=1
            i+=1
            break
        i+=1
            
    while i< c-1:
        t=lines[i][ind[i][2]:ind[i][3]]
        if t=='varchar' :
            cj.write(f"or {lines[i][ind[i][0]:ind[i][1]]} like ? ")
            r+=1
        i+=1
    if i<c:
        t=lines[i][ind[i][2]:ind[i][3]]
    if t=='varchar':
        cj.write(f"{lines[i][ind[i][0]:ind[i][1]]} like ?\",[")
    else :
        cj.write(f"\",[")
    i=0
    for i in range(r-1):
        cj.write(f"`${{req.params.id}}%`,")
    cj.write(f"`${{req.params.id}}%`],")
    cj.write(f"(err , results) =>    {{ \n")
    cj.write(f"if(err)\n console.error(\"Failed to get {name}\",err);\nelse\n res.status(200).json(results);\n")
    cj.write(f" }});\n}} catch(err)\n{{\n\n")
    cj.write(f"console.error(\"Cannot send the {name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};\n")


    #applyFilterSearch{name}

    cj.write(f"// applyFilterSearch{name}\n\n\n")

    cj.write(f"const applyFilterSearch{name} = (req,res)=> {{\n\n")
    cj.write(f"console.log(\"applyFilterSearch{name}() called\");\n")
    cj.write(f"console.log(\"params received is\",req.query);\n")
    cj.write(f"\nconst {{ id ")
    r=0

    i=0
    while i <c-1 :
        if "enum" in lines[i][ind[i][2]:ind[i][3]] or "Id" in lines[i][ind[i][0]:ind[i][1]] or "id" in lines[i][ind[i][0]:ind[i][1]] or "ID" in lines[i][ind[i][0]:ind[i][1]] :
            if r==0:
                cj.write(f",")
                r+=1
            cj.write(f"{lines[i][ind[i][0]:ind[i][1]]},")
        i+=1
    cj.write(f"{lines[i][ind[i][0]:ind[i][1]]} " )
    cj.write(f"}}= req.query;\n\n")
    cj.write(f"let checkFields =[];\nlet checkValues=[];\n\n")
    cj.write(f"checkFields.push(\"true\");\n \n")
    i=0
    while i< c:
        t=lines[i][ind[i][2]:ind[i][3]]
        if t=='enum' :
            cj.write(f"if({lines[i][ind[i][0]:ind[i][1]]})\n")
            cj.write(f"{{checkFields.push(`{lines[i][ind[i][0]:ind[i][1]]} = ?`);\n checkValues.push(`${{{lines[i][ind[i][0]:ind[i][1]]}}}` );\n}}\n")
        i+=1
    #cj.write(f"{{checkFields.push(`\"true\"= \'?\'`);\n checkValues.push(true );\n}}\n")
    cj.write(f"const query =`Select * from {name} where ${{checkFields.join(\" and \")}} ")
    r=0
    i=0
    u=0
    while i< c:
        t=lines[i][ind[i][2]:ind[i][3]]
        if t=='varchar' and 'id' not in lines[i][ind[i][0]:ind[i][1]] and 'Id' not in lines[i][ind[i][0]:ind[i][1]] and 'ID' not in lines[i][ind[i][0]:ind[i][1]] and 'Image' not in lines[i][ind[i][0]:ind[i][1]] :
            cj.write(f"and (")
            u+=1
            cj.write(f"{ lines[i][ind[i][0]:ind[i][1]]} like ? ")
            i+=1
            r+=1
            break
        i+=1
    while i< c-1:
        t=lines[i][ind[i][2]:ind[i][3]]
        if t=='varchar' and 'id' not in lines[i][ind[i][0]:ind[i][1]] and 'Id' not in lines[i][ind[i][0]:ind[i][1]] and 'ID' not in lines[i][ind[i][0]:ind[i][1]] and 'Image' not in lines[i][ind[i][0]:ind[i][1]] :
            cj.write(f" or {lines[i][ind[i][0]:ind[i][1]]} like ? ")
            u+=1
            r+=1
        i+=1

    if(i<c):
        t=lines[i][ind[i][2]:ind[i][3]]
    if t=='varchar' and 'id' not in lines[i][ind[i][0]:ind[i][1]] and 'Id' not in lines[i][ind[i][0]:ind[i][1]] and 'ID' not in lines[i][ind[i][0]:ind[i][1]] and 'Image' not in lines[i][ind[i][0]:ind[i][1]]:
        cj.write(f"{lines[i][ind[i][0]:ind[i][1]]} like ?\n" )
        r+=1
    if u >1:
        cj.write(f")` ")
    else :
        cj.write(f"` ")
    i=0
    for i in range(r):
        #cj.write(f"req.params.id,",end="\n")
        cj.write(f"\ncheckValues.push(`${{req.query.id}}%`);\n")
    cj.write(f" try{{\n conn.query(query, ")

    cj.write(f"checkValues,")
    cj.write(f"(err , results) =>    {{ \n")
    cj.write(f"if(err)\n console.error(\"Failed to applyFilterSearch{name}\",err);\nelse\n res.status(200).json(results);\n")
    cj.write(f" }});\n}} catch(err)\n{{\n\n")
    cj.write(f"console.error(\"Cannot send the applyFilterSearch{name}\",err);\n res.status(500).send({{error:err}});\n}}\n}};\n\n\n")


    #add{name}
    cj.write(f"// add{name}\n\n\n")
    cj.write(f"//{name}id might not be auto generate in that case you need to manually insert {name}Id or {name}ID\n\n")
    cj.write(f"const add{name}= (req ,res) => {{\nif(!conn)\n console.log(\"conn not properly linked to routes\");\n")
    cj.write(f" console.log(\"add{name} Called\");\n")
    cj.write(f"//{name}id might not be auto generate in that case you need to manually insert {name}Id or {name}ID\n\n")
    cj.write("const {")
    i=0
    while i< c-1:
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        cj.write(f"{lines[i][ind[i][0]:ind[i][1]]},")
        i+=1  
    cj.write(f"{lines[i][ind[i][0]:ind[i][1]]}")
    cj.write("}=req.body;")
    cj.write(f"console.log(req.body);\n    conn.query(\"Insert into {name}(")
    i=0
    while i< c-1:
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        cj.write(f"{lines[i][ind[i][0]:ind[i][1]]} ,")
        i+=1
    cj.write(f"{lines[i][ind[i][0]:ind[i][1]]}")
    cj.write(") values (")
    i=0
    while i<c-1 :
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        cj.write("?,")
        i+=1
    cj.write("?" )
    cj.write(")\", [")
    i=0
    while i< c-1:
        if(lines[i][ind[i][2]:ind[i][3]]=='timestamp'):
            i+=1
            continue
        cj.write(f"{lines[i][ind[i][0]:ind[i][1]]},")
        i+=1
    cj.write(f"{lines[i][ind[i][0]:ind[i][1]]}")
    cj.write(f"], (err , result) =>\n {{\n if(err)\n console.error(\"Failed to add {name}\");\n")
    cj.write(f"else\n{{console.log(\"Successfully created {name}\");\n\n")
    cj.write(f"res.status(201).json(result);\n }}\n}});\n}};\n\n")



    #delete{name}

    cj.write(f"// delete{name}\n\n\n")
    cj.write(f"const delete{name}= async (req , res)=>{{\nconsole.log(\"delete{name}() called\");\nif(!conn)\n")
    cj.write(f"console.error(\"conn was not routed properly\");\n console.log(\"delete{name} called\");\n")
    cj.write(f"\n//IMP :Recheck if Id matches once again from table\n")
    cj.write(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem\n")
    cj.write(f"conn.query(\"Delete from {name} where {name}Id =?\",[req.params.id], (err, result)=>\n{{\n")
    cj.write(f"if(!err)\nres.status(200).send(\"User deleted successfully\");\nelse\n{{\n\n")
    cj.write(f"console.error(\"An error occured\", err);\n}}\n}});\n}};\n\n")





    #update{name}

    cj.write(f"// update{name}\n\n\n")
    cj.write(f"\n\nconst update{name} =async (req , res) => {{ \nconsole.log(\"update{name}() called\");\nif(!conn)\n console.error(\"conn not linked to routes\"); \n")
    cj.write(f"\nconst {name}Id= req.params.id\n")
    cj.write(f"\nconst {{\n")
    i=0
    while i <c-1 :
        cj.write(f"{lines[i][ind[i][0]:ind[i][1]]}")
        i+=1
    cj.write(f"{lines[i][ind[i][0]:ind[i][1]]}")
    cj.write(f"}}= req.body;\n\n")
    cj.write(f"if(!{name}Id||isNaN({name}Id))\n")
    cj.write(f"{{\nconsole.error(\"Invalid {name}Id sent\");\n res.status(404).send(\"Invalid {name}Id\");\n}}\n")
    cj.write(f"let updateFields= [];\n let updateValues=[];\n\n")
    i=1
    while i< c:
        cj.write(f"if({lines[i][ind[i][0]:ind[i][1]]}){{\n\n")
        cj.write(f"updateFields.push(\'{lines[i][ind[i][0]:ind[i][1]]}=?\');\n")
        cj.write(f"updateValues.push({lines[i][ind[i][0]:ind[i][1]]});\n}}\n")
        i+=1
    cj.write(f"updateValues.push({lines[0][ind[0][0]:ind[0][1]]})\n")
    cj.write(f"if(updateFields.length==0)\n console.error(\"NO field value specified for update\")\n\n")
    cj.write(f"const query  = `update {name} set ${{userFields.join(\',\')}} where {name.capitalize()}Id= \'?\'`;\n")
    cj.write(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem\n")
    cj.write(f"conn.query( query , updateValues, (err , result)=>{{\n")
    cj.write(f"if(err)\n {{console.error(\"Failed to update {name}\");\n res.status(400).send(\"An error occured\", err);\n}}\n")
    cj.write(f"res.status(200).send(result);\n }});\n }} \n\n")
    cj.write(f"module.exports={{get{name} ,add{name} ,delete{name} , update{name} ,get{name}By, get{name}Like ,applyFilterSearch{name}}};\n\n\n")


print(f"Backend generated at {controllersdirectory} /{name}")

#printing routes

print(f"\n\n//Printing Routes\n\n\n")
#RouteGen


print(f"\n\n// routes/routes.js\n\n\n")
#print(f"\n\n {name} routes")
print(f"const {{add{name},get{name},delete{name} , update{name},applyFilterSearch{name},get{name}Like,get{name}By}}= require('../controllers/{name}.js');")
print(f"Route.get(\'/{name}Page\',(req , res)=>{{\n res.sendFile(path.join(__dirname , \'../views\',\'{name}.html\'));\n}});\n")
print(f"Route.get(\'/{name}\' , get{name});\n\nRoute.post(\'/{name}\' ,add{name});\n\nRoute.delete(\'/{name}/:id\',delete{name});\n\nRoute.put(\'/{name}/:id\',update{name});")
print(f"\n\nRoute.get(\'/{name}By\',get{name}By);\n\nRoute.get(\'/{name}Like\',get{name}Like);\n\n Route.get(\'/{name}Search\',applyFilterSearch{name});")
print(f"\n\n")