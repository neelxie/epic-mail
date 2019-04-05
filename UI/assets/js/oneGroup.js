window.onload = function(){
    let my_url = location.href
    let url = new URL(my_url)
    let group_id = url.searchParams.get('group_id')
    getOneGroupy(group_id);
}

function getOneGroupy(groupy_id){
    token = localStorage.getItem('token');
    
    if (token === null) {
        alert('You must log in');
        window.location.replace('index.html');
    }
    fetch('https://my-epic-mail.herokuapp.com/api/v2/groups/'+groupy_id, {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.status === 400){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
        }
        if (data.status === 401){
            document.getElementById('blank').style.display = "block";
            document.getElementById('blank').innerHTML = data.error;
            window.location.replace('index.html');
        }
        if (data.status === 200){
            console.log(data['data'])
            data.data.forEach((group) => {
                document.getElementById("group_id").innerHTML=`${group.group_id}`;
                document.getElementById("group_name").innerHTML=`${group.group_name}`;
                document.getElementById("admin").innerHTML=`${group.created_by}`;
                document.getElementById("created_on").innerHTML=`${group.created_on}`;
            })    
        }
    });
    
}