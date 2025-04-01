import mysql.connector


#inputting part
import os
dbname=input("Enter the database name from which to retrieve data\t")


#connecting to database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database=dbname
)

cursor = connection.cursor()
cursor.execute("show tables; ")
tuples = cursor.fetchall()

for tuple in tuples:
    print(tuple)


name= input("Enter the form table Name from which to retrieve data\t")
if name.lower() =='all':
    cursor.execute("select COLUMN_NAME from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where table_schema = %s and CONSTRAINT_NAME='PRIMARY';" ,( dbname))
else :
    cursor.execute("select COLUMN_NAME from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where table_name= %s and table_schema = %s and CONSTRAINT_NAME='PRIMARY';" ,(name , dbname))
primarykey= cursor.fetchone()
print(f"Primary key", primarykey[0])
cursor.execute("select COLUMN_NAME , COLUMN_TYPE FROM information_schema.columns where table_name = %s and table_schema= %s;",( name ,dbname))

rows = cursor.fetchall()

c=0
column=[]
line2=[]
type=[]
lines=[]
en = []
size=[]
totalEnum=0
for row in rows:
    #print(row)
    column.append(row[0])
    #print(f"column[{c}]= ",column[c])
    line2.append(row[1])
    i=0
    #print(f"line2[{c}]= ",line2[c])
    while i< len(line2[c]) :
        if line2[c][i] == '(' :
            break
        i+=1
    type.append(line2[c][0:i])
    #print(f"type[{0}]= ",type[c])
    if type[c]== "enum" :
        
        r=1
        j=i
        while j <len(line2[c]):
            if(line2[c][j]==","):
                r+=1
            j+=1
        j=i
        size.append(r)
        for u in range(r):
            while j <len(line2[c]) and line2[c][j]!='\'':
                j+=1
            j+=1
            s1=j
            while j <len(line2[c]) and line2[c][j]!='\'':
                j+=1
            e1=j
            j+=1
            en.append(line2[c][s1:e1])
            #print(f"en =",en[totalEnum])
            totalEnum+=1
    c+=1
count = 0
co =0
i=0 
ind = []

