const express=require("express");
const app = express();

app.get("/",(req, res)=>{
    res.json ([
        {
            id:1,
            name:"David Nickson",
            age: 29
        }, 
        {
            id:2,
            name:"Nick Davidson",
            age: 27
        }, 
        {
            id:3,
            name:"Julia Roberts",
            age: 35
        },
        {
            id:4,
            name:"Pamerson Andella",
            age: 41
        }, 
        {
            id:5,
            name:"Pamerson Andella",
            age: 41  
        }
    ])
});

app.listen(5000,()=>{
    console.log("app is running")
})