i=0
k=0
r=0



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
        t=type[i]
        if type[i] == 'int' :
            t='number'
        elif type[i]== 'varchar' :
            t='text'
        elif type[i]=='enum' :
            vh.write(f"\t<select id=\"{column[i]}\" name=\"{column[i]}\">")
            for t in range(size[r]):
                vh.write(f"\t\t<option value=\"{en[k]}\">{en[k]}</option>")
                k+=1
            vh.write(f"\t</select>")
            i+=1
            r+=1
            continue
        elif type[i]=='timestamp':
            i+=1
            continue
        elif type[i]=='datetime' :
            t='datetime-local'
        elif type[i] =='decimal':
            vh.write(f"\t<input type=\"decimalInput\" id=\"{column[i]}\" placeholder=\"{column[i]}\" step=\"0.01\"/> ")
            i+=1
            continue
        elif type[i]=='tinyint':
            t='number'

        vh.write(f"\t<input type=\"{t}\" id=\"{column[i]}\" placeholder=\"{column[i]}\"/> ")
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
        if "enum" in type[i] :
            for t in range(size[r]):
                print(f"\t\t<input type=\"radio\" name=\"{column[i]}Choice\" value=\"{en[k]}\">{en[k]}</input>\n")
                vh.write(f"\t\t<input type=\"radio\" name=\"{column[i]}Choice\" value=\"{en[k]}\">{en[k]}</input>")
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
        if(type[i]=='timestamp'):
            i+=1
            continue
        vj.write(f"const {column[i]}= document.getElementById(\'{column[i]}\').value.trim()\n\n")
        i+=1
    vj.write(f"const formData=new FormData()\n")
    i=0
    while i<c :
        if(type[i]=='timestamp'):
            i+=1
            continue
        vj.write(f"formData.append(\'{column[i]}\',{column[i]})\n")
        i+=1
    i=0
    vj.write(f"const {name}Data= {{\n")
    while i<c -1:
        if(type[i]=='timestamp'):
            i+=1
            continue
        vj.write(f"{column[i]} ,")
        i+=1
    if(type[i]!='timestamp'):
        vj.write(f"{column[i]}")
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
        if "enum" in type[i] :
            vj.write(f"\n\nconst {column[i]}Choice = document.querySelector(\'input[name=\"{column[i]}Choice\"]:checked\');\n  \n")
            vj.write(f"if({column[i]})\n")
            vj.write(f"choice.push([\"{column[i]}\",{column[i]}Choice.value]);\n\n\n")
        i+=1
    vj.write(f"let obj=Object.fromEntries(choice);\n")
    vj.write(f"console.log(obj);\n")
    vj.write(f"let JSONstring=JSON.stringify(obj);\n")
    vj.write(f"console.log(JSONstring);\n")
    vj.write(f" const response = await axios(`/{name}Search`, {{params: obj}});\n")
    i=0

    vj.write(f"const data =await response.data;//axios automatically parses also .json() does not work here\n\n try{{ if(response.status==200) //response.ok does not work here\n {{;\ndata.forEach( item => {{\n")
    vj.write(f"const t= document.createElement('li');\n t.innerHTML=`${{item.{column[1]}}}`;\n searchList.appendChild(t);\n \n")
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
        if column[i] =='timestamp':
            i+=1
            continue
        vj.write(f"const t{i} = document.createElement(\'p\');\n")
        vj.write(f"t{i}.innerHTML=`${{item.{column[i]}}}`;\n")
        vj.write(f"{name}List.appendChild(t{i});\n")
        i+=1
    vj.write(f"const del = document.createElement(\'button\');\n")
    vj.write(f"del.innerHTML=`DELETE`\n")
    vj.write(f"del.onclick= () =>{{\n")
    vj.write(f"console.log(\"delete{name} called\");\n")
    vj.write(f"delete{name}(item.{column[0]});\n")
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
    cj.write(f" try{{\n conn.query(\"Select * from {name} where {primarykey[0]} = ?\" ,[req.params.id] ,(err , results) =>    {{ \n//IMP :Recheck if Id matches once again from table\n")
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
        t=type[i]
        if type[i]=='varchar' :
            cj.write(f" {column[i]} like ? " )
            r+=1
            i+=1
            break
        i+=1
            
    while i< c-1:
        t=type[i]
        if type[i]=='varchar' :
            cj.write(f"or {column[i]} like ? ")
            r+=1
        i+=1
    if i<c:
        t=type[i]
    if type[i]=='varchar':
        cj.write(f"{column[i]} like ?\",[")
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
        if "enum" in type[i] or "Id" in column[i] or "id" in column[i] or "ID" in column[i] :
            if r==0:
                cj.write(f",")
                r+=1
            cj.write(f"{column[i]},")
        i+=1
    cj.write(f"{column[i]} " )
    cj.write(f"}}= req.query;\n\n")
    cj.write(f"let checkFields =[];\nlet checkValues=[];\n\n")
    cj.write(f"checkFields.push(\"true\");\n \n")
    i=0
    while i< c:
        t=type[i]
        if type[i]=='enum' :
            cj.write(f"if({column[i]})\n")
            cj.write(f"{{checkFields.push(`{column[i]} = ?`);\n checkValues.push(`${{{column[i]}}}` );\n}}\n")
        i+=1
    #cj.write(f"{{checkFields.push(`\"true\"= \'?\'`);\n checkValues.push(true );\n}}\n")
    cj.write(f"const query =`Select * from {name} where ${{checkFields.join(\" and \")}} ")
    r=0
    i=0
    u=0
    while i< c:
        t=type[i]
        if type[i]=='varchar' and 'id' not in column[i] and 'Id' not in column[i] and 'ID' not in column[i] and 'Image' not in column[i] :
            cj.write(f"and (")
            u+=1
            cj.write(f"{ column[i]} like ? ")
            i+=1
            r+=1
            break
        i+=1
    while i< c-1:
        t=type[i]
        if type[i]=='varchar' and 'id' not in column[i] and 'Id' not in column[i] and 'ID' not in column[i] and 'Image' not in column[i] :
            cj.write(f" or {column[i]} like ? ")
            u+=1
            r+=1
        i+=1

    if(i<c):
        t=type[i]
    if type[i]=='varchar' and 'id' not in column[i] and 'Id' not in column[i] and 'ID' not in column[i] and 'Image' not in column[i]:
        cj.write(f"{column[i]} like ?\n" )
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
        if(type[i]=='timestamp'):
            i+=1
            continue
        cj.write(f"{column[i]},")
        i+=1  
    cj.write(f"{column[i]}")
    cj.write("}=req.body;")
    cj.write(f"console.log(req.body);\n    conn.query(\"Insert into {name}(")
    i=0
    while i< c-1:
        if(type[i]=='timestamp'):
            i+=1
            continue
        cj.write(f"{column[i]} ,")
        i+=1
    cj.write(f"{column[i]}")
    cj.write(") values (")
    i=0
    while i<c-1 :
        if(type[i]=='timestamp'):
            i+=1
            continue
        cj.write("?,")
        i+=1
    cj.write("?" )
    cj.write(")\", [")
    i=0
    while i< c-1:
        if(type[i]=='timestamp'):
            i+=1
            continue
        cj.write(f"{column[i]},")
        i+=1
    cj.write(f"{column[i]}")
    cj.write(f"], (err , result) =>\n {{\n if(err)\n console.error(\"Failed to add {name}\");\n")
    cj.write(f"else\n{{console.log(\"Successfully created {name}\");\n\n")
    cj.write(f"res.status(201).json(result);\n }}\n}});\n}};\n\n")



    #delete{name}

    cj.write(f"// delete{name}\n\n\n")
    cj.write(f"const delete{name}= async (req , res)=>{{\nconsole.log(\"delete{name}() called\");\nif(!conn)\n")
    cj.write(f"console.error(\"conn was not routed properly\");\n console.log(\"delete{name} called\");\n")
    cj.write(f"\n//IMP :Recheck if Id matches once again from table\n")
    cj.write(f"//Since mysql is case insensitive case might not be that necessary at all but changes like ActivityId instead of activitiesId cause problem\n")
    cj.write(f"conn.query(\"Delete from {name} where {primarykey[0]} =?\",[req.params.id], (err, result)=>\n{{\n")
    cj.write(f"if(!err)\nres.status(200).send(\"User deleted successfully\");\nelse\n{{\n\n")
    cj.write(f"console.error(\"An error occured\", err);\n}}\n}});\n}};\n\n")





    #update{name}

    cj.write(f"// update{name}\n\n\n")
    cj.write(f"\n\nconst update{name} =async (req , res) => {{ \nconsole.log(\"update{name}() called\");\nif(!conn)\n console.error(\"conn not linked to routes\"); \n")
    cj.write(f"\nconst {name}Id= req.params.id\n")
    cj.write(f"\nconst {{\n")
    i=0
    while i <c-1 :
        cj.write(f"{column[i]}")
        i+=1
    cj.write(f"{column[i]}")
    cj.write(f"}}= req.body;\n\n")
    cj.write(f"if(!{name}Id||isNaN({name}Id))\n")
    cj.write(f"{{\nconsole.error(\"Invalid {name}Id sent\");\n res.status(404).send(\"Invalid {name}Id\");\n}}\n")
    cj.write(f"let updateFields= [];\n let updateValues=[];\n\n")
    i=1
    while i< c:
        cj.write(f"if({column[i]}){{\n\n")
        cj.write(f"updateFields.push(\'{column[i]}=?\');\n")
        cj.write(f"updateValues.push({column[i]});\n}}\n")
        i+=1
    cj.write(f"updateValues.push({column[0]})\n")
    cj.write(f"if(updateFields.length==0)\n console.error(\"NO field value specified for update\")\n\n")
    cj.write(f"const query  = `update {name} set ${{userFields.join(\',\')}} where {primarykey[0]}= \'?\'`;\n")
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










cursor.close()

connection.close